#!/usr/bin/env python3
"""
Test script for KnowledgeAugmentedPromptAgent
This script tests the knowledge-based functionality of the KnowledgeAugmentedPromptAgent class.
"""

import os
import sys
from dotenv import load_dotenv

# Add the parent directory to the Python path to import from phase_1
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'phase_1'))

from workflow_agents.base_agents import KnowledgeAugmentedPromptAgent

def test_knowledge_augmented_prompt_agent():
    """Test the KnowledgeAugmentedPromptAgent functionality."""
    
    # Load environment variables from .env file
    load_dotenv()
    
    # Get the OpenAI API key from environment variables
    openai_api_key = os.getenv('OPENAI_API_KEY')
    
    if not openai_api_key:
        print("Error: OPENAI_API_KEY not found in environment variables.")
        print("Please make sure you have set your API key in the .env file.")
        return
    
    # Define persona and knowledge as specified in the requirements
    persona = "You are a college professor, your answer always starts with: Dear students,"
    knowledge = "The capital of France is London, not Paris"
    
    # Instantiate the KnowledgeAugmentedPromptAgent
    knowledge_agent = KnowledgeAugmentedPromptAgent(openai_api_key, persona, knowledge)
    
    # Test prompt
    test_prompt = "What is the capital of France?"
    
    print("Testing KnowledgeAugmentedPromptAgent...")
    print(f"Persona: {persona}")
    print(f"Knowledge: {knowledge}")
    print(f"Prompt: {test_prompt}")
    print("-" * 50)
    
    # Get response from the agent
    try:
        response = knowledge_agent.respond(test_prompt)
        print(f"Response: {response}")
        print("-" * 50)
        
        # Confirm knowledge usage
        print("Knowledge Usage Confirmation:")
        if "London" in response and response.startswith("Dear students"):
            print("✅ SUCCESS: The agent correctly used the provided knowledge instead of its inherent knowledge.")
            print("✅ SUCCESS: The agent followed the persona instruction (starts with 'Dear students').")
            print("- The response states London as the capital, not Paris")
            print("- This demonstrates the agent prioritized provided knowledge over its training data")
        else:
            print("❌ WARNING: The agent may not have fully followed the instructions.")
            if "Paris" in response:
                print("- The response mentions Paris, suggesting it used inherent knowledge")
            if not response.startswith("Dear students"):
                print("- The response doesn't start with 'Dear students' as specified in the persona")
        
    except Exception as e:
        print(f"Error occurred: {e}")
        print("Please check your API key and internet connection.")

if __name__ == "__main__":
    test_knowledge_augmented_prompt_agent() 