# Prompt Engineering Process

### Step 1
#### Intention
For the first iteration, I wanted to setup up an llm agent and test if it works.

#### Action/Change
I used llama3.2 and setup 2 hyperparameters (temperature and max-tokens). I then initialized the message history with a system prompt that explains the role of the agent. I also added another message with a user role, asking the agent to start a DnD game. I also modified the game loop from the demo_lab to fit the correct order of response generation and user input retrieval.

#### Result
The llm agent was able to generate a story and prompt the user to select from multiple options to progress through the game.

#### Reflection/Analysis of the result. 
It was important to define the agent to start the game in the initialzation of messages using a user message instead of prompting the agent within system prompt to make sure the game loop starts off with the agent automatically creating a story and starting a DnD game. I understood that some models may or may not generate a response based on a system prompt.