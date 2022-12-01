'''
Perplexity calculation for PFG Dataset with evaluate library from huggingface
'''

import pandas as pd
import evaluate
perplexity = evaluate.load("perplexity", module_type="metric")

# Fetch the persuader lines for the perplexity computation
df = pd.read_excel('300_dialog.xlsx', index_col=0, header=None)

persuader_lines = df[df[2] == 0]

_dict = {}
for idx, row in persuader_lines.iterrows():
    if str(row[1]) not in _dict:
        _dict[str(row[1])] = []

    _dict[str(row[1])].append(str(row[4]).rstrip())

input_texts = []
for key, val in _dict.items():
    input_texts.append(val)

# Calculate perplexity scores of the persauder conversations from PFG Dataset
with open("perplexity_dataset.txt", "w") as file_obj:

    for inputs in input_texts:
        results = perplexity.compute(predictions=inputs, model_id='gpt2')

        #print (results)
        #print (round(results["mean_perplexity"], 2))
        file_obj.write("{} {}".format(str(round(results["mean_perplexity"], 2)), len(inputs)))
        file_obj.write("\n")