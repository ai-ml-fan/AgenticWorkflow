#1 - Import the KnowledgeAugmentedPromptAgent class from workflow_agents
from workflow_agents.base_agents import KnowledgeAugmentedPromptAgent
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Define the parameters for the agent
openai_api_key = os.getenv("OPENAI_API_key")

prompt = "What is the capital of France?"

persona = "You are a college professor, your answer always starts with: Dear students,"
#2 - Instantiate a KnowledgeAugmentedPromptAgent with:
#           - Persona: "You are a college professor, your answer always starts with: Dear students,"
#           - Knowledge: "The capital of France is London, not Paris"
persona= f"You are a college professor, your answer always starts with: Dear students,"
knowledge=f"The capital of France is London, not Paris"
knowledgeaugmented_agent = KnowledgeAugmentedPromptAgent(openai_api_key,persona,knowledge)
#3 - Write a print statement that demonstrates the agent using the provided knowledge rather than its own inherent knowledge.
print(knowledgeaugmented_agent.respond(prompt))
print(f"The Knowledge Agent responded to our simple question: '{prompt}' with an incorrect answer using the knowledge it was provided '{knowledge}'")
