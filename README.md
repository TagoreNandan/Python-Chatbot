<<<<<<< HEAD
# 3 Python AI Projects 🚀

A collection of three AI projects built with Python, LangChain, and modern AI providers.

## 📁 Project Structure

```
3 python ai projects/
├── project 1/              # 🤖 AI Assistant with Multi-Provider Support
│   ├── main.py            # Main AI assistant application
│   ├── pyproject.toml     # Dependencies configuration
│   ├── README.md          # Project-specific documentation
│   ├── test_simple.py     # Test utilities
│   └── env.example        # Environment variables template
├── project 2/              # 🎯 [Coming Soon] Your next AI project
├── project 3/              # 🎯 [Coming Soon] Your next AI project
├── run_ai_assistant.py    # 🚀 Easy launcher for AI assistant
├── run_ai.sh              # Shell script launcher
└── README.md              # This file
```

## 🚀 Quick Start

### Running the AI Assistant (Project 1)

**Option 1: Python Launcher (Recommended)**
```bash
python3 run_ai_assistant.py
```

**Option 2: Shell Script**
```bash
./run_ai.sh
```

**Option 3: Direct Command**
```bash
cd "project 1" && uv run main.py
```

## 🤖 AI Assistant Features

- **Multi-Provider Support**: OpenAI, Mistral AI, Google AI
- **Smart Fallback**: Works even without API keys
- **Built-in Tools**: Calculator and greeting functions
- **Error Handling**: Graceful handling of API issues
- **Easy Setup**: Simple environment configuration

## 🛠️ Setup

### Prerequisites
- Python 3.13+
- [uv](https://docs.astral.sh/uv/) package manager

### Installation
1. Clone this repository
2. Navigate to the project directory
3. Install dependencies:
   ```bash
   cd "project 1"
   uv sync
   ```

### Configuration
1. Copy the environment template:
   ```bash
   cp "project 1/env.example" "project 1/.env"
   ```
2. Add your API keys to `.env`:
   ```env
   OPENAI_API_KEY=your_openai_key_here
   MISTRAL_API_KEY=your_mistral_key_here
   GOOGLE_API_KEY=your_google_key_here
   ```

## 🔑 API Keys

Get your API keys from:
- **OpenAI**: https://platform.openai.com/api-keys
- **Mistral AI**: https://console.mistral.ai/api-keys/
- **Google AI**: https://makersuite.google.com/app/apikey

## 🎯 Project 1: AI Assistant

A sophisticated AI assistant that can:
- Answer questions using multiple AI providers
- Perform calculations
- Greet users
- Handle errors gracefully
- Work offline with basic tools

### Features
- **Multi-Provider AI**: Automatically tries OpenAI, Mistral AI, then Google AI
- **Fallback Mode**: Simple keyword-based responses when no API is available
- **Tool Integration**: Calculator and greeting functions
- **Error Recovery**: Graceful handling of quota limits and API errors

## 🔮 Future Projects

- **Project 2**: [Your next AI project idea]
- **Project 3**: [Your next AI project idea]

## 🛡️ Security

- `.env` files are automatically ignored by git
- API keys are never committed to the repository
- Environment templates show required variables without exposing secrets

## 📝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🤝 Support

If you encounter any issues:
1. Check the project-specific README files
2. Verify your API keys are correctly set
3. Ensure all dependencies are installed
4. Open an issue on GitHub

---

**Happy coding! 🎉** 
=======
# Python-Chatbot
>>>>>>> 6a62a5e841e4d03890f97c965ed0b93b12e6a2c3
