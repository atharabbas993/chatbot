# ChatBot

ChatBot is a simple chatbot application built using Python and Tkinter. It provides predefined responses to specific user inputs. The GUI is designed using Tkinter and the chatbot is integrated with predefined responses for common questions.

## Features

- Simple and easy-to-use interface
- Predefined responses to common questions
- Scrollable chat window
- Clear chat functionality
- Responds to 'Enter' key for sending messages

## Getting Started

These instructions will help you set up and run the ChatBot on your local machine.

### Prerequisites

- Python 3.x
- Tkinter library (usually included with Python installations)
- Pillow library for image handling

### Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/your-username/chatbot.git
    cd chatbot
    ```

2. **Install required libraries:**

    Ensure you have `Pillow` installed. If not, you can install it using pip:

    ```sh
    pip install Pillow
    ```

### Running the Application

1. **Navigate to the project directory:**

    ```sh
    cd chatbot
    ```

2. **Run the application:**

    ```sh
    python chatbot.py
    ```

    This will launch the ChatBot application.

### Usage

- Type a message into the input field and press "Send>>" or hit "Enter" to send the message.
- The bot will respond based on predefined responses stored in the application.
- Click on "Clear Data" to clear the chat history.

### Predefined Responses

The chatbot currently supports the following predefined responses:

| User Input                         | Bot Response                                               |
|------------------------------------|------------------------------------------------------------|
| Hi                                 | Hello                                                      |
| How are you?                       | Fine and you?                                              |
| What is your name?                 | I am a ChatBot. How can I help you?                        |
| I'm fine                           | Nice to hear you are fine                                  |
| Who created you?                   | I was created by Mr. Athar Abbas                           |
| What do you do?                    | I am a chatbot designed to help answer your questions and provide information. |
| How can I contact you?             | You can contact Athar Abbas at atharabbas993@gmail.com     |
| What are your working hours?       | I am available 24/7 to assist you.                         |
| What languages can you speak?      | I understand only English for communication.               |
| Do you have any hobbies?           | As a chatbot, I don't have hobbies, but I can help you find hobbies and activities that you might enjoy! |

If the user input does not match any predefined response, the bot will respond with "Sorry, I did not get it".

### Customization

To customize the responses, you can modify the `self.responses` dictionary in the `ChatBot` class.

```python
self.responses = {
    "Hi": "Hello",
    "How are you?": "Fine and you?",
    "What is your name?": "I am a ChatBot. How can I help you?",
    "I'm fine": "Nice to hear you are fine",
    "Who created you?": "I was created by Mr. Athar Abbas",
    "What do you do?": "I am a chatbot designed to help answer your questions and provide information.",
    "How can I contact you?": "You can contact Athar Abbas at atharabbas993@gmail.com",
    "What are your working hours?": "I am available 24/7 to assist you.",
    "What languages can you speak?": "I understand only English for communication.",
    "Do you have any hobbies?": "As a chatbot, I don't have hobbies, but I can help you find hobbies and activities that you might enjoy!"
}
