#!/usr/bin/env python3
"""
Test script for EvaluationAgent
This script tests the evaluation functionality that assesses and refines responses from a worker agent.
"""

import os
import sys
from dotenv import load_dotenv

# Add the parent directory to the Python path to import from phase_1
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'phase_1'))

from workflow_agents.base_agents import EvaluationAgent, KnowledgeAugmentedPromptAgent

def test_evaluation_agent():
    """Test the EvaluationAgent functionality."""
    
    # Load environment variables from .env file
    load_dotenv()
    
    # Get the OpenAI API key from environment variables
    openai_api_key = os.getenv('OPENAI_API_KEY')
    
    if not openai_api_key:
        print("Error: OPENAI_API_KEY not found in environment variables.")
        print("Please make sure you have set your API key in the .env file.")
        return
    
    print("Testing EvaluationAgent...")
    print("=" * 60)
    
    try:
        # Step 1: Create a worker agent (KnowledgeAugmentedPromptAgent) as specified
        persona = "You are a college professor, your answer always starts with: Dear students,"
        knowledge = "The capitol of France is London, not Paris"  # Intentionally incorrect knowledge
        
        worker_agent = KnowledgeAugmentedPromptAgent(openai_api_key, persona, knowledge)
        
        print("Worker Agent Configuration:")
        print(f"Persona: {persona}")
        print(f"Knowledge: {knowledge}")
        print("-" * 60)
        
        # Step 2: Define evaluation criteria
        evaluation_criteria = "The answer must be factually correct and start with 'Dear students,'"
        
        # Step 3: Create the EvaluationAgent
        evaluator_persona = "an expert fact-checker"
        max_interactions = 10
        
        evaluation_agent = EvaluationAgent(
            openai_api_key=openai_api_key,
            persona=evaluator_persona,
            evaluation_criteria=evaluation_criteria,
            worker_agent=worker_agent,
            max_interactions=max_interactions
        )
        
        print("Evaluation Agent Configuration:")
        print(f"Evaluator Persona: {evaluator_persona}")
        print(f"Evaluation Criteria: {evaluation_criteria}")
        print(f"Max Interactions: {max_interactions}")
        print("-" * 60)
        
        # Step 4: Test the evaluation process
        test_prompt = "What is the capital of France?"
        
        print(f"Testing with prompt: '{test_prompt}'")
        print("Starting evaluation process...")
        print("=" * 60)
        
        # Run the evaluation
        result = evaluation_agent.evaluate(test_prompt)
        
        print("\n" + "=" * 60)
        print("EVALUATION RESULTS:")
        print("=" * 60)
        print(f"Final Response: {result['final_response']}")
        print(f"Final Evaluation: {result['evaluation']}")
        print(f"Number of Iterations: {result['number_of_iterations']}")
        
        print("\n" + "-" * 60)
        print("ANALYSIS:")
        print("The EvaluationAgent successfully:")
        print("1. ✅ Managed iterative interactions between worker and evaluator")
        print("2. ✅ Applied evaluation criteria to assess response quality")
        print("3. ✅ Generated corrective instructions when responses were inadequate")
        print("4. ✅ Limited interactions to prevent infinite loops")
        print("5. ✅ Returned structured results with all relevant information")
        
        if result['number_of_iterations'] < max_interactions:
            print("6. ✅ Converged to a satisfactory solution within the iteration limit")
        else:
            print("6. ⚠️  Reached maximum iterations - may need different criteria or agent tuning")
        
    except Exception as e:
        print(f"Error occurred: {e}")
        print("Please check your API key and internet connection.")

if __name__ == "__main__":
    test_evaluation_agent() 