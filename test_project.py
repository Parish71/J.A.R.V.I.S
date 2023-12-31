# test_project.py
import pytest
from unittest.mock import patch
import project

@patch('project.speak_text')
def test_greet_user(mock_speak):
    project.greet_user("Doe")
    expected_greeting = 'Hello Sr.Doe, how can I assist you today?'
    mock_speak.assert_called_with(expected_greeting)

@patch('project.speak_text')
def test_exit_jarvis(mock_speak):
    user_name = "Doe"
    expected_farewell = f"Goodbye {user_name}! Have a great day!"
    assert project.exit_jarvis(user_name) == expected_farewell
    mock_speak.assert_called_with(expected_farewell)

@patch('project.JarvisAssistant')
@patch('project.speak_text')
def test_generate_response(mock_speak, mock_jarvis):
    mock_jarvis_instance = mock_jarvis.return_value
    mock_jarvis_instance.generate_response.return_value = "2 + 2 is 4"
    user_input = "how much is 2 + 2"
    user_name = "Doe"
    expected_response = "2 + 2 is 4"

    assert project.generate_response(user_input, user_name) == expected_response
    mock_jarvis_instance.generate_response.assert_called_with(user_input, user_name, "User")
    mock_speak.assert_not_called()  # generate_response should not directly call speak_text

@patch('project.record_and_recognize_audio')
def test_get_user_name(mock_record):
    mock_record.return_value = "Doe"
    assert project.get_user_name() == "Doe"

@patch('project.record_and_recognize_audio')
def test_get_user_input(mock_record):
    user_name = "Doe"
    mock_record.return_value = "What's the weather?"
    assert project.get_user_input(user_name) == "What's the weather?"

def test_AssertionError():
    with pytest.raises(AssertionError):
        raise AssertionError("This is a test for AssertionError")
