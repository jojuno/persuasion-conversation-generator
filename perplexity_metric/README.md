References for the usage of Perplexity metric:

[Perplexity of fixed-length models](https://huggingface.co/transformers/v4.6.0/perplexity.html)

Execution steps:

1) Run readconvos.py to generate persuadee and persuader dialogue files from conversations generated from Model A and B
2) Run perplexity.py to get mean perplexity scores for persuader dialogues from Model A generated conversations
3) Run perplexity_dataset.py to fetch mean perplexity scores for persuader dialogues from PFG dataset 
