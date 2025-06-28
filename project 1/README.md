# AI Assistant Project

A simple AI assistant built with LangChain and LangGraph that can perform calculations and chat with users.

## Features

- **Calculator Tool**: Add two numbers together
- **Greeting Tool**: Say hello to users
- **Fallback Mode**: Works even without API keys
- **Multiple AI Providers**: Supports OpenAI and Google AI

## Setup

### 1. Install Dependencies

```bash
uv sync
```

### 2. Set up API Keys (Optional)

Create a `.env` file in the project directory:

```env
# OpenAI API (Primary)
OPENAI_API_KEY=your_openai_api_key_here

# Google AI API (Fallback)
GOOGLE_API_KEY=your_google_api_key_here
```

### 3. Get API Keys

- **OpenAI**: Visit [OpenAI API Keys](https://platform.openai.com/api-keys)
- **Google AI**: Visit [Google AI Studio](https://makersuite.google.com/app/apikey)

## Usage

Run the assistant:

```bash
uv run main.py
```

### Modes

1. **Full AI Mode**: When API keys are configured
2. **Simple Mode**: When no API keys are available (still functional with basic tools)

## Troubleshooting

### OpenAI Quota Exceeded

If you see "insufficient_quota" error:

1. Check your billing at [OpenAI Billing](https://platform.openai.com/account/billing)
2. Add credits to your account
3. Or use Google AI as fallback

### Missing API Keys

The program will automatically switch to simple mode if no API keys are found.

### Google AI Setup Issues

If you get Google credentials errors:

1. Make sure you have the correct API key
2. The API key should be from Google AI Studio, not Google Cloud
3. No additional setup required - just the API key

## Example Usage

```
You: add 5 and 3
Assistant: The sum of 5 and 3 is 8

You: hello John
Assistant: Hello John, I hope you are well today

You: what is 10 + 20?
Assistant: The sum of 10 and 20 is 30
``` 