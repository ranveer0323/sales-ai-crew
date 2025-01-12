from crewai import Crew, Process
from agents import junior_sales_associate, senior_sales_associate
from tasks import lead_ranking, communication_generation
import agentops
import os

agentops.init(api_key=os.getenv("AGENTOPS_API_KEY"), auto_start_session=True)


lead_ranking.agent = junior_sales_associate
communication_generation.agent = senior_sales_associate

crew = Crew(
    agents=[junior_sales_associate, senior_sales_associate],
    tasks=[lead_ranking, communication_generation],
    process=Process.sequential,
    verbose=True
)

if __name__ == "__main__":
    file_path = "F:\\Learning\\sales-crew\\retail_crm_lead_data.csv"
    result = crew.kickoff(inputs={"file_path": file_path})
    print(result)
