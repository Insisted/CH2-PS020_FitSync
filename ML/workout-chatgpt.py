import os

import pandas as pd
import openai


openai.api_key = os.environ.get('ChatGPT')
MODEL = 'gpt-3.5-turbo'
messages = [ {'role': 'system', 'content': 'You are a intelligent workout/fitness coach.'} ]


def start(df): # Biarin dulu, test APInya jalan ga pake input manual
	message = input('User : ') 

	if message: 
		messages.append( 
			{'role': 'user', 'content': message}, 
		) 
		chat = openai.ChatCompletion.create( 
			model=MODEL, messages=messages 
		) 

	reply = chat.choices[0].message.content 

	print(f'ChatGPT: {reply}') 

	messages.append({'role': 'assistant', 'content': reply}) 


if __name__ == '__main__':
	df = pd.read_excel('./data/Gym-Visual-EXERCISES-list.xlsx', sheet_name='Animated GIFs')

	start(df)