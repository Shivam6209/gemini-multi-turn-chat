# Gemini Multi-Turn Chat

A simple console-based chatbot that uses Google's Gemini AI model to maintain context-aware conversations.

## Features

- Multi-turn conversation with context preservation
- Configurable model parameters (temperature)
- Console-based interface
- Environment-based API key management

## Setup

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a `.env` file in the root directory with your Gemini API key:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

## Usage

Run the chat application:
```bash
python chat.py
```

The application will:
1. Ask for your initial message
2. Allow you to set the temperature parameter (0.0 to 1.0)
3. Maintain conversation context across multiple turns
4. Display Gemini's responses after each turn

## Note

Make sure you have a valid Gemini API key from Google AI Studio (https://makersuite.google.com/app/apikey).