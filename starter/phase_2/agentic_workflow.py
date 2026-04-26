# agentic_workflow.py

#1 - Import the following agents: ActionPlanningAgent, KnowledgeAugmentedPromptAgent, EvaluationAgent, RoutingAgent from the workflow_agents.base_agents module
from workflow_agents.base_agents import ActionPlanningAgent,KnowledgeAugmentedPromptAgent, EvaluationAgent, RoutingAgent
import os
from dotenv import load_dotenv
from pathlib import Path # for file path

#2 - Load the OpenAI key into a variable called open_api_key
load_dotenv()
open_api_key = os.getenv("OPENAI_API_key")
#print(open_api_key)
# load the product spec
#3 - Load the product spec document Product-Spec-Email-Router.txt into a variable called product_spec
#Get the directory where this sourcefile is located
srcdir = Path(__file__).parent
# Specify a path using the / operator
prodspec_flnm = "Product-Spec-Email-Router.txt"
file_path = srcdir / prodspec_flnm
#print(file_path)
product_spec = ''
with file_path.open('r') as txtfile:
    product_spec = txtfile.read()
# Instantiate all the agents

# Action Planning Agent


knowledge_action_planning = (
    "Extract 3 high-level workflow steps for Email Router project planning:\n"
    "1. Generate user stories: create comprehensive user stories for the Email Router product with each user story containing a [persona], an action and desired outcome\n"
    "2. Define product features:create comprehensive product features with Feature Name, Description, Key Functionality, and User Benefit\n"
    "3. Define development tasks: create comprehensive engineering tasks corresponding to the user stories with Task ID, Title, Description, Acceptance Criteria, Estimated Effort, and Dependencies\n"
    "Focus specifically on Email Router functionality, not generic examples.")

#4 - Instantiate an action_planning_agent using the 'knowledge_action_planning'
action_planning_agent = ActionPlanningAgent(open_api_key,knowledge_action_planning)

# Product Manager - Knowledge Augmented Prompt Agent
persona_product_manager = "You are a Product Manager, you are solely responsible for generating user stories. You identify,and generate user stories for a product after analysing the product specification given."
knowledge_product_manager = ( f"""
    User Stories are defined by writing sentences with a persona, an action, and a desired outcome. 
    The stories always start with: 'As a [persona], I want...' .
    Write several stories for the product spec attached, where the personas are the different users of the product. 
    Product Spec follows: '{product_spec}'"""
)

#6 - Instantiate a product_manager_knowledge_agent using 'persona_product_manager' and the completed 'knowledge_product_manager'
product_manager_knowledge_agent = KnowledgeAugmentedPromptAgent(open_api_key,persona_product_manager,knowledge_product_manager)

# Product Manager - Evaluation Agent
#7 - Define the persona and evaluation criteria for a Product Manager evaluation agent and instantiate it as product_manager_evaluation_agent. This agent will evaluate the product_manager_knowledge_agent.
persona_prod_manager_eval = "You are an evaluation agent that checks the answers of product manager agents."
# The evaluation_criteria should specify the expected structure for user stories (e.g., "As a [type of user], I want [an action or feature] so that [benefit/value].").
eval_criteria = "The response should follow the following structure for user stories.Eg: As a [persona or type of user], I want [an action or feature] so that [outcome or benefit/value]. "
product_manager_evaluation_agent = EvaluationAgent(open_api_key,persona_prod_manager_eval,eval_criteria,product_manager_knowledge_agent,10)

# Program Manager - Knowledge Augmented Prompt Agent
persona_program_manager = "You are a Program Manager, you are only responsible for defining and organizing features for a product."
knowledge_program_manager = "Features of a product are created by grouping already created user stories into cohesive,logical groups."
# Instantiate a program_manager_knowledge_agent using 'persona_program_manager' and 'knowledge_program_manager'
# (This is a necessary step before TODO 8. Students should add the instantiation code here.)
program_manager_knowledge_agent = KnowledgeAugmentedPromptAgent(open_api_key,persona_program_manager,knowledge_program_manager)

# Program Manager - Evaluation Agent
persona_program_manager_eval = "You are an evaluation agent that checks the answers of other worker agents."
#8 - Instantiate a program_manager_evaluation_agent using 'persona_program_manager_eval' and the evaluation criteria below.
#                      "The answer should be product features that follow the following structure: " \
#                      "Feature Name: A clear, concise title that identifies the capability\n" \
#                      "Description: A brief explanation of what the feature does and its purpose\n" \
#                      "Key Functionality: The specific capabilities or actions the feature provides\n" \
#                      "User Benefit: How this feature creates value for the user"
#                      For the 'agent_to_evaluate' parameter, refer to the provided solution code's pattern.
program_mgr_eval_criteria = (
                                "The response should be product features that follow the following structure: \n"
                                "Feature Name: A clear, concise title that identifies the capability\n" 
                                "Description: A brief explanation of what the feature does and its purpose\n"  
                                "Key Functionality: The specific capabilities or actions the feature provides\n"  
                                "User Benefit: How this feature creates value for the user"
                            )
