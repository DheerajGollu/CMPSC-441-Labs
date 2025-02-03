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



### Step 2
#### Intention
For the second iteration, I did not focus on any improvements. Instead, I wanted to check if the llm agent performed as well as the first iteration and see if the gameplay might differ.

#### Action/Change
I think testing the llm agent again will provide insight into how well my initial prompt was. Moreover, it will give me an idea of whether the llm agent is able to provide a unique story experience for every new game.

#### Result
The llm agent did not create a new story for the second iteration. The story title, supporting character names, and initial options were almost the same. However, the agent is at least working as expected.

#### Reflection/Analysis of the result. 
I think the reason why the story did not change much is because the training data that is related to DnD was limited for the llama3.2 model. Moreover, I did not specify the agent to create a new and interesting story for every game in the first system prompt.



### Step 3
#### Intention
For the third iteration, I intended to improve the creativity and uniquness of the story for every new game.

#### Action/Change
I first changed the temperature of the model from 1.0 to 1.5 to make it provide more creative/random output. Then, I updated the system prompt by asking the agent to provide a new plot and characters for every game. I expected that explicitly prompting the agent to generate unique stories would help me achieve the desired result.

#### Result
The agent was able to generate a unique story that was different from the previous attempts. However, although the character descriptions changed slighlty, the names did not differ at all. I think I should clearly prompt the agent to change character names as well.

#### Reflection/Analysis of the result. 
I realized that being explicit with prompts and using the right words is important. Although I mentioned that new characters should be generated, the names of the characters did not change at all. Although I increased the temperature by 0.5, I did not see a noticeable difference in the agent's output.



### Step 4
#### Intention
For this step, I wished to improve the formatting of the agent's output, make sure new character names are generated for every game, and reduce repetition of words.

#### Action/Change
I increased temperature again by 0.5 and max_tokens to 500, and I also included the repition_penalty hyperparemeter that I set to 1.2 to reduce repetition of text. I also mentioned in the system prompt that the agent should format the text with aesthetic spacing.

#### Result
I was satisfied with the fact that each story for every new game is unique. Moreover, this time, character names differed from the last attempt. Additionally, I liked the formatting of the text, as bullet lists were introduced. Surprisingly, the agent now has started to describe the equipment of each character, which I think is a nice addition. I also noticed fewer repetition of words, which is also a preferrable outcome. However, after selecting an option in the game, there was no second option list to continue the game, which might have been caused by a low token limit. Surprisingly, I also noticed some issues with grammar. For instance, the agent said the following: "You are adventurers seeking fortune ..." and "You are four brave adventurers: ... ."  

#### Reflection/Analysis of the result. 
Instead of prompting the agent to reduce repition, it seems like changing the repition_penalty hyperparameter works well. Additionally, increasing the temperature by more has definitely improved the story plot and descriptions. However, more randomness and constraints on repetitive text might have limited the agent in making concise descriptions that come under the token_limit. I was also pleased with the formatting of text after prompting the agent to make the text visually organized and aesthetic. ALso, I am not sure why there is an issue with grammar, but it might be worth trying to prompt the agent to check for proper grammar.



### Step 5
#### Intention
For this iteration, I wished to ensure proper grammar was enforced, descriptions were concise, and the gameplay continued without stopping due to token limits.

#### Action/Change
I increased the max_tokens to 1000 to ensure that the agent does not stop gameplay due to reaching low token limits. Moreover, I added a second system prompt message, asking the agent to keep descriptions concise and grammatically correct. I added a second system prompt because the first system prompt was getting verbose. I assumed that having a second system prompt should work the same as having just one big system prompt.

#### Result
The recorded attempt did not change the grammar mistakes mentioned in the previous attempt. Additionally, I felt that the spacing and text format slightly deteriorated. However, descriptions were concise, and there was no problem with gameplay. 

#### Reflection/Analysis of the result. 
I think having a second system prompt may or may not work everytime. Some of the features I liked from the previous attempt were not consistent in this one. However, there was another attempt before that was not recorded, and that attempt satisfied what I was expecting. Therefore, I think the problem might be having a second system prompt because the model is not performing consistently. Another reason might just be the relative small size of the llama3.2 model. I feel that using a larger model will make a difference.