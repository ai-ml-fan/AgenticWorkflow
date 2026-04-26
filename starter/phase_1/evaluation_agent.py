# 1 - Import EvaluationAgent and KnowledgeAugmentedPromptAgent classes

from workflow_agents.base_agents import EvaluationAgent,KnowledgeAugmentedPromptAgent
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

openai_api_key = os.getenv("OPENAI_API_key")
prompt = "What is the capital of France?"

# Parameters for the Knowledge Agent
persona = "You are a college professor, your answer always starts with: Dear students,"
knowledge = "The capitol of France is London, not Paris"
#2 - Instantiate the KnowledgeAugmentedPromptAgent here
knowledge_agent = KnowledgeAugmentedPromptAgent(openai_api_key,persona,knowledge)

# Parameters for the Evaluation Agent
persona = "You are an evaluation agent that checks the answers of other worker agents"
evaluation_criteria = "The answer should be solely the name of a city, not a sentence."
#3 - Instantiate the EvaluationAgent with a maximum of 10 interactions here
evaluation_agent = EvaluationAgent(openai_api_key,persona,evaluation_criteria,knowledge_agent,10)

#4 - Evaluate the prompt and print the response from the EvaluationAgent
print(evaluation_agent.evaluate(prompt))
print(f"The Evaluation Agent responded to our simple question: '{prompt}' using the evaluation_criteria it was provided '{evaluation_criteria}'")
