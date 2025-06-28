from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv
import os
import sys

load_dotenv()

@tool
def calculator(a: float, b: float) -> str:
    """Useful for performing basic arithmeric calculations with numbers"""
    print("Tool has been called.")
    return f"The sum of {a} and {b} is {a + b}"
    
@tool
def say_hello(name: str) -> str:
    """Useful for greeting a user"""
    print("Tool has been called.")
    return f"Hello {name}, I hope you are well today"

def create_model():
    """Create a model with fallback options"""
    # Try OpenAI first
    openai_key = os.getenv("OPENAI_API_KEY")
    if openai_key and openai_key != "your_openai_api_key_here":
        try:
            return ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
        except Exception as e:
            print(f"OpenAI model failed: {e}")
    
    # Try Mistral AI as second option
    try:
        from langchain_mistralai import ChatMistralAI
        mistral_key = os.getenv("MISTRAL_API_KEY")
        if mistral_key and mistral_key != "your_mistral_api_key_here":
            return ChatMistralAI(model="mistral-large-latest", temperature=0)
    except ImportError:
        print("Mistral AI package not installed. Install with: uv add langchain-mistralai")
    except Exception as e:
        print(f"Mistral AI model failed: {e}")
    
    # Try Google AI as fallback
    try:
        from langchain_google_genai import ChatGoogleGenerativeAI
        google_key = os.getenv("GOOGLE_API_KEY")
        if google_key and google_key != "your_google_api_key_here":
            return ChatGoogleGenerativeAI(model="gemini-1.5-pro", temperature=0)
    except ImportError:
        print("Google AI package not installed. Install with: uv add langchain-google-genai")
    except Exception as e:
        print(f"Google AI model failed: {e}")
    
    # If all else fails, provide instructions
    print("\n" + "="*60)
    print("API KEYS NOT CONFIGURED")
    print("="*60)
    print("To use this AI assistant, you need to set up API keys:")
    print("\n1. Create a .env file in this directory")
    print("2. Add your API keys:")
    print("   OPENAI_API_KEY=your_actual_openai_key")
    print("   MISTRAL_API_KEY=your_actual_mistral_key")
    print("   GOOGLE_API_KEY=your_actual_google_key")
    print("\n3. Get API keys from:")
    print("   - OpenAI: https://platform.openai.com/api-keys")
    print("   - Mistral AI: https://console.mistral.ai/api-keys/")
    print("   - Google AI: https://makersuite.google.com/app/apikey")
    print("\n4. For quota issues, check your billing at:")
    print("   - OpenAI: https://platform.openai.com/account/billing")
    print("   - Mistral AI: https://console.mistral.ai/billing")
    print("="*60)
    
    return None

def simple_chat_mode():
    """Simple chat mode when no API is available"""
    print("\nSimple Chat Mode (No AI)")
    print("I can only use the available tools:")
    print("- calculator(a, b): Add two numbers")
    print("- say_hello(name): Greet someone")
    print("\nType 'quit' to exit.")
    
    while True:
        user_input = input("\nYou: ").strip()
        
        if user_input.lower() == "quit":
            break
        
        # Simple keyword-based responses
        if "calculator" in user_input.lower() or "add" in user_input.lower() or "sum" in user_input.lower() or "+" in user_input:
            try:
                # Try to extract numbers from input - improved regex
                import re
                # Look for numbers in various formats
                numbers = re.findall(r'\d+\.?\d*', user_input)
                if len(numbers) >= 2:
                    a, b = float(numbers[0]), float(numbers[1])
                    result = calculator(a, b)
                    print(f"Assistant: {result}")
                else:
                    print("Assistant: Please provide two numbers to add. Example: 'add 5 and 3' or '5 + 3'")
            except:
                print("Assistant: I couldn't understand the numbers. Please try: 'add 5 and 3' or '5 + 3'")
        
        elif "hello" in user_input.lower() or "greet" in user_input.lower():
            # Try to extract a name
            import re
            name_match = re.search(r'hello\s+(\w+)', user_input.lower())
            if name_match:
                name = name_match.group(1)
                result = say_hello(name)
                print(f"Assistant: {result}")
            else:
                result = say_hello("there")
                print(f"Assistant: {result}")
        
        else:
            print("Assistant: I can help with calculations (try 'add 5 and 3') or greetings (try 'hello John').")

def main():
    model = create_model()
    
    if model is None:
        simple_chat_mode()
        return
    
    tools = [calculator, say_hello]
    agent_executor = create_react_agent(model, tools)
    
    print("Welcome! I'm your AI assistant. Type 'quit' to exit.")
    print("You can ask me to perform calculations or chat with me.")
    
    while True:
        user_input = input("\nYou: ").strip()
        
        if user_input == "quit":
            break
        
        print("\nAssistant: ", end="")
        try:
            for chunk in agent_executor.stream(
                {"messages": [HumanMessage(content=user_input)]}
            ):
                if "agent" in chunk and "messages" in chunk["agent"]:
                    for message in chunk["agent"]["messages"]:
                        print(message.content, end="")
            print()
        except Exception as e:
            print(f"\nError: {e}")
            print("Switching to simple mode...")
            simple_chat_mode()
            break
        
if __name__ == "__main__":
    main()
                