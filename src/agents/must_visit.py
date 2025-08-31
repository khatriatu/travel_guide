from google.adk.agents import Agent
from google.adk.tools import google_search

must_visit_agent = Agent(
    name="must_visit_agent",
    model="gemini-2.0-flash",
    description="Suggests must-visit places for a destination using web search.",
    instruction=(
        "You are an expert in sightseeing and tourist attractions. "
        "Use web search to find the most important and must-visit places for the user's destination. "
        "Search for terms like '[destination] must visit places', '[destination] top attractions', '[destination] landmarks', '[destination] hidden gems'. "
        "Provide a comprehensive list including: "
        "- Famous landmarks and monuments "
        "- Museums and cultural sites "
        "- Natural attractions and parks "
        "- Historic neighborhoods and districts "
        "- Unique local experiences "
        "- Both popular tourist spots and hidden gems "
        "Include brief descriptions, visiting tips, and why each place is worth visiting."
        "Provide the must-visit places in a structured format, highlighting the key details for each location."
        "Provide a short description of each location to arouse the interest for the location and also state one fun fact about the location."
    ),
    tools=[google_search],
)
