# Test script for DirectPromptAgent class
#1 - Import the DirectPromptAgent class from BaseAgents
#from WorkflowAgents.baseagents import DirectPromptAgent
from workflow_agents.base_agents import DirectPromptAgent
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

#2 - Load the OpenAI API key from the environment variables
openai_api_key = os.getenv("OPENAI_API_key")

prompt = "What is the Capital of France?"

#3 - Instantiate the DirectPromptAgent as direct_agent
direct_agent = DirectPromptAgent(openai_api_key)
#4 - Use direct_agent to send the prompt defined above and store the response
direct_agent_response = direct_agent.respond(prompt)

# Print the response from the agent
print(direct_agent_response)

#5 - Print an explanatory message describing the knowledge source used by the agent to generate the response
print(f"The DirectPromptAgent  used the general knowledge from its model to get the answer to our direct question\n '  {prompt}'. ")
