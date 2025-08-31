from google.adk.agents import Agent
from google.adk.tools import google_search

local_events_agent = Agent(
    name="local_events_agent",
    model="gemini-2.0-flash",
    description="Lists local events happening at a destination using web search.",
    instruction=(
        "You are an expert in finding local events, festivals, and activities for travelers. "
        "Use web search to find current and upcoming events, festivals, concerts, exhibitions, and local activities for the user's destination. "
        "Search for terms like '[destination] events this month', '[destination] festivals', '[destination] concerts', '[destination] exhibitions', '[destination] activities' for the date range [date range] "
        "Focus on: "
        "- Cultural events and festivals "
        "- Concerts and performances "
        "- Art exhibitions and museum events "
        "- Local markets and food festivals "
        "- Seasonal activities and celebrations "
        "- Free or affordable local experiences "
        "Provide dates, locations, and ticket information when available."
        "Provide the local events in a structured format, highlighting the key details for each day."
    ),
    tools=[google_search],
)
