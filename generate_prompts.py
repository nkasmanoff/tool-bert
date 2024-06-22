raw_question_prompt = """# Task Description
You are an LLM function calling and question pair generation machine. You are working with this tool description:

{tool_description}

It is your job to generate {num_raw_questions} random questions that a curious person might ask that could, 
theoretically, be answered using this tool. Try to make the questions start in various ways, but still be 
relevant to the tool and examples provided.

# Format Instructions
{format_instructions}
"""