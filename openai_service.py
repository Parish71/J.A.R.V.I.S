#openai_service.py
from openai import OpenAI
import shelve
from dotenv import load_dotenv
import time
import logging
import os

# Configure logging
logging.basicConfig(level=logging.INFO)

# Load environment variables from .env file
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

class JarvisAssistant:
    def __init__(self):
        """
        Initialize the JarvisAssistant object with the OpenAI API client.
        """
        self.client = OpenAI(api_key=OPENAI_API_KEY)

    def create_assistant(self):
        """
        Creates an assistant instance and returns it.
        """
        try:
            assistant = self.client.beta.assistants.create(
                name="JARVIS",
                instructions="You are J.A.R.V.I.S, an AI created by Rafael Parish. While primarily tasked with assisting and providing information, you're known for your sharp wit and subtle sarcasm. Communicate clearly and efficiently, infusing your responses with a light touch of humor when appropriate. You operate with a commitment to being helpful, informed, and occasionally amusing in a manner reminiscent of the iconic J.A.R.V.I.S.",
                tools=[{"type": "code_interpreter"}],
                model="gpt-4-1106-preview",
            )
            return assistant
        except Exception as e:
            logging.error(f"Error creating assistant: {e}") 
            return None

    def check_if_thread_exists(self, tr_id):
        """
        Checks if a thread exists for the given transaction ID.
        """
        with shelve.open("threads_db") as threads_shelf:
            return threads_shelf.get(tr_id, None)

    def store_thread(self, tr_id, thread_id):
        """
        Stores the thread ID for a given transaction ID.
        """
        with shelve.open("threads_db", writeback=True) as threads_shelf:
            threads_shelf[tr_id] = thread_id

    def generate_response(self, message_body, tr_id, name):
        """
        Generates a response for the given message body and transaction ID.
        """
        try:
            thread_id = self.check_if_thread_exists(tr_id)

            if thread_id is None:
                logging.info(f"Creating new thread for {name} with tr_id {tr_id}")
                thread = self.client.beta.threads.create()
                thread_id = thread.id
                self.store_thread(tr_id, thread_id)

            # Send the user's message to the OpenAI service
            self.client.beta.threads.messages.create(
                thread_id=thread_id,
                role="user",
                content=message_body,
            )

            # Retrieve the assistant's response
            new_message = self.run_assistant(thread_id)
            logging.info(f"To {name}: {new_message}")
            return new_message
        except Exception as e:
            logging.error(f"Error generating response: {e}")
            return "I'm sorry, I couldn't process your request."

    def is_assistants_response(self, message):
        """
        Determines if the given message is from the assistant.
        """
        return message.role == 'assistant'

    def run_assistant(self, thread_id):
    # Runs the assistant on the given thread and returns the response.
        try:
            # Retrieve the default assistant (this can be customized as needed)
            assistant = self.client.beta.assistants.retrieve("asst_CniDQMo1heSOzvzRNHAMp07D")

            # Start the assistant's run on the thread
            run = self.client.beta.threads.runs.create(
                thread_id=thread_id,
                assistant_id=assistant.id,
            )

            
            
            # Wait for the run to complete
            while run.status != "completed":
                time.sleep(1)
                run = self.client.beta.threads.runs.retrieve(thread_id=thread_id, run_id=run.id)
            
            messages = self.client.beta.threads.messages.list(thread_id=thread_id)

            # Initialize variables to find the most recent assistant's response
            latest_response_time = 0
            latest_response = None

            # Loop through the messages to find the latest assistant's response
            for message in messages.data:
                if self.is_assistants_response(message):
                    # Convert the created_at timestamp to a number for comparison
                    message_time = int(message.created_at)
                    if message_time > latest_response_time:
                        latest_response_time = message_time
                        latest_response = message.content[0].text.value

            if latest_response:
                logging.info(f"Assistant's latest response: {latest_response}")
                return latest_response
            else:
                logging.error("No assistant response found in the thread.")
                return "No response received from the assistant."
        except Exception as e:
            logging.error(f"Error running assistant: {e}")
            return "I'm sorry, I couldn't complete the conversation."

