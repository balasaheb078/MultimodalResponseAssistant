# Multimodal Response Assistant

This project is a text-based assistant that generates responses using Google Generative AI and provides output in both text and voice formats. It leverages the Google Gemini API for content generation and uses `gTTS` and `pygame` for text-to-speech functionality.

## Features

- **Text Input**: Takes user input via the command line.
- **Generative AI**: Generates contextual responses using Google Gemini.
- **Voice Output**: Converts the generated text responses into voice using `gTTS` and plays them using `pygame`.
- **Chat History**: Maintains a history of the conversation for context.

## Dependencies

The following Python packages are required:

- `google-generativeai`: For interacting with the Google Generative AI API.
- `pyttsx3`: For text-to-speech conversion.
- `speech_recognition`: For speech recognition (if needed in future extensions).
- `gtts`: For converting text to speech.
- `pygame`: For audio playback.
- `os`, `time`: For file handling and timing operations.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/balasaheb078/MultimodalResponseAssistant.git
    cd MultimodalResponseAssistant
    ```


2. **Install the dependencies:**

    ```bash
    pip install google-generativeai pyttsx3 speech_recognition gtts pygame
    ```

3. **Run the script:**

    ```bash
    python MultimodalResponseAssistant.py
    ```

## Usage

1. **Run the script:**

    ```bash
    python MultimodalResponseAssistant.py
    ```

2. **Input your questions or commands when prompted:**

    ```plaintext
    You have any question: [Your Question]
    ```

3. **The assistant will respond both in text and voice format.**

## Limitations

- **Voice Response Latency**: The voice output process may be slower due to the time required to generate the text-to-speech file and play it using `pygame`. This could be noticeable, especially for longer responses.
  
- **API Key Handling**: The API key is currently hardcoded, which is not secure. It's recommended to use environment variables or a secure configuration method.

- **Chat History Growth**: Over time, the chat history might grow large, which could affect the performance. Consider managing or truncating old entries for long sessions.

## Note

- **API Key**: Replace the `api_key` variable in the script with your Google API key.
- **Dependencies**: Ensure all dependencies are correctly installed. If you encounter issues, verify the installation of each package.


