from langchain.chat_models import AzureChatOpenAI
from langchain.prompts import ChatPromptTemplate

from langchain.output_parsers import ResponseSchema
from langchain.output_parsers import StructuredOutputParser

# This function shows the process of creating an output parser
# PLEASE DO NOT edit this function
def get_basic_output_parser():
    # Set up an output parser, starting with schema
    is_food_schema = ResponseSchema(name = "is_food", description = "Is the topic a food? Answer True if yes, False if no.")
    # This is a small example, so we just need one schema, 
    # but for more complex outputs, we can include multiple schemas
    response_schemas = [is_food_schema]
    output_parser = StructuredOutputParser.from_response_schemas(response_schemas)
    return output_parser

# This function shows the process of creating a prompt 
# that is compatible with the output_parser
def get_basic_prompt():
    # Set up a prompt to extract the necessary information and 
    # include a placeholder for some formatting instructions. 
    # We need the output to be JSON.
    prompt_template = """
    For the following topic, extract the following information:

    is_food: Is the topic a food? Answer True if yes, False if no.

    topic: {topic}

    {format_instructions}
    """
    prompt = ChatPromptTemplate.from_template(prompt_template)
    return prompt

# This function takes our prompt, model, and output parser and
# invokes them via a chain, thus returning the response
# PLEASE DO NOT edit this function but try invoking it with different topics
# and note the output
def invoke_basic_chain(topic):
    prompt = get_basic_prompt()
    model = AzureChatOpenAI()
    output_parser = get_basic_output_parser()
    chain = prompt | model | output_parser

    # Invoke the chain and parse the output using the output parser
    response = chain.invoke({"topic": topic, "format_instructions":  output_parser.get_format_instructions()})
    return response

# TODO Finish this function by creating an output_parser from
# the following schemas:
# - title
# - is_family_friendly
# - genre
# - run_time
# - year_released
def get_complex_output_parser():
    title_schema = ResponseSchema(name = "title", description = "What is the title of the movie?")
    is_family_friendly_schema = ResponseSchema(name = "is_family_friendly", description = "Is the movie family friendly? Return a boolean: True if yes, False otherwise")
    genre_schema = ResponseSchema(name = "genre", description = "What are the genre(s) of the movie? Return as a single string, genres separated by spaces")
    run_time_schema = ResponseSchema(name = "run_time", description = "The run time of the movie in the format \"X minutes\"")
    year_released_schema = ResponseSchema(name = "year_released", description = "The year the movie was released")

    response_schemas = [title_schema, is_family_friendly_schema, genre_schema, run_time_schema, year_released_schema]
    
    
    output_parser = StructuredOutputParser.from_response_schemas(response_schemas)
    return output_parser


def get_complex_prompt():
    prompt_template = """
    For the following movie, extract the following information:

    title: The title of the movie

    is_family_friendly: Is the movie family friendly? Return True if yes, False otherwise

    genre: The genre of the movie

    run_time: The run time of the movie in the format "X minutes"

    year_released: The year the movie was released
    ...

    movie: {movie}

    {format_instructions}

    Ensure the output is valid JSON.
    """
    prompt = ChatPromptTemplate.from_template(prompt_template)
    return prompt

def invoke_complex_chain(movie):
    prompt = get_complex_prompt()
    model = AzureChatOpenAI()
    output_parser = get_complex_output_parser()
    chain = prompt | model | output_parser

    # Invoke the chain and parse the output using the output parser
    response = chain.invoke({"movie": movie, "format_instructions":  output_parser.get_format_instructions()})
    return response


try:
    print(invoke_complex_chain("The Matrix"))
except Exception as e:
    print(e)