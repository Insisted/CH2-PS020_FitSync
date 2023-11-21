import asyncio
import os

import pandas as pd
from api_key import OPENAI_API_KEY
from openai import AsyncOpenAI

MODEL = 'gpt-3.5-turbo'
messages = [{
	'role': 'system',
	'content': '''
You are an intelligent workout/fitness coach. I have a task that would need me to classify a workout as "Beginner|Intermediate|Expert" level with respect of the data as "Male|Female", help me with that. Answer me with a JSON response in this structure
```
{
    "name": "{What I asked you}",
    "gender": "{Gender based on the input}"
    "desc": "{The description of the workout}",
    "level": "{The level of the workout}"
}
```
No explaining no nothing.
'''
}]

client = AsyncOpenAI(api_key=OPENAI_API_KEY)


async def main(df):
	message = input('User : ') 
	
	if message:
		messages.append({'role': 'user', 'content': message}) 

		chat = await client.chat.completions.create(
			messages=messages,
			model=MODEL,
		)

	reply = chat.choices[0].message.content 

	print(f'ChatGPT: {reply}') 

	messages.append({'role': 'assistant', 'content': reply}) 


if __name__ == '__main__':
	df = pd.read_excel('./ML/data/Gym-Visual-EXERCISES-list.xlsx', sheet_name='Animated GIFs')

	asyncio.run(main(df))

	print(messages)
