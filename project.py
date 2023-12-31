# project.py

print("Importing speech_handler.py")
from speech_handler import record_and_recognize_audio, speak_text
print("Importing openai_service.py")
from openai_service import JarvisAssistant

def get_user_name():
    """
    Asks the user for their name and returns it.
    """
    speak_text("Hello, I am JARVIS, your personal assistant. Tell me your last name no more words?")
    print("Listening for user's name...")
    return record_and_recognize_audio()

def greet_user(user_name):
    """
    Greets the user by name.
    """
    greeting = f"Hello Sr.{user_name}, how can I assist you today?"
    speak_text(greeting)
    return greeting

def get_user_input(user_name):
    """
    Listens for and returns the user's input.
    """
    print(f"Listening for {user_name}...")
    return record_and_recognize_audio()

def generate_response(user_input, user_name):
    """
    Generates a response from the OpenAI service based on user input.
    """
    jarvis = JarvisAssistant()  # Initialize the JarvisAssistant
    response = jarvis.generate_response(user_input, user_name, "User")
    print(f"JARVIS responded: {response}")
    return response

def exit_jarvis(user_name):
    """
    Handles the exit process for the user.
    """
    farewell_message = f"Goodbye {user_name}! Have a great day!"
    speak_text(farewell_message)
    return farewell_message

def main():
    user_name = get_user_name()  # Get the user's name
    greet_user(user_name)  # Greet the user

    while True:
        user_input = get_user_input(user_name)  # Get user input

        if user_input.lower() == "exit":  # Implement a way to exit the loop
            print(exit_jarvis(user_name))
            break

        # Generate a response and speak it out
        response = generate_response(user_input, user_name)
        speak_text(response)

if __name__ == "__main__":
    main()
