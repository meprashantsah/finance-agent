from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools # enables agent to access stock data, finacial information, etc. from yahoo finance
from phi.tools.duckduckgo import DuckDuckGo # enables agent to web search using DuckDuckGo

import os
from dotenv import load_dotenv
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
# groq_api_key = os.getenv("GROQ_API_KEY")

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

multi_ai_agent = Agent(
    model = Groq(id="llama-3.3-70b-versatile"),
    team=[web_search_agent, financial_agent],
    instructions= ["Always include the source of the information you provide.", "use tables to present financial data clearly"],
    show_tool_calls=True,
    markdown=True,
)

multi_ai_agent.print_response("summarize analyst recommendations and share the latest news for NVDA.", stream=True)

