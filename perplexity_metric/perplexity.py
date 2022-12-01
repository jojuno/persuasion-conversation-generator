'''
Perplexity calculation for Model A generated conversations with evaluate library from huggingface
'''

import evaluate
perplexity = evaluate.load("perplexity", module_type="metric")

# Fetch the persuader lines for the perplexity computation
input_texts = []
with open("persuader_convo.txt", "r") as file_obj:
    start = 0
    lines_list = file_obj.readlines()
    for idx, line in enumerate(lines_list):
        if line == "\n":
            input_texts.append(lines_list[start:idx])
            start = idx + 1

    for lst in input_texts:
        for idx, _ in enumerate(lst):
            lst[idx] = lst[idx].rstrip()

# Calculate perplexity scores of the persauder conversations generated from Model A
with open("perplexity_persuader_convo.txt", "w") as file_obj:

    for inputs in input_texts:
        results = perplexity.compute(predictions=inputs, model_id='gpt2')

        for result in results["perplexities"]:
            file_obj.write(str(result))
            file_obj.write("\n")

        file_obj.write('\n')
        #print (results)
        #print (round(results["mean_perplexity"], 2))
        file_obj.write("{} {}".format(str(round(results["mean_perplexity"], 2)), len(inputs)))
        file_obj.write("\n")