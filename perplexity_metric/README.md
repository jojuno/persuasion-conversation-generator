References for the usage of Perplexity metric:

[Perplexity of fixed-length models](https://huggingface.co/transformers/v4.6.0/perplexity.html)

Execution steps:

1) Run ***readconvos.py*** to generate persuadee and persuader dialogue files for conversations generated from Model A and B (*conversations.txt*)
2) Run ***perplexity.py*** to calculate mean perplexity scores for persuader dialogues from Step 1
3) Run ***perplexity_dataset.py*** to calculate mean perplexity scores for persuader dialogues from PFG dataset (*300_dialog.xlsx*)
