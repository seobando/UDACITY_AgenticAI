#!/usr/bin/env python3
"""
Test script for DirectPromptAgent
This script tests the basic functionality of the DirectPromptAgent class.
"""

import os
import sys
from dotenv import load_dotenv

# Add the parent directory to the Python path to import from phase_1
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from phase_1.workflow_agents.base_agents import DirectPromptAgent


def test_direct_prompt_agent():
    """Test the DirectPromptAgent functionality."""
    
    # Load environment variables from .env file
    load_dotenv()
    
    # Get the OpenAI API key from environment variables
    openai_api_key = os.getenv('OPENAI_API_KEY')
    
    if not openai_api_key:
        print("Error: OPENAI_API_KEY not found in environment variables.")
        print("Please make sure you have set your API key in the .env file.")
        return
    
    # Instantiate the DirectPromptAgent
    direct_agent = DirectPromptAgent(openai_api_key)
    
    # Test prompt
    test_prompt = "What is the Capital of France?"
    
    print("Testing DirectPromptAgent...")
    print(f"Prompt: {test_prompt}")
    print("-" * 50)
    
    # Get response from the agent
    try:
        response = direct_agent.respond(test_prompt)
        print(f"Response: {response}")
        print("-" * 50)
        
        # Explain the knowledge source
        print("Knowledge Source:")
        print("The DirectPromptAgent uses general knowledge from the GPT-3.5-turbo model.")
        print("It does not have any additional context, memory, or specialized knowledge.")
        print("The response is based solely on the pre-trained knowledge embedded in the LLM.")
        
    except Exception as e:
        print(f"Error occurred: {e}")
        print("Please check your API key and internet connection.")

if __name__ == "__main__":
    test_direct_prompt_agent() 