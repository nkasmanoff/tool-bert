play_spotify_tool_description = """This tool is used when the user asks the llm to play a song on spotify.

Here are some examples of queries that would use this tool:
- Can you play the song "Bohemian Rhapsody" by Queen?
- Play Taylor Swift
- Please play some classical music
"""

check_weather_tool_description = """This tool is used when the user asks the llm to check the weather.

Here are some examples of queries that would use this tool:
- What is the weather like today?
- What's the weather outside?
- Tell me the weather.
"""

check_news_tool_description = """This tool is used when the user asks the llm to check the news.

Here are some examples of queries that would use this tool:
- What's in the news?
- What's the news?
- Tell me what's going on. 
"""

take_picture_tool_description = """This tool is used when the user asks the llm to take a picture.  

Here are some examples of queries that would use this tool:
- Take a photo.
- Can you take a picture? 
- What do you see?
"""

no_tool_needed_description = """This tool does not require any external tools. It is a standalone tool that can be used
without any additional tools. Basically the LLM can just generate the answer on it's own and requires no additional information. 

Here are some examples of queries that would use this tool:
- What is the capital of France?
- Who are you?
- Where is the Sun?
- When did the Titanic sink?
- Why is the sky blue?
- How can I train for a marathon?
"""



tool_names = {
    'play_spotify' : play_spotify_tool_description,
    'check_weather' : check_weather_tool_description,
    'check_news' : check_news_tool_description,
    'take_picture' : take_picture_tool_description,
    'no_tool_needed' : no_tool_needed_description,
}

tool_names = ['take_picture', 'no_tool_needed', 'check_news', 'check_weather', 'play_spotify']
