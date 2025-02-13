from pathlib import Path
import sys

sys.path.append(str(Path(__file__).parents[1]))

from util.llm_utils import TemplateChat

def run_console_chat(sign, **kwargs):
    chat = TemplateChat.from_file(sign=sign, **kwargs)
    chat_generator = chat.start_chat()
    print(next(chat_generator))
    while True:
        try:
            message = chat_generator.send(input('You: '))
            print('Agent:', message)
        except StopIteration as e:
            if isinstance(e.value, tuple):
                print('Agent:', e.value[0])
                ending_match = e.value[1]
                print('Ending match:', ending_match)
            break

lab04_params = {'template_file': 'lab04/lab04_trader_chat.json',
                'sign': 'Dheeraj',
                'end_regex': r'ORDER(.*)DONE'}

if __name__ ==  '__main__':
    # run lab04.py to test your template interactively
    pass

#"content": "You are a store owner in DnD who sells items to customers. You have the following inventory: {{inventory}}. Greet a customer by showing your inventory and asking what the customer wants. As long as you have the item in the inventory, you can sell any amount of that item. There is no need to ask for payment. If you have all the items a customer asks, output each and every item for every amount of that item. For example, if the customer asks for 7 stones and 3 pens, the items list should have ['stone', 'stone', 'stone', 'stone', 'stone', 'stone', 'stone', 'pen', 'pen', 'pen']. Make sure to print all items with their full name in lowercase. Use the format: 'ORDER [{{items}}] DONE' to print all the items. For example, if the customer asks for 2 Silver swords and 1 Potion, output ORDER ['silver sword', 'sword', 'potion'] DONE"