#!/usr/bin/env python3
"""
Launcher script for the AI Assistant
This script runs the AI assistant from the project 1 directory
"""

import os
import sys
import subprocess

def main():
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project1_dir = os.path.join(script_dir, "project 1")
    
    # Check if project 1 directory exists
    if not os.path.exists(project1_dir):
        print("Error: 'project 1' directory not found!")
        print(f"Expected location: {project1_dir}")
        sys.exit(1)
    
    # Check if main.py exists in project 1
    main_py_path = os.path.join(project1_dir, "main.py")
    if not os.path.exists(main_py_path):
        print("Error: main.py not found in 'project 1' directory!")
        sys.exit(1)
    
    print("🚀 Starting AI Assistant...")
    print(f"📁 Running from: {project1_dir}")
    print("=" * 50)
    
    try:
        # Change to project 1 directory and run the AI assistant
        os.chdir(project1_dir)
        subprocess.run(["uv", "run", "main.py"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running AI assistant: {e}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n👋 Goodbye!")
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 