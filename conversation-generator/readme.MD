# version 2

model A is trained on data of the form: 
```
    <|startoftext|>Good morning. How are you doing today?<|endoftext|>
    Hi. I am doing good. How about you?<|endoftext|>
    <|persuader|>I'm doing pretty good for a Tuesday morning. <|endoftext|>
    Haha. Same here, but it really feels like a Monday.<|endoftext|>
    <|persuader|>Ugh yes it does!<|endoftext|>
    I can not believe how warm it is already.<|endoftext|>
    <|persuader|>Where are you from? <|endoftext|>
    I am from the Midwest. What about you?<|endoftext|>
    <|persuader|>I'm from the South East. It's always warm here. <|endoftext|>
    Oh, yep. You are definitely in for warm weather, which is great as far as I am concerned.<|endoftext|>
    <|persuader|>We're about to get hit by a tropical storm.<|endoftext|>
    I heard that some bad weather was going to be coming. I hope it is not too severe.<|endoftext|>
    <|persuader|>Me too. It's just part of living on the Gulf. You have to be prepared for it.<|endoftext|>
    Yes, I am sure you get a lot of storms.<|endoftext|>
    <|persuader|>We do. I guess I should get into what this chat is supposed to be about. Have you heard of the Charity Save The Children?<|endoftext|>
    I have heard about them. What do you like about them?<|endoftext|>
    <|persuader|>I like that they're committed to helping children in need. They're very transparent in their work and do great things to help children in underprivileged countries. <|endoftext|>
    Yes, I also like what they do. They are a great organization.<|endoftext|>
    <|persuader|>I'm planning on donating most of my earnings today. Would you like to donate as well?<|endoftext|>
    I would like to dotate $0.20. Would that help?<|endoftext|>
    <|persuader|>Yes it would. Any little bit helps. Thank you for your donation!<|endoftext|>
```

model B is the general conversational model (HF: facebook/blenderbot-3B)