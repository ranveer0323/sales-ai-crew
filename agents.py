from crewai import Agent, LLM
from crewai_tools import FileReadTool
import os

groq_api_key = os.getenv("GROQ_API_KEY")
file_read_tool = FileReadTool()

# llm = LLM(
#     model="llama-3.1-70b-versatile",
#     api_key=groq_api_key,
#     base_url="https://api.groq.com/openai/v1"
# )

llm = LLM(
    model="gpt-4o-mini"
)

junior_sales_associate = Agent(
    role="Junior Sales Associate",
    goal="Analyse CRM data and rank leads.",
    backstory="You are a junior sales associate who is experienced in "
              "analysing CRM data and ranking leads which will convert.",
    verbose=True,
    tools=[file_read_tool],
    llm=llm,
    max_iter=7
)

senior_sales_associate = Agent(
    role="Senior Sales Associate",
    goal="Craft tailored communication messages for each lead.",
    backstory="You are a senior sales associate who is experienced in "
              "outreach and communication. You have a deep understanding "
              "and experience in crafting effective communication messages like "
              "mails, sms and so on to convert a lead.",
    verbose=True,
    llm=llm
)
