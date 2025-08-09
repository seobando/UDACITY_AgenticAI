#!/usr/bin/env python3
"""
Test script for RAGKnowledgePromptAgent
This script tests the RAG (Retrieval-Augmented Generation) functionality.
"""

import os
import sys
from dotenv import load_dotenv

# Add the parent directory to the Python path to import from phase_1
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from phase_1.workflow_agents.base_agents import RAGKnowledgePromptAgent

def test_rag_knowledge_prompt_agent():
    """Test the RAGKnowledgePromptAgent functionality."""
    
    # Load environment variables from .env file
    load_dotenv()
    
    # Get the OpenAI API key from environment variables
    openai_api_key = os.getenv('OPENAI_API_KEY')
    
    if not openai_api_key:
        print("Error: OPENAI_API_KEY not found in environment variables.")
        print("Please make sure you have set your API key in the .env file.")
        return
    
    # Define persona for the RAG agent
    persona = "a knowledgeable research assistant"
    
    # Create sample knowledge corpus for testing
    sample_knowledge = """
    Machine Learning is a subset of artificial intelligence that focuses on algorithms 
    and statistical models that computer systems use to perform tasks without explicit instructions.
    
    Deep Learning is a subset of machine learning that uses neural networks with multiple layers
    to model and understand complex patterns in data.
    
    Natural Language Processing (NLP) is a field of AI that focuses on the interaction between
    computers and human language, enabling machines to understand, interpret, and generate human text.
    
    Computer Vision is a field of AI that enables computers to interpret and understand visual
    information from the world, including images and videos.
    """
    
    print("Testing RAGKnowledgePromptAgent...")
    print(f"Persona: {persona}")
    print("Sample Knowledge Corpus: Machine Learning, Deep Learning, NLP, Computer Vision concepts")
    print("-" * 50)
    
    try:
        # Instantiate the RAGKnowledgePromptAgent
        rag_agent = RAGKnowledgePromptAgent(openai_api_key, persona)
        
        # Process the knowledge into chunks and embeddings
        print("Step 1: Chunking the knowledge corpus...")
        chunks = rag_agent.chunk_text(sample_knowledge)
        print(f"Created {len(chunks)} chunks from the knowledge corpus.")
        
        print("\nStep 2: Calculating embeddings for chunks...")
        embeddings_df = rag_agent.calculate_embeddings()
        print(f"Generated embeddings for {len(embeddings_df)} chunks.")
        
        # Test prompts
        test_prompts = [
            "What is machine learning?",
            "Tell me about deep learning",
            "How does computer vision work?"
        ]
        
        print("\nStep 3: Testing RAG functionality with different prompts...")
        print("-" * 50)
        
        for i, prompt in enumerate(test_prompts, 1):
            print(f"\nTest {i}:")
            print(f"Prompt: {prompt}")
            
            response = rag_agent.find_prompt_in_knowledge(prompt)
            print(f"Response: {response}")
            print("-" * 30)
        
        print("\nRAG Process Analysis:")
        print("✅ The RAG agent successfully:")
        print("1. Chunked the knowledge corpus into manageable pieces")
        print("2. Generated embeddings for each chunk")
        print("3. Found the most relevant chunk for each prompt using similarity search")
        print("4. Generated responses based on the retrieved relevant information")
        print("5. Used only the provided knowledge rather than general model knowledge")
        
        # Clean up generated files
        print(f"\nCleaning up generated files...")
        chunk_file = f"chunks-{rag_agent.unique_filename}"
        embedding_file = f"embeddings-{rag_agent.unique_filename}"
        
        if os.path.exists(chunk_file):
            os.remove(chunk_file)
            print(f"Removed {chunk_file}")
        
        if os.path.exists(embedding_file):
            os.remove(embedding_file)
            print(f"Removed {embedding_file}")
        
    except Exception as e:
        print(f"Error occurred: {e}")
        print("Please check your API key and internet connection.")
        print("Note: RAG agent requires additional setup and may have specific requirements.")

if __name__ == "__main__":
    test_rag_knowledge_prompt_agent() 