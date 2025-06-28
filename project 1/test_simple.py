#!/usr/bin/env python3
"""
Simple test script to verify the calculator functionality
"""

import re

def test_calculator():
    """Test the number extraction logic"""
    
    test_cases = [
        "add 5 and 3",
        "5 + 3", 
        "what is 10 plus 20",
        "calculate 15 and 25",
        "sum of 7 and 9",
        "hello world",  # should not match
        "just text",    # should not match
    ]
    
    print("Testing number extraction:")
    print("=" * 40)
    
    for test_input in test_cases:
        print(f"\nInput: '{test_input}'")
        
        # Check if it should trigger calculator
        if ("calculator" in test_input.lower() or 
            "add" in test_input.lower() or 
            "sum" in test_input.lower() or 
            "+" in test_input or
            "plus" in test_input.lower() or
            "calculate" in test_input.lower()):
            
            # Extract numbers
            numbers = re.findall(r'\d+\.?\d*', test_input)
            if len(numbers) >= 2:
                a, b = float(numbers[0]), float(numbers[1])
                result = f"The sum of {a} and {b} is {a + b}"
                print(f"✅ Found numbers: {numbers}")
                print(f"✅ Result: {result}")
            else:
                print(f"❌ No numbers found or not enough numbers")
        else:
            print(f"⏭️  Not a calculator request")

if __name__ == "__main__":
    test_calculator() 