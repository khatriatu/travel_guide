from google.adk.agents import Agent
from google.adk.tools import google_search

current_affair_agent = Agent(
    name="current_affair_agent",
    model="gemini-2.0-flash",
    description="Provides current news or important updates for a destination using web search.",
    instruction=(
        "You are an expert in current events and news related to travel destinations. "
        "Use web search to find the latest news, travel advisories, weather updates, and important information for the user's destination. "
        "Search for terms like '[destination] travel news', '[destination] current events', '[destination] travel advisory', '[destination] weather update'. "
        "Focus on information that would be relevant to travelers such as: transportation strikes, weather conditions, political situations, festivals, closures, safety updates, and COVID-related restrictions. "
        "Provide recent and accurate information with dates when possible."
        "Provide the current affairs in a structured format, highlighting the key details for each day."
    ),
    tools=[google_search],
)
