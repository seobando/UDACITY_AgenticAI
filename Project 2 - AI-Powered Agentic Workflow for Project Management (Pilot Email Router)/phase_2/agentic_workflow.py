# agentic_workflow.py

import sys
import os
from dotenv import load_dotenv

# Add the phase_1 directory to the Python path to import workflow_agents
phase_1_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'phase_1'))
sys.path.insert(0, phase_1_path)

# TODO: 1 - Import the following agents: ActionPlanningAgent, 
# KnowledgeAugmentedPromptAgent, EvaluationAgent, RoutingAgent from the 
# workflow_agents.base_agents module
from workflow_agents.base_agents import (
    ActionPlanningAgent, 
    KnowledgeAugmentedPromptAgent, 
    EvaluationAgent, 
    RoutingAgent
)

# TODO: 2 - Load the OpenAI key into a variable called openai_api_key
load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')

# load the product spec
# TODO: 3 - Load the product spec document Product-Spec-Email-Router.txt 
# into a variable called product_spec
product_spec_path = os.path.join(
    os.path.dirname(__file__), 
    'Product-Spec-Email-Router.txt'
)
with open(product_spec_path, 'r') as file:
    product_spec = file.read()

# Instantiate all the agents

# Action Planning Agent
knowledge_action_planning = (
    "Stories are defined from a product spec by identifying a "
    "persona, an action, and a desired outcome for each story. "
    "Each story represents a specific functionality of the product "
    "described in the specification. \n"
    "Features are defined by grouping related user stories. \n"
    "Tasks are defined for each story and represent the engineering "
    "work required to develop the product. \n"
    "A development Plan for a product contains all these components"
)
# TODO: 4 - Instantiate an action_planning_agent using the 'knowledge_action_planning'
action_planning_agent = ActionPlanningAgent(openai_api_key, knowledge_action_planning)

# Product Manager - Knowledge Augmented Prompt Agent
persona_product_manager = (
    "You are a Product Manager, you are responsible for defining the "
    "user stories for a product."
)
knowledge_product_manager = (
    "Stories are defined by writing sentences with a persona, an action, "
    "and a desired outcome. "
    "The sentences always start with: As a "
    "Write several stories for the product spec below, where the personas "
    "are the different users of the product. "
    # TODO: 5 - Complete this knowledge string by appending the 
    # product_spec loaded in TODO 3
    + product_spec
)
# TODO: 6 - Instantiate a product_manager_knowledge_agent using 
# 'persona_product_manager' and the completed 'knowledge_product_manager'
product_manager_knowledge_agent = KnowledgeAugmentedPromptAgent(
    openai_api_key, 
    persona_product_manager, 
    knowledge_product_manager
)

# Product Manager - Evaluation Agent
# TODO: 7 - Define the persona and evaluation criteria for a Product Manager 
# evaluation agent and instantiate it as product_manager_evaluation_agent. 
# This agent will evaluate the product_manager_knowledge_agent.
# The evaluation_criteria should specify the expected structure for user 
# stories (e.g., "As a [type of user], I want [an action or feature] so 
# that [benefit/value].").
persona_product_manager_eval = (
    "You are an evaluation agent that checks the answers of other "
    "worker agents."
)
evaluation_criteria_product_manager = (
    "The answer should be user stories that follow the standard structure: "
    "'As a [type of user], I want [an action or feature] so that "
    "[benefit/value].' "
    "Each story should have a clear persona, action, and desired outcome. "
    "The stories should be relevant to the product specification and cover "
    "different user types."
)
product_manager_evaluation_agent = EvaluationAgent(
    openai_api_key, 
    persona_product_manager_eval, 
    evaluation_criteria_product_manager, 
    product_manager_knowledge_agent, 
    max_interactions=3
)

# Program Manager - Knowledge Augmented Prompt Agent
persona_program_manager = (
    "You are a Program Manager, you are responsible for defining the "
    "features for a product."
)
knowledge_program_manager = (
    "Features of a product are defined by organizing similar user stories "
    "into cohesive groups."
)
# Instantiate a program_manager_knowledge_agent using 'persona_program_manager' 
# and 'knowledge_program_manager'
# (This is a necessary step before TODO 8. Students should add the 
# instantiation code here.)
program_manager_knowledge_agent = KnowledgeAugmentedPromptAgent(
    openai_api_key, 
    persona_program_manager, 
    knowledge_program_manager
)

# Program Manager - Evaluation Agent
persona_program_manager_eval = (
    "You are an evaluation agent that checks the answers of other "
    "worker agents."
)

# TODO: 8 - Instantiate a program_manager_evaluation_agent using 
# 'persona_program_manager_eval' and the evaluation criteria below.
evaluation_criteria_program_manager = (
    "The answer should be product features that follow the following structure: "
    "Feature Name: A clear, concise title that identifies the capability\n"
    "Description: A brief explanation of what the feature does and its purpose\n"
    "Key Functionality: The specific capabilities or actions the feature provides\n"
    "User Benefit: How this feature creates value for the user"
)
program_manager_evaluation_agent = EvaluationAgent(
    openai_api_key,
    persona_program_manager_eval,
    evaluation_criteria_program_manager,
    program_manager_knowledge_agent,
    max_interactions=3
)

