from google.adk.agents import Agent

def simple_greeting(name: str = "there") -> dict:
    """A simple greeting function that takes a name and returns a personalized greeting.
    
    Args:
        name (str): The name of the person to greet. Defaults to "there".
        
    Returns:
        dict: A response containing status and greeting message.
    """
    return {
        "status": "success",
        "message": f"Hello {name}! I'm your AI travel guide assistant. How can I help you today?"
    }

def get_travel_info(destination: str) -> dict:
    """Provides basic travel information for a destination.
    
    Args:
        destination (str): The travel destination to get information about.
        
    Returns:
        dict: Travel information or error message.
    """
    # Simple mock data for demonstration
    travel_data = {
        "paris": {
            "best_time": "April to June and September to October",
            "currency": "Euro (EUR)",
            "language": "French",
            "highlights": "Eiffel Tower, Louvre Museum, Notre-Dame Cathedral"
        },
        "tokyo": {
            "best_time": "March to May and September to November",
            "currency": "Japanese Yen (JPY)", 
            "language": "Japanese",
            "highlights": "Tokyo Tower, Senso-ji Temple, Shibuya Crossing"
        },
        "new york": {
            "best_time": "April to June and September to November",
            "currency": "US Dollar (USD)",
            "language": "English", 
            "highlights": "Statue of Liberty, Central Park, Times Square"
        }
    }
    
    dest_lower = destination.lower()
    if dest_lower in travel_data:
        info = travel_data[dest_lower]
        return {
            "status": "success",
            "destination": destination,
            "info": info
        }
    else:
        return {
            "status": "error",
            "message": f"Sorry, I don't have travel information for {destination} yet. I currently have info for Paris, Tokyo, and New York."
        }

def answer_question(question: str) -> dict:
    """Answers general travel-related questions.
    
    Args:
        question (str): The question to answer.
        
    Returns:
        dict: Response with answer or guidance.
    """
    return {
        "status": "success",
        "question": question,
        "response": f"I've received your question: '{question}'. I'm a smart travel guide and I'm here to help with travel-related queries. Feel free to ask about destinations, travel tips, or use my other tools!"
    }

# Create the main agent
root_agent = Agent(
    name="smart_travel_guide",
    model="gemini-2.0-flash",
    description="A smart travel guide AI agent that helps users with travel information and questions.",
    instruction=(
        "You are a helpful and knowledgeable travel guide AI assistant. "
        "You can provide travel information for destinations, answer travel-related questions, "
        "and help users plan their trips. Be friendly, informative, and encouraging. "
        "When users ask for information about destinations, use the get_travel_info tool. "
        "For general questions, use the answer_question tool. "
        "Always greet new users warmly using the simple_greeting tool."
    ),
    tools=[simple_greeting, get_travel_info, answer_question],
)
