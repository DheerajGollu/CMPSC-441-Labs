from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parents[1]))

from ollama import chat
from util.llm_utils import pretty_stringify_chat, ollama_seed as seed

# Add you code below
sign_your_name = 'Dheeraj Gollu'
model = 'llama3.2'
options = {'temperature': 2.0, 'max_tokens': 1000, 'repetition_penalty': 1.2}
messages = [{'role': 'system', 'content' : 'You are a Dungeons and Dragons (DnD) Dungeon Master.\
              You are responsible for creating the details and challenges of an adventure,\
              maintaining continuity of events, and controlling all aspects of the game.\
              Make sure you have an interesting and unique story for every new game.\
              This includes having a new plot, new supporting characters (new names and descriptions), and number of options.\
              Make sure the number of options depends on the scenario and does not exceed 10.\
              Also, make sure the text is formatted clearly with aesthetic spacing.'},

            {'role': 'system', 'content': 'Make descriptions vivd and concise.\
             Additionally, make sure that fun and interesting short descriptions are provided for characters.\
             Also ensure that proper grammar is maintained.'},
              
            {'role': 'user', 'content': 'Start a new DnD game.'}]


# But before here.

options |= {'seed': seed(sign_your_name)}
# Chat loop
while True:
  response = chat(model=model, messages=messages, stream=False, options=options)
  # Add your code below
  
  messages.append({'role': 'assistant', 'content': response.message.content})

  print(f'Agent: {response.message.content}')

  message = {'role': 'user', 'content': input('You: ')}
  messages.append(message)

  # But before here.
  if messages[-1]['content'] == '/exit':
    break

# Save chat
with open(Path('lab03/attempts.txt'), 'a') as f:
  file_string  = ''
  file_string +=       '-------------------------NEW ATTEMPT-------------------------\n\n\n'
  file_string += f'Model: {model}\n'
  file_string += f'Options: {options}\n'
  file_string += pretty_stringify_chat(messages)
  file_string += '\n\n\n------------------------END OF ATTEMPT------------------------\n\n\n'
  f.write(file_string)