# Development Engineer - Knowledge Augmented Prompt Agent
persona_dev_engineer = "You are a Development Engineer, you are responsible for defining the development tasks for a product."
knowledge_dev_engineer = "Development tasks are defined by identifying what needs to be built to implement each user story."
# Instantiate a development_engineer_knowledge_agent using 'persona_dev_engineer' and 'knowledge_dev_engineer'
# (This is a necessary step before TODO 9. Students should add the instantiation code here.)
development_engineer_knowledge_agent = KnowledgeAugmentedPromptAgent(openai_api_key, persona_dev_engineer, knowledge_dev_engineer)

# Development Engineer - Evaluation Agent
persona_dev_engineer_eval = "You are an evaluation agent that checks the answers of other worker agents."
# TODO: 9 - Instantiate a development_engineer_evaluation_agent using 'persona_dev_engineer_eval' and the evaluation criteria below.
evaluation_criteria_dev_engineer = (
    "The answer should be tasks following this exact structure: "
    "Task ID: A unique identifier for tracking purposes\n"
    "Task Title: Brief description of the specific development work\n"
    "Related User Story: Reference to the parent user story\n"
    "Description: Detailed explanation of the technical work required\n"
    "Acceptance Criteria: Specific requirements that must be met for completion\n"
    "Estimated Effort: Time or complexity estimation\n"
    "Dependencies: Any tasks that must be completed first"
)
development_engineer_evaluation_agent = EvaluationAgent(
    openai_api_key,
    persona_dev_engineer_eval,
    evaluation_criteria_dev_engineer,
    development_engineer_knowledge_agent,
    max_interactions=3
)


# Routing Agent
# TODO: 10 - Instantiate a routing_agent. You will need to define a list of agent dictionaries (routes) for Product Manager, Program Manager, and Development Engineer. Each dictionary should contain 'name', 'description', and 'func' (linking to a support function). Assign this list to the routing_agent's 'agents' attribute.

# Job function persona support functions
# TODO: 11 - Define the support functions for the routes of the routing agent (e.g., product_manager_support_function, program_manager_support_function, development_engineer_support_function).
# Each support function should:
#   1. Take the input query (e.g., a step from the action plan).
#   2. Get a response from the respective Knowledge Augmented Prompt Agent.
#   3. Have the response evaluated by the corresponding Evaluation Agent.
#   4. Return the final validated response.

def product_manager_support_function(query):
    """Support function for Product Manager routing"""
    print(f"Product Manager handling: {query}")
    # Step 1: Generate knowledge-based response
    knowledge_response = product_manager_knowledge_agent.respond(query)
    # Step 2: Evaluate the response for proper structure
    result = product_manager_evaluation_agent.evaluate(query)
    return f"Product Manager Result: {result['final_response']}"

def program_manager_support_function(query):
    """Support function for Program Manager routing"""
    print(f"Program Manager handling: {query}")
    # Step 1: Generate knowledge-based response
    knowledge_response = program_manager_knowledge_agent.respond(query)
    # Step 2: Evaluate the response for proper structure
    result = program_manager_evaluation_agent.evaluate(query)
    return f"Program Manager Result: {result['final_response']}"

def development_engineer_support_function(query):
    """Support function for Development Engineer routing"""
    print(f"Development Engineer handling: {query}")
    # Step 1: Generate knowledge-based response
    knowledge_response = development_engineer_knowledge_agent.respond(query)
    # Step 2: Evaluate the response for proper structure
    result = development_engineer_evaluation_agent.evaluate(query)
    return f"Development Engineer Result: {result['final_response']}"

# Define routes for the routing agent
routes = [
    {
        'name': 'Product Manager',
        'description': 'Handles user stories definition, persona identification, and product requirements gathering',
        'func': product_manager_support_function
    },
    {
        'name': 'Program Manager', 
        'description': 'Handles feature definition, organizing user stories into cohesive groups, and feature planning',
        'func': program_manager_support_function
    },
    {
        'name': 'Development Engineer',
        'description': 'Handles development tasks definition, technical implementation planning, and engineering work breakdown',
        'func': development_engineer_support_function
    }
]

routing_agent = RoutingAgent(openai_api_key, routes)

# Run the workflow

print("\n*** Workflow execution started ***\n")
# Workflow Prompt
# ****
workflow_prompt = "What would the development tasks for this product be?"
# ****
print(f"Task to complete in this workflow, workflow prompt = {workflow_prompt}")

print("\nDefining workflow steps from the workflow prompt")
# TODO: 12 - Implement the workflow.
#   1. Use the 'action_planning_agent' to extract steps from the 'workflow_prompt'.
#   2. Initialize an empty list to store 'completed_steps'.
#   3. Loop through the extracted workflow steps:
#      a. For each step, use the 'routing_agent' to route the step to the appropriate support function.
#      b. Append the result to 'completed_steps'.
#      c. Print information about the step being executed and its result.
#   4. After the loop, print the final output of the workflow (the last completed step).

# Extract workflow steps using action planning agent
workflow_steps = action_planning_agent.extract_steps_from_prompt(workflow_prompt)
print(f"Extracted workflow steps: {workflow_steps}")

# Initialize completed steps list
completed_steps = []

# Loop through each workflow step
for i, step in enumerate(workflow_steps):
    print(f"\n=== Executing Step {i+1}: {step} ===")
    
    # Route the step to appropriate agent
    step_result = routing_agent.route(step)
    
    # Append result to completed steps
    completed_steps.append(step_result)
    
    # Print step execution info
    print(f"Step {i+1} completed. Result: {step_result[:200]}...")  # Print first 200 chars

# Print final workflow output
print(f"\n*** Workflow execution completed ***")
print(f"Final workflow output (last step): {completed_steps[-1] if completed_steps else 'No steps completed'}")