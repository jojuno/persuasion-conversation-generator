# need to have modelA (gpt) and modelB (requests library) "talk" to each other 

import gpt_2.src.interactive_conditional_samples as A
import modelB as B

NUM_TURNS = 5
NUM_CONVERSATIONS = 10

def process_model_B(input): # model B requires specific input format, so this just takes care of that 
    return {
        'generated_responses': conversation['B'],
        'past_user_inputs': conversation['A'], 
        'text': input
    }

A_resp = A.interact_model('<|startoftext|>') # start token to get persuader line 
A_file = open('persuader.txt', 'w+')
B_file = open('persuadee.txt', 'w+')
conv_file = open('conversations.txt', 'a')

conversation = {'A': [], 'B': []} # storing the entire conversation in each ordered list per model 

feed_to_B =  process_model_B(A_resp) # get the input for model B
conversation['A'].append(A_resp) # store the persuader line
    # this MUST be done after getting the input for model B (#19) bc we don't want to feed this line into model B as past conversation history

for _ in range(NUM_TURNS):
    B_resp = B.feed(feed_to_B) # get response from model B
    conversation['B'].append(B_resp) # store response in conversation

    A_resp = A.interact_model(B_resp + '<|persuader|>') # get response from model A 
        # <|persuader|> token used bc we train model A on ALL lines w/ persuader lines starting w/ token; we want to 'complete' the utterance starting w/ given token 
    conversation['A'].append(A_resp) # store response in conversation
        
    feed_to_B = process_model_B(A_resp) # get the formatted input for model B

print('A:', conversation['A'][0] + '\n') # A has one extra line bc we get the first line w/ the <|startoftext|> token (#15, appended at #20)
A_file.write(conversation['A'][0] + '\n')
conv_file.write('A:' + conversation['A'][0] + '\n')

for i in range(NUM_TURNS):
    print('B:', conversation['B'][i])
    print('A:', conversation['A'][i+1])
    B_file.write(conversation['B'][i] + '\n')
    A_file.write(conversation['A'][i+1] + '\n')
    conv_file.write('B:' + conversation['B'][i] + '\n')
    conv_file.write('A:' + conversation['A'][i+1] + '\n')

A_file.write('\n')
B_file.write('\n')
conv_file.write('\n')

A_file.close()
B_file.close()
conv_file.close()

# write the full conversation to separate files (persuader.txt & persuadee.txt)