#For the 'agent_to_evaluate' parameter, refer to the provided solution code's pattern.
program_manager_evaluation_agent = EvaluationAgent(open_api_key,persona_program_manager_eval,program_mgr_eval_criteria, program_manager_knowledge_agent,10)
# Development Engineer - Knowledge Augmented Prompt Agent
persona_dev_engineer = "You are a Development Engineer, you are responsible for defining and describing one or more development tasks for a product."
knowledge_dev_engineer = "Development tasks define what needs to be built to implement features to support each user story."
# Instantiate a development_engineer_knowledge_agent using 'persona_dev_engineer' and 'knowledge_dev_engineer'
# (This is a necessary step before TODO 9. Students should add the instantiation code here.)
development_engineer_knowledge_agent = KnowledgeAugmentedPromptAgent(open_api_key,persona_dev_engineer,knowledge_dev_engineer)
# Development Engineer - Evaluation Agent
persona_dev_engineer_eval = "You are an evaluation agent that evaluates and checks the answers of Development Engineer Knowledge agents."
#9 - Instantiate a development_engineer_evaluation_agent using 'persona_dev_engineer_eval' and the evaluation criteria below.
#                      "The answer should be tasks following this exact structure: " \
#                      "Task ID: A unique identifier for tracking purposes\n" \
#                      "Task Title: Brief description of the specific development work\n" \
#                      "Related User Story: Reference to the parent user story\n" \
#                      "Description: Detailed explanation of the technical work required\n" \
#                      "Acceptance Criteria: Specific requirements that must be met for completion\n" \
#                      "Estimated Effort: Time or complexity estimation\n" \
#                      "Dependencies: Any tasks that must be completed first"
development_engineer_eval_criteria = ("Evaluate that the response aways specifies one or more development tasks that are essentioal for creating the product. The tasks have to be in the following structure: \n" \
                        "Task ID: A unique identifier for tracking purposes\n" \
                        "Task Title: Brief description of the specific development work\n" \
                        "Related User Story: Reference to the parent user story\n" \
                        "Description: Detailed explanation of the technical work required\n" \
                        "Acceptance Criteria: Specific requirements that must be met for completion\n" \
                        "Estimated Effort: Time or complexity estimation\n" \
                        "Dependencies: Any tasks that must be completed first"
                       )
development_engineer_evaluation_agent= EvaluationAgent(open_api_key,persona_dev_engineer_eval,development_engineer_eval_criteria,development_engineer_knowledge_agent,10)
# Routing Agent
#10 - Instantiate a routing_agent. You will need to define a list of agent dictionaries (routes) for Product Manager, Program Manager, and Development Engineer. Each dictionary should contain 'name', 'description', and 'func' (linking to a support function). Assign this list to the routing_agent's 'agents' attribute.
agents = [
    {
        "name": "Product Manager",
        "description": "Responsible for defining product personas and user stories only. Does not define features or tasks. Does not group stories",
        "func": lambda x:product_manager_knowledge_agent.respond
    },
    {
        "name": "Program Manager",
        "description": "Responsible for defining the features for a product. Organizes similar user stories into cohesive groups.",
        "func": lambda x:program_manager_knowledge_agent.respond
    },
    {
        "name": "Development Engineer",
        "description": "Responsible for defining the development tasks for a product. Development tasks are defined by identifying what needs to be built to implement each user story.",
        "func": lambda x:development_engineer_knowledge_agent.respond
    }
]
routing_agent = RoutingAgent(open_api_key,agents)
# Job function persona support functions
#11 Define the support functions for the routes of the routing agent (e.g., product_manager_support_function, program_manager_support_function, development_engineer_support_function).
# Each support function should:
#   1. Take the input query (e.g., a step from the action plan).
#   2. Get a response from the respective Knowledge Augmented Prompt Agent.
#   3. Have the response evaluated by the corresponding Evaluation Agent.
#   4. Return the final validated response.
def product_manager_support_function(query):
    resp = product_manager_knowledge_agent.respond(query)
    return(product_manager_evaluation_agent.evaluate(resp)["response"])

def program_manager_support_function(query):
    resp = program_manager_knowledge_agent.respond(query)
    return(program_manager_evaluation_agent.evaluate(resp)["response"])

def development_engineer_support_function(query):
    print(f"Development Engineer Support function called for \n {query}")
    resp = development_engineer_knowledge_agent.respond(query)
    return(development_engineer_evaluation_agent.evaluate(resp)["response"])

# Run the workflow

print("\n*** Workflow execution started ***\n")
# Workflow Prompt
# ****
#workflow_prompt = "What would the development tasks for the product 'Email Router' be?"
workflow_prompt = "Put together a complete and thorough project plan for the product 'Email Router', including user stories, features and development tasks."

# ****
print(f"Task to complete in this workflow, workflow prompt = \n'{workflow_prompt}'")

print("\nDefining workflow steps from the workflow prompt")
#12 - Implement the workflow.
#   1. Use the 'action_planning_agent' to extract steps from the 'workflow_prompt'.
#   2. Initialize an empty list to store 'completed_steps'.
#   3. Loop through the extracted workflow steps:
#      a. For each step, use the 'routing_agent' to route the step to the appropriate support function.
#      b. Append the result to 'completed_steps'.
#      c. Print information about the step being executed and its result.
#   4. After the loop, print the final output of the workflow (the last completed step).

#print(f"Response from ActionPlanningAgent to the prompt '{workflow_prompt}' \n\n\n '{action_planning_agent.extract_steps_from_prompt(workflow_prompt)}'")
steps_from_prompt = action_planning_agent.extract_steps_from_prompt(workflow_prompt)
#print(f"Response from ActionPlanningAgent to the prompt '{workflow_prompt}' \n\n\n '{steps_from_prompt}'")


completed_steps=[]
for step in steps_from_prompt:
    print(f"\n\n***** Executing step: *******\n{step}")
    routing_res = routing_agent.route(step)
    completed_steps.append(routing_res)
    #print(f"Step {step} completed. Its results are shown above. \n")
print("====== All Steps are successfully executed =======")

print("\n*** CLEAN FINAL WORKFLOW OUTPUT ***")
for completed_step in completed_steps:
    print("\n", completed_step)


