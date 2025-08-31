# Smart Travel Guide - Google ADK AI Agent

A basic Google Agent Development Kit (ADK) implementation that creates an AI-powered travel guide agent. This agent can provide travel information, answer questions, and help users plan their trips.

## Features

- **Interactive AI Agent**: Powered by Google's Gemini 2.0 Flash model
- **Travel Information**: Get details about popular destinations (Paris, Tokyo, New York)
- **Question Answering**: Ask general travel-related questions
- **Friendly Greetings**: Personalized welcome messages
- **Web UI**: Interactive browser-based interface for chatting with the agent

## Prerequisites

- Python 3.9 or higher
- Google AI Studio API key (free from [Google AI Studio](https://aistudio.google.com/apikey))

## Quick Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure API Key

1. Get your free API key from [Google AI Studio](https://aistudio.google.com/apikey)
2. Open the `.env` file
3. Replace `YOUR_API_KEY_HERE` with your actual API key:

```env
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=your_actual_api_key_here
```

### 3. Run the Agent

#### Option A: Interactive Web UI (Recommended)
```bash
adk web
```
Then open your browser to `http://localhost:8000` and select "smart_travel_guide" from the dropdown.

#### Option B: Terminal Interface
```bash
adk run
```

#### Option C: Demo Script
```bash
python example.py
```

## Usage Examples

Once your agent is running, try these prompts:

- "Tell me about Paris"
- "What's the best time to visit Tokyo?"
- "I'm planning a trip to New York"
- "What should I pack for a European trip?"
- "Help me plan a weekend getaway"

## Project Structure

```
smart_travel_guide/
├── __init__.py          # Package initialization
├── ai_agent.py          # Main agent definition with tools
├── example.py           # Demo script for testing
├── .env                 # Environment variables (API key)
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

## Agent Tools

The agent comes with three built-in tools:

1. **simple_greeting**: Provides personalized welcome messages
2. **get_travel_info**: Returns travel information for supported destinations
3. **answer_question**: Handles general travel-related questions

## Customization

### Adding New Destinations

Edit the `travel_data` dictionary in `ai_agent.py`:

```python
travel_data = {
    "your_city": {
        "best_time": "Season information",
        "currency": "Currency info",
        "language": "Primary language",
        "highlights": "Main attractions"
    }
}
```

### Adding New Tools

Create new functions and add them to the `tools` list in the `root_agent` definition:

```python
def your_new_tool(parameter: str) -> dict:
    """Your tool description."""
    return {"status": "success", "result": "your result"}

root_agent = Agent(
    # ... other parameters
    tools=[simple_greeting, get_travel_info, answer_question, your_new_tool],
)
```

## Troubleshooting

### Common Issues

1. **Agent not in dropdown**: Make sure you're running `adk web` from the parent directory of `smart_travel_guide`
2. **API errors**: Verify your API key is correctly set in the `.env` file
3. **Import errors**: Ensure all dependencies are installed with `pip install -r requirements.txt`

### Getting Help

- [Google ADK Documentation](https://google.github.io/adk-docs/)
- [Google ADK Quickstart](https://google.github.io/adk-docs/get-started/quickstart/)
- [Google AI Studio](https://aistudio.google.com/)

## Next Steps

- Explore [ADK Tutorials](https://google.github.io/adk-docs/tutorials/) for advanced features
- Add memory and session management
- Integrate with external APIs for real-time travel data
- Deploy your agent using Google Cloud Run or Vertex AI

## License

This project is for educational and demonstration purposes.