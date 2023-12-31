from langchain.llms.openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType

load_dotenv()


def generate_pet_name(animal_type, pet_color, coat_pattern):
    llm = OpenAI(temperature=0.7)

    # name = llm("I have a dog pet and I want a cool name for it. Suggest me five cool names for my pet.")

    prompt_template_name = PromptTemplate(
        input_variables=['animal_type', 'pet_color', 'coat_pattern'],
        # template="I have a {animal_type} pet and I want a cool name for it, it is {pet_color} in color and has a {coat_pattern} pattern. Suggest me five cool names for my pet."
        template = "I have a {pet_color} {animal_type}, which has {coat_pattern} coat pattern. Please generate 5 names for my pet."
    )

    # LLM Chain --to--> name_chain
    name_chain = LLMChain(
        llm=llm, prompt=prompt_template_name, output_key="pet_name")
    response = name_chain({'animal_type': animal_type,
                          'pet_color': pet_color, 'coat_pattern': 'coat_pattern'})
    return response

# Eitan's implementation for the landing page.
def generate_output(input):
    llm = OpenAI(temperature=0.7)

    prompt_template_name = PromptTemplate(
        input_variables=['input'],
        template="{input}"
    )

    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="output")
    response = name_chain({'input': input})

    return response

def langchain_agent(question):
    llm = OpenAI(temperature=0)

    # Note - Wikipedia must be installed, numexpr for numerical expression evaluator for NumPy.
    # pip install wikipedia numexpr
    tools = load_tools(["wikipedia", "llm-math"], llm=llm)
    agent = initialize_agent(
        tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
    )

    return agent(question)
 


if __name__ == "__main__":
    # print (generate_pet_name("cat"))
    # print (generate_pet_name("cow", "black"))
    langchain_agent()
