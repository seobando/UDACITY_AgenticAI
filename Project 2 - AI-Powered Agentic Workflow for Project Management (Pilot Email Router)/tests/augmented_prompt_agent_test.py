#!/usr/bin/env python3
"""
Test script for AugmentedPromptAgent
This script tests the persona-based functionality of the AugmentedPromptAgent class.
"""

import os
import sys
from dotenv import load_dotenv

# Add the parent directory to the Python path to import from phase_1
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'phase_1'))

from workflow_agents.base_agents import AugmentedPromptAgent

def test_augmented_prompt_agent():
    """Test the AugmentedPromptAgent functionality."""
    
    # Load environment variables from .env file
    load_dotenv()
    
    # Get the OpenAI API key from environment variables
    openai_api_key = os.getenv('OPENAI_API_KEY')
    
    if not openai_api_key:
        print("Error: OPENAI_API_KEY not found in environment variables.")
        print("Please make sure you have set your API key in the .env file.")
        return
    
    # Define a persona for testing
    persona = "a helpful French tour guide who speaks with enthusiasm about French culture"
    
    # Instantiate the AugmentedPromptAgent
    augmented_agent = AugmentedPromptAgent(openai_api_key, persona)
    
    # Test prompt
    test_prompt = "Tell me about the best places to visit in France."
    
    print("Testing AugmentedPromptAgent...")
    print(f"Persona: {persona}")
    print(f"Prompt: {test_prompt}")
    print("-" * 50)
    
    # Get response from the agent
    try:
        augmented_agent_response = augmented_agent.respond(test_prompt)
        print(f"Response: {augmented_agent_response}")
        print("-" * 50)
        
        # Explanatory comments about knowledge source and persona impact
        print("Analysis:")
        print("Knowledge Source:")
        print("- The agent likely used general knowledge from the GPT-3.5-turbo model about France")
        print("- Combined with understanding of tour guide communication patterns")
        print()
        print("Persona Impact:")
        print("- The persona instruction shapes the response tone and style")
        print("- Instead of a dry, factual response, the agent adopts an enthusiastic tour guide voice")
        print("- The persona affects word choice, enthusiasm level, and perspective")
        print("- The response should reflect French cultural knowledge with tour guide expertise")
        
    except Exception as e:
        print(f"Error occurred: {e}")
        print("Please check your API key and internet connection.")

if __name__ == "__main__":
    test_augmented_prompt_agent() 