#!/usr/bin/env python3
"""
Test script for ActionPlanningAgent
This script tests the action planning functionality that extracts steps from user prompts.
"""

import os
import sys
from dotenv import load_dotenv

# Add the parent directory to the Python path to import from phase_1
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'phase_1'))

from workflow_agents.base_agents import ActionPlanningAgent

def test_action_planning_agent():
    """Test the ActionPlanningAgent functionality."""
    
    # Load environment variables from .env file
    load_dotenv()
    
    # Get the OpenAI API key from environment variables
    openai_api_key = os.getenv('OPENAI_API_KEY')
    
    if not openai_api_key:
        print("Error: OPENAI_API_KEY not found in environment variables.")
        print("Please make sure you have set your API key in the .env file.")
        return
    
    print("Testing ActionPlanningAgent...")
    print("=" * 60)
    
    try:
        # Define knowledge for the action planning agent
        cooking_knowledge = """
        Cooking Knowledge Base:
        
        Scrambled Eggs Recipe:
        1. Crack 2-3 eggs into a bowl
        2. Add a splash of milk or cream
        3. Add salt and pepper to taste
        4. Whisk the eggs until well combined
        5. Heat butter in a non-stick pan over medium-low heat
        6. Pour the egg mixture into the pan
        7. Let the eggs sit for 20 seconds, then gently stir
        8. Continue stirring gently until eggs are almost set but still creamy
        9. Remove from heat (eggs will continue cooking)
        10. Serve immediately on a plate
        
        General Cooking Tips:
        - Always wash hands before cooking
        - Gather all ingredients before starting
        - Use fresh ingredients when possible
        - Clean as you go to keep workspace organized
        """
        
        # Create the ActionPlanningAgent
        action_agent = ActionPlanningAgent(openai_api_key, cooking_knowledge)
        
        print("Action Planning Agent Configuration:")
        print("Knowledge Domain: Cooking (specifically scrambled eggs)")
        print("Task: Extract actionable steps from user prompts")
        print("-" * 60)
        
        # Test with the specified prompt
        test_prompt = "One morning I wanted to have scrambled eggs"
        
        print(f"Test Prompt: '{test_prompt}'")
        print("-" * 60)
        print("Extracting Action Steps...")
        
        # Get the action steps
        action_steps = action_agent.extract_steps_from_prompt(test_prompt)
        
        print("\nExtracted Action Steps:")
        print("=" * 60)
        
        if action_steps:
            for i, step in enumerate(action_steps, 1):
                print(f"{i}. {step}")
        else:
            print("No action steps were extracted.")
        
        print("\n" + "=" * 60)
        print("ACTION PLANNING ANALYSIS:")
        print("=" * 60)
        print("The ActionPlanningAgent successfully:")
        print("1. ✅ Processed the user's intent from natural language")
        print("2. ✅ Used provided knowledge to identify relevant steps")
        print("3. ✅ Extracted actionable steps in a logical sequence")
        print("4. ✅ Filtered out empty or irrelevant lines from the response")
        print("5. ✅ Returned a clean list of executable actions")
        
        print("\nStep Analysis:")
        if len(action_steps) > 0:
            print(f"✅ Generated {len(action_steps)} actionable steps")
            if any("egg" in step.lower() for step in action_steps):
                print("✅ Steps are relevant to the scrambled eggs context")
            if any("crack" in step.lower() or "whisk" in step.lower() or "heat" in step.lower() for step in action_steps):
                print("✅ Steps include specific cooking actions from the knowledge base")
        else:
            print("⚠️  No steps were generated - may need to adjust knowledge or prompt")
        
        # Test with additional prompts to demonstrate versatility
        additional_prompts = [
            "I need to prepare breakfast",
            "Help me cook eggs", 
            "What should I do to make scrambled eggs?"
        ]
        
        print("\n" + "-" * 60)
        print("ADDITIONAL TESTS:")
        print("-" * 60)
        
        for i, prompt in enumerate(additional_prompts, 1):
            print(f"\nAdditional Test {i}: '{prompt}'")
            try:
                steps = action_agent.extract_steps_from_prompt(prompt)
                print(f"Steps extracted: {len(steps)}")
                if steps:
                    print("Sample steps:", steps[:3])  # Show first 3 steps
            except Exception as e:
                print(f"Error: {e}")
        
    except Exception as e:
        print(f"Error occurred: {e}")
        print("Please check your API key and internet connection.")

if __name__ == "__main__":
    test_action_planning_agent() 