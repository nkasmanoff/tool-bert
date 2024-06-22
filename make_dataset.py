from typing import List

from langchain.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field, validator
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
from generate_prompts import raw_question_prompt
from tools import tool_names
import pandas as pd 
import os
import json

class QuestionGeneratorTool(BaseModel):
    questions: List[str] = Field(description="questions the LLM will generate.")


def tool_name2_id(tool_name, df):
    return df['tool_name'].unique().tolist().index(tool_name)

def get_id2tool_name(id, tool_names):
    return tool_names[id]



def make_tool_calling_dataset(model_name='gpt-4-turbo', num_raw_questions=50):

    if not os.path.exists('generated_questions'):
        os.makedirs('generated_questions')

    parser = PydanticOutputParser(pydantic_object=QuestionGeneratorTool)

    prompt = PromptTemplate(
        template=raw_question_prompt,
        input_variables=["tool_description", "num_raw_questions"],
        partial_variables={"format_instructions": parser.get_format_instructions()},
    )


    model = ChatOpenAI(temperature=0, model=model_name)

    chain = prompt | model | parser

    for tool_name, tool_description in tool_names.items():
        questions = chain.invoke({"tool_description": tool_description, "num_raw_questions": num_raw_questions})
        # save questions to a list with tool name as the title, appending to the file
        with open(f"generated_questions/{tool_name}.txt", "a") as f:
            for question in questions.questions:
                f.write(question + "\n")
                
        print(f"Generated questions for {tool_name}")    

    tools_df = pd.DataFrame(columns=['tool_name', 'command'])
    tool_commands = os.listdir('generated_questions')

    for tool_command in tool_commands:
        tool_name = tool_command.split('.')[0]
        with open(f'generated_questions/{tool_command}', 'r') as f:
            commands = f.readlines()
        tools_df = pd.concat([tools_df, pd.DataFrame({'tool_name': [tool_name]*len(commands), 'command': commands})])

        
    tools_df['command'] = tools_df['command'].apply(lambda x: x.replace('\n', ' ').strip())
    tools_df['label'] = None
    tools_df['label'] = tools_df['tool_name'].apply(lambda x: tool_name2_id(x, tools_df))
    tools_json = tools_df.to_dict('records')


    with open('generated_questions/dataset.json', 'w') as f:
        json.dump(tools_json, f, indent=4)


if __name__ == "__main__":
    make_tool_calling_dataset()