import evaluate
perplexity = evaluate.load("perplexity", module_type="metric")

# Fetch persuadee and persuader lines from the conversations generated from Model A and B
input_texts = []
with open("conversation.txt", "r") as file_obj:
    start = 0
    lines_list = file_obj.readlines()
    for idx, line in enumerate(lines_list):
        if line == "\n":
            input_texts.append(lines_list[start:idx])
            start = idx + 1

    for lst in input_texts:
        for idx, _ in enumerate(lst):
            lst[idx] = lst[idx].strip()

#print (input_texts)


# Write the conversations to individual files
persuader_lines = []
persuadee_lines = []

for convo in input_texts:
    persuader = []
    persuadee = []

    for line in convo:

        if line[0] == "A":
            line_stripped = str(line[2:]).strip()
            persuader.append(line_stripped)

        elif line[0] == "B":
            line_stripped = str(line[2:]).strip()
            persuadee.append(line_stripped)

    persuader_lines.append(persuader)
    persuadee_lines.append(persuadee)

with open("persuader_convo.txt", "w") as file_obj:

    for persuader in persuader_lines:
        for line in persuader:
            file_obj.write(str(line).strip())
            file_obj.write("\n")
        file_obj.write("\n")

with open("persuadee_convo.txt", "w") as file_obj:

    for persuadee in persuadee_lines:
        for line in persuadee:
            file_obj.write(str(line).strip())
            file_obj.write("\n")

        file_obj.write("\n")