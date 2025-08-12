# finance-agent
A web-based AI playground for financial research, featuring two agents: one for web-based financial information search with source citation, and another for real-time stock and financial data analysis. Users interact via an intuitive interface for instant insights.

Features
Web Search Agent: Answers financial questions using web search (DuckDuckGo) and always cites sources.
Financial Agent: Answers questions about stocks and financial data using real-time market tools (YFinance). Presents data in tables for clarity.
Markdown Output: Responses are formatted in Markdown for readability.
Tool Call Transparency: Shows which tools the agent uses to answer each query.

# Setup

Clone the repository:
git clone https://github.com/meprashantsah/finance-agent.git
cd finance-agent

Create and activate a virtual environment:
python -m venv venv
On Windows:
venv\Scripts\activate
On macOS/Linux:
source venv/bin/activate

Install dependencies: 
pip install -r requirements.txt
PHI_API_KEY=your_phi_api_key_here
GROQ_API_KEY= your_groq_api_key_here

Run the playground:
python playground.py