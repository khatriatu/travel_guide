from google.adk.agents import Agent
from google.adk.tools import google_search

accomodation_agent = Agent(
    name="accomodation_agent",
    model="gemini-2.0-flash",
    description="Suggests hotels, hostels, and stays for a given destination using web search.",
    instruction=(
        "You are an expert in recommending accommodation options for travelers. "
        "Use web search to find current information about hotels, hostels, Airbnb, and unique stays for the user's destination. "
        "Search for terms like 'best hotels in [destination]', 'budget accommodation [destination]', 'luxury hotels [destination]'. "
        "Provide a mix of different price ranges and accommodation types. "
        "Include specific hotel names, brief descriptions, and any notable features or ratings when available."
    ),
    tools=[google_search],
)
