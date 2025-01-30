from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parents[1]))

from ollama import chat
from util.llm_utils import pretty_stringify_chat, ollama_seed as seed

# Add you code below
sign_your_name = 'Dheeraj Gollu'
model = 'llama3.2'
options = {'temperature': 1.0, 'max_tokens': 200}
messages = [{'role': 'system', 'content' : 'You are a Dungeons and Dragons (DnD) Dungeon Master.\
              You are responsible for creating the details and challenges of an adventure,\
              maintaining continuity of events, and controlling all aspects of the game.'},
              
            {'role': 'user', 'content': 'Start a DnD game.'}]


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

