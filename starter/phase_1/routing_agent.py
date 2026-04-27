
#1 - Import the KnowledgeAugmentedPromptAgent and RoutingAgent
from workflow_agents.base_agents import KnowledgeAugmentedPromptAgent,RoutingAgent

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

openai_api_key = os.getenv("OPENAI_API_key")

persona = "You are a college professor"

knowledge = "You know everything about Texas"
#2 - Define the Texas Knowledge Augmented Prompt Agent
texas_knowledge_agent = KnowledgeAugmentedPromptAgent(openai_api_key,persona,knowledge)

knowledge = "You know everything about Europe"
#3 - Define the Europe Knowledge Augmented Prompt Agent
eu_knowledge_agent = KnowledgeAugmentedPromptAgent(openai_api_key,persona,knowledge)

persona = "You are a college math professor"
knowledge = "You know everything about math, you take prompts with numbers, extract math formulas, and show the answer without explanation"
#4 - Define the Math Knowledge Augmented Prompt Agent
math_knowledge_agent = KnowledgeAugmentedPromptAgent(openai_api_key,persona,knowledge)

routing_agent = RoutingAgent(openai_api_key, {})
agents = [
    {
        "name": "texas agent",
        "description": "Answer a question about Texas",
        #5 - Call the Texas Agent to respond to prompts
        "func": lambda x: texas_knowledge_agent.respond(x)
    },
    {
        "name": "europe agent",
        "description": "Answer a question about Europe",
        #6 - Define a function to call the Europe Agent
        "func": lambda x: eu_knowledge_agent.respond(x)
    },
    {
        "name": "math agent",
        "description": "When a prompt contains numbers, respond with a math formula",
        #7 - Define a function to call the Math Agent
        "func": lambda x: math_knowledge_agent.respond(x)
    }
]

routing_agent.agents = agents

#8 - Print the RoutingAgent responses to the following prompts:
#           - "Tell me about the history of Rome, Texas"
#           - "Tell me about the history of Rome, Italy"
#           - "One story takes 2 days, and there are 20 stories"
prompt_tex = "Tell me about the history of Rome, Texas"
prompt_eu = "Tell me about the history of Rome, Italy""Tell me about the history of Rome, Italy"
prompt_math= "One story takes 2 days, and there are 20 stories"
list_of_prompts = [prompt_tex,prompt_eu,prompt_math]
for pt in list_of_prompts:
    callf = routing_agent.route(pt)

    #print(f"Response from the best agent:\n\n'{callf(pt)}'")
    
    