import google.generativeai as genai
import pyttsx3
import speech_recognition as sr
from gtts import gTTS
import pygame
from time import sleep
import os

# Directly setting the API key
api_key = "use your api key here"

# Configuring the Generative AI client
genai.configure(api_key=api_key)

# Initialize the Generative Model with 'gemini-1.5-flash'
model = genai.GenerativeModel('gemini-1.5-flash')

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    try:
        tts = gTTS(text)
        tts.save('temp.mp3')

        # Initialize the mixer module
        pygame.mixer.init()

        # Load the MP3 file
        pygame.mixer.music.load('temp.mp3')

        # Play the MP3 file
        pygame.mixer.music.play()

        # Keep the program running to allow the music to play
        while pygame.mixer.music.get_busy():
            sleep(1)

        # Unload the MP3 file
        pygame.mixer.music.unload()
        os.remove('temp.mp3')

    except Exception as e:
        print(f"An error occurred: {e}")

# List to store chat history
chat_history = []

while True:
    # Prompting the user for input
    user_input = input("You have any question: ")

    # Store user input in chat history
    chat_history.append(f"User: {user_input}")

    # Generate context for the model by concatenating the chat history
    context = "\n".join(chat_history)
    
    # Generating content based on user input with context
    response = model.generate_content(f"{context}\nAI: {user_input}")
    
    # Print response text, replacing or stripping markdown characters if necessary
    output_text = response.text
    # Optionally strip unwanted characters or formatting
    output_text = output_text.replace('*', '')  # Remove asterisks
    output_text = output_text.replace('_', '')  # Remove underscores, if needed

    # Store AI response in chat history
    chat_history.append(f"AI: {output_text}")

    print("Speaking:", output_text) 
    speak(output_text)

    # Optional: Print chat history to see the accumulated conversation
    print("\nChat History:")
    for entry in chat_history:
        print(entry)
