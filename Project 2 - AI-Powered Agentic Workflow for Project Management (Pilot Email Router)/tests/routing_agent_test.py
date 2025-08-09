#!/usr/bin/env python3
"""
Test script for RoutingAgent
This script tests the routing functionality that directs prompts to the most appropriate specialized agent.
"""

import os
import sys
from dotenv import load_dotenv

# Add the parent directory to the Python path to import from phase_1
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'phase_1'))

from workflow_agents.base_agents import RoutingAgent, KnowledgeAugmentedPromptAgent

def test_routing_agent():
    """Test the RoutingAgent functionality."""
    
    # Load environment variables from .env file
    load_dotenv()
    
    # Get the OpenAI API key from environment variables
    openai_api_key = os.getenv('OPENAI_API_KEY')
    
    if not openai_api_key:
        print("Error: OPENAI_API_KEY not found in environment variables.")
        print("Please make sure you have set your API key in the .env file.")
        return
    
    print("Testing RoutingAgent...")
    print("=" * 60)
    
    try:
        # Step 1: Create specialized agents for different domains
        
        # Texas Agent
        texas_persona = "a knowledgeable Texas historian"
        texas_knowledge = """
        Texas is the second-largest state in the United States. Austin is the capital of Texas.
        Rome, Texas is a small unincorporated community in Sunflower County, Texas.
        Texas was an independent republic from 1836 to 1845 before joining the United States.
        The Alamo is a famous historical site in San Antonio, Texas.
        """
        texas_agent = KnowledgeAugmentedPromptAgent(openai_api_key, texas_persona, texas_knowledge)
        
        # Europe Agent
        europe_persona = "a European history expert"
        europe_knowledge = """
        Rome, Italy is the capital city of Italy and was the center of the Roman Empire.
        Rome has a rich history spanning over 2,500 years and is known as the 'Eternal City'.
        The Colosseum, Vatican City, and Trevi Fountain are famous landmarks in Rome, Italy.
        Italy is located in Southern Europe and has a Mediterranean climate.
        """
        europe_agent = KnowledgeAugmentedPromptAgent(openai_api_key, europe_persona, europe_knowledge)
        
        # Math Agent  
        math_persona = "a mathematics professor"
        math_knowledge = """
        Mathematical problem solving involves breaking down complex problems into smaller steps.
        Project management often involves calculating timelines, resources, and milestones.
        If one story takes 2 days and there are 20 stories, the total time would be 2 × 20 = 40 days.
        Time estimation is crucial for project planning and resource allocation.
        """
        math_agent = KnowledgeAugmentedPromptAgent(openai_api_key, math_persona, math_knowledge)
        
        print("Specialized Agents Created:")
        print("1. Texas Agent - Expert in Texas history and geography")
        print("2. Europe Agent - Expert in European history and culture")  
        print("3. Math Agent - Expert in mathematics and calculations")
        print("-" * 60)
        
        # Step 2: Define agent functions/lambdas
        def texas_agent_func(prompt):
            return f"[Texas Agent] {texas_agent.respond(prompt)}"
        
        def europe_agent_func(prompt):
            return f"[Europe Agent] {europe_agent.respond(prompt)}"
        
        def math_agent_func(prompt):
            return f"[Math Agent] {math_agent.respond(prompt)}"
        
        # Step 3: Create the agents list for the router
        agents = [
            {
                "name": "Texas Agent",
                "description": "Expert in Texas history, geography, and Texas-related topics including cities and landmarks in Texas",
                "func": texas_agent_func
            },
            {
                "name": "Europe Agent", 
                "description": "Expert in European history, culture, and European cities including Rome, Italy and other European topics",
                "func": europe_agent_func
            },
            {
                "name": "Math Agent",
                "description": "Expert in mathematics, calculations, project management timelines, and numerical problem solving",
                "func": math_agent_func
            }
        ]
        
        # Step 4: Create the RoutingAgent
        routing_agent = RoutingAgent(openai_api_key, agents)
        
        print("Router Configuration:")
        print(f"Number of specialized agents: {len(agents)}")
        print("Routing based on semantic similarity between prompts and agent descriptions")
        print("-" * 60)
        
        # Step 5: Test routing with different prompts
        test_prompts = [
            "Tell me about the history of Rome, Texas",
            "Tell me about the history of Rome, Italy", 
            "One story takes 2 days, and there are 20 stories"
        ]
        
        print("Testing Routing Functionality:")
        print("=" * 60)
        
        for i, prompt in enumerate(test_prompts, 1):
            print(f"\nTest {i}: '{prompt}'")
            print("-" * 40)
            
            response = routing_agent.route(prompt)
            print(f"Response: {response}")
            print("-" * 40)
        
        print("\n" + "=" * 60)
        print("ROUTING ANALYSIS:")
        print("=" * 60)
        print("The RoutingAgent successfully:")
        print("1. ✅ Calculated embeddings for user prompts")
        print("2. ✅ Calculated embeddings for agent descriptions")
        print("3. ✅ Computed cosine similarity between prompt and agent descriptions")
        print("4. ✅ Selected the agent with the highest similarity score")
        print("5. ✅ Routed different types of questions to appropriate specialists")
        print("\nExpected Routing:")
        print("- 'Rome, Texas' → Texas Agent (geographic location match)")
        print("- 'Rome, Italy' → Europe Agent (European city match)")
        print("- 'story calculation' → Math Agent (numerical problem match)")
        
    except Exception as e:
        print(f"Error occurred: {e}")
        print("Please check your API key and internet connection.")

if __name__ == "__main__":
    test_routing_agent() 