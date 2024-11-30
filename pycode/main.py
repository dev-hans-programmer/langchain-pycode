import argparse
from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence
from pycode.config import config

print(config)

parser = argparse.ArgumentParser()
parser.add_argument("--language", default="python")
parser.add_argument("--task", default="Return a list of numbers")
args = parser.parse_args()

code_prompt = PromptTemplate(
    template="Write a {language} function that will {task}",
    input_variables=["language", "task"],
)

code_test_prompt = PromptTemplate(
    template="Write a test for the code: {code}", input_variables=["code"]
)
openai_llm = OpenAI()

# Create a code chain
code_chain = code_prompt | openai_llm | StrOutputParser()
# Create a test chain
code_test_chain = code_test_prompt | openai_llm | StrOutputParser()
# Create a sequence
# chain = RunnableSequence(code_chain, code_test_chain)
# or
chain = code_chain | code_test_chain
# invoke the sequence
# Print the result
result = chain.invoke({"language": args.language, "task": args.task})
print(result)
