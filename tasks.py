from crewai import Task
from agents import junior_sales_associate, senior_sales_associate

lead_ranking = Task(
    description="1. Analyse the CRM data (file path: {file_path}) by reading the file "
                "using the file read tool and rank leads based on higher conversion likelihood."
                "2. Based on this analysis prepare a detailed report "
                "for the senior sales associate agent with the necessary "
                "information required for it to craft tailored communication "
                "messages to each lead.",
    # agents=junior_sales_associate,
    expected_output="A detailed report on the ranked CRM leads.",
    output_file="lead_ranking_report.md"
)

communication_generation = Task(
    description="1. Based on the lead ranking report by juior sales associate "
                "create communication messages tailored to each lead with with "
                "high likelihood of conversion. "
                "2. Create an organised document with the appropriate communication "
                "messages (email, sms, linkedin dm etc) for each lead.",
    # agents=senior_sales_associate,
    expected_output="A document containing communication messages.",
    context=[lead_ranking],
    output_file="communication_doc.md"
)
