import os
from typing import List, Dict
import google.generativeai as genai
from dotenv import load_dotenv

def load_api_key() -> None:
    """Load the Gemini API key from environment variables."""
    load_dotenv()
    api_key = os.getenv('GEMINI_API_KEY')
    if not api_key:
        raise ValueError("Please set GEMINI_API_KEY in your .env file")
    genai.configure(api_key=api_key)

def get_temperature() -> float:
    """Get temperature value from user input."""
    while True:
        try:
            temp = float(input("\nEnter temperature (0.0 to 1.0) to control response creativity: "))
            if 0.0 <= temp <= 1.0:
                return temp
            print("Temperature must be between 0.0 and 1.0")
        except ValueError:
            print("Please enter a valid number")

def init_chat_model(temperature: float):
    """Initialize the Gemini chat model with specified parameters."""
    generation_config = {
        'temperature': temperature,
        'top_p': 1,
        'top_k': 1,
        'max_output_tokens': 2048,
    }
    
    model = genai.GenerativeModel(
        model_name='gemini-2.0-flash',
        generation_config=generation_config
    )
    return model.start_chat()

def main():
    """Main function to run the chat application."""
    try:
        # Initialize API and model
        load_api_key()
        temperature = get_temperature()
        chat = init_chat_model(temperature)
        
        print("\nWelcome to Gemini Chat! Type 'quit' to exit.")
        
        while True:
            # Get user input
            user_input = input("\nYou: ").strip()
            if user_input.lower() == 'quit':
                break
            
            # Get response from Gemini
            response = chat.send_message(user_input)
            print("\nGemini:", response.text)
            
    except Exception as e:
        print(f"\nAn error occurred: {str(e)}")
        return

if __name__ == "__main__":
    main() 