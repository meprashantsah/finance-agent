import openai
from phi.agent import Agent
import phi.api
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools  
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv

import os
import phi
from phi.playground import Playground, serve_playground_app
load_dotenv()

phi.api = os.getenv("PHI_API_KEY")

# web search agent
web_search_agent = Agent(
    name="Web Search Agent",
    role="A financial agent that can search the web for information and answer questions about financial topics.",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGo()],
    instructions= ["Always  include the source of the information you provide."],
    show_tool_calls=True,
    markdown=True,
)

# financial agent
financial_agent = Agent(
    name="Financial Agent",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True, company_news=True)],
    instructions=["use tables to present financial data clearly"],
    show_tool_calls=True,
    markdown=True,
)

app = Playground(agents=[web_search_agent, financial_agent]).get_app()

if __name__=="__main__":
    serve_playground_app("playground:app", reload=True)
