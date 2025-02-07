# AI Sales Outreach Assistant

This project implements an AI-powered sales outreach assistant that ranks leads obtained from CRM data (CSV) and generates personalized outreach messages based on the leads' requirements. The system utilizes the `crewai` framework for AI agent orchestration and `agentops` for agent observability.

## Features

- **Lead Ranking:** Analyzes CRM leads to determine priority based on predefined criteria.
- **Personalized Outreach:** Generates tailored communication messages for each lead.
- **AI-Powered Agents:** Utilizes junior and senior sales associates to process and generate results.
- **Sequential Task Execution:** Ensures smooth and logical flow of operations.

## Installation

### Prerequisites

- Python 3.11
- Poetry (for dependency management)
- `crewai`, `agentops`

### Setup

1. Clone the repository:
   ```sh
   git clone <repository_url>
   cd sales-crew
   ```
2. Install dependencies using Poetry:
   ```sh
   poetry install
   ```
3. Set up environment variables:
   ```sh
   export AGENTOPS_API_KEY=<your_api_key>
   export OPENAI_API_KEY=<your_openai_api_key>
   ```
4. Ensure the CRM data file exists at the specified location or update the script accordingly.

## Usage

Run the AI sales outreach assistant with the following command:

```sh
poetry run python main.py
```

## Project Structure

```
 sales-crew/
 ├── agents.py  # Defines AI agents (junior and senior sales associates)
 ├── tasks.py   # Defines tasks for lead ranking and communication generation
 ├── main.py    # Main execution script
 ├── README.md  # Project documentation
 ├── retail_crm_lead_data.csv  # CRM lead data (input file)
```

## Workflow

1. The `junior_sales_associate` ranks the leads from the CRM data.
2. The `senior_sales_associate` generates personalized outreach messages.
3. The workflow executes sequentially using the `crewai` framework.
4. Results are printed to the console.

## License

This project is licensed under the MIT License.

## Contact

Feel free to reach out ar ranawatranveer0323@gmail.com :)

