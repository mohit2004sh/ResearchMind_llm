<<<<<<< HEAD
from langchain_mistralai import ChatMistralAI
from langchain.agents import create_agent
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from tool import scrape_url , searching
from dotenv import load_dotenv
load_dotenv()

model = ChatMistralAI(model = "mistral-small-latest", temperature=0)

#1st agent
def searchAgent():
    return create_agent(
        model= model,
        tools=[searching]
    )


# 2nd agent
def researchAgent():
    return create_agent(
        model= model,
        tools=[scrape_url]
    )


writer_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert research writer. Write clear, structured and insightful reports."),
    ("human", """Write a detailed research report on the topic below.

Topic: {topic}

Research Gathered:
{research}

Structure the report as:
- Introduction
- Key Findings (minimum 3 well-explained points)
- Conclusion
- Sources (list all URLs found in the research)

Be detailed, factual and professional."""),
])

writer_chain = writer_prompt | model | StrOutputParser()

#critic_chain 

critic_prompt = ChatPromptTemplate.from_messages([
     ("system", "You are a sharp and constructive research critic. Be honest and specific."),
    ("human", """Review the research report below and evaluate it strictly.

Report:
{report}

Respond in this exact format:

Score: X/10

Strengths:
- ...
- ...

Areas to Improve:
- ...
- ...

One line verdict:
..."""),
])

=======
from langchain_mistralai import ChatMistralAI
from langchain.agents import create_agent
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from tool import scrape_url , searching
from dotenv import load_dotenv
load_dotenv()

model = ChatMistralAI(model = "mistral-small-latest", temperature=0)

#1st agent
def searchAgent():
    return create_agent(
        model= model,
        tools=[searching]
    )


# 2nd agent
def researchAgent():
    return create_agent(
        model= model,
        tools=[scrape_url]
    )


writer_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert research writer. Write clear, structured and insightful reports."),
    ("human", """Write a detailed research report on the topic below.

Topic: {topic}

Research Gathered:
{research}

Structure the report as:
- Introduction
- Key Findings (minimum 3 well-explained points)
- Conclusion
- Sources (list all URLs found in the research)

Be detailed, factual and professional."""),
])

writer_chain = writer_prompt | model | StrOutputParser()

#critic_chain 

critic_prompt = ChatPromptTemplate.from_messages([
     ("system", "You are a sharp and constructive research critic. Be honest and specific."),
    ("human", """Review the research report below and evaluate it strictly.

Report:
{report}

Respond in this exact format:

Score: X/10

Strengths:
- ...
- ...

Areas to Improve:
- ...
- ...

One line verdict:
..."""),
])

>>>>>>> 1ab8a9506f5e007e8bae57503944d7e1919ee2f9
critic_chain = critic_prompt | model | StrOutputParser()