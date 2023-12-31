openai_service.py: This file contains the JarvisAssistant class, which interacts with the OpenAI API to create an assistant and generate responses based on user queries. It handles the creation of threads, storage of conversation history, and communication with the OpenAI service.

speech_handler.py: This file is responsible for handling speech recognition and text-to-speech functionalities. It uses the speech_recognition library to convert spoken words into text and pyttsx3 for converting text back into spoken words. It defines functions for recording and recognizing audio from the microphone and for speaking text out loud.

project.py: This is the main script of your project, which integrates all the functionalities. It imports and utilizes functions from speech_handler.py and JarvisAssistant from openai_service.py to interact with the user. It defines functions for getting the user's name, greeting the user, capturing user input, generating responses, and the main loop that orchestrates the conversation flow.

test_project.py: This file contains the tests for your project. It uses pytest and unittest.mock to test the functionalities defined in project.py. It includes tests for greeting the user, handling the exit command, generating responses, getting the user's name, and capturing user input. It ensures that your program behaves as expected and that each function performs its intended task correctly.

These four files together create a cohesive backend system named JARVIS, capable of understanding spoken input, processing it intelligently, and responding audibly to the user.

# JARVIS - Your Personal AI Assistant

JARVIS (Just A Rather Very Intelligent System) is your personal AI assistant, inspired by the iconic digital helper from the Iron Man MCU. It's designed to understand your spoken commands, process them intelligently, and respond in a human-like manner.

## Features

- **Voice Interaction**: Communicate with JARVIS using natural language. JARVIS listens to your queries and responds verbally.
- **OpenAI Integration**: Leverages the power of OpenAI's GPT models to provide informative and contextually relevant responses.
- **Customizable Responses**: Tailored responses based on user input and previous interactions.
- **Continuous Conversation**: Maintains context over a session for a natural and fluid conversation experience.

## Components

- `openai_service.py`: Manages interactions with the OpenAI API.
- `speech_handler.py`: Handles speech recognition and text-to-speech conversion.
- `project.py`: The main script that integrates all components and runs the assistant.
- `test_project.py`: Contains tests to ensure the reliability and correctness of the system.

## Setup

1. **Clone the Repository**: Clone this repository to your local machine.
    ```
    git clone https://github.com/your-username/JARVIS.git
    ```
2. **Install Dependencies**: Navigate to the cloned directory and install the required Python packages.
    ```
    pip install -r requirements.txt
    ```
3. **Environment Variables**: Set up the necessary environment variables or `.env` file with your OpenAI API key.

## Usage

To start JARVIS, run the `project.py` script:

python project.py

Speak to JARVIS as you would to a person. You can ask questions, request information, or just chat. To end the session, simply say "exit". But remember you need to set the .env file with you own OPENAI_API_KEY , for tests on gpt-4-turbo in my realease 1 test with no more then 100 words is closer then 0,01$
Read the requirements.txt to see if you have all the needed

## Testing

Run the tests to ensure JARVIS is functioning correctly:


## Customization

You can customize JARVIS's behavior and responses by modifying the `openai_service.py` script. Change the model, adjust the settings, or even provide specific instructions for different types of interactions.

## Contributions

Contributions are welcome! If you have ideas for new features, improvements, or bug fixes, feel free to submit a pull request or open an issue.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

- Inspired by the JARVIS system from the Iron Man series.
- Powered by OpenAI's GPT models.
- Thanks to all the contributors who spend time improving this project.

Enjoy your personal AI assistant, JARVIS created by Rafael Parish!
