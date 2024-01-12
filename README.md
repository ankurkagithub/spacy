# Natural Language Processing (NLP) using Spacy

# Project Description
A program with preloaded garden path sentence data to carry out entity recognition using the NLP Spacy library.
More details on garden-path sentences can be found here: https://en.wikipedia.org/wiki/Garden-path_sentence

# Table of Content
1. Installation
1. Usage
1. Credits

# 1. Installation
1. Download or fork the "garden.py" file in a local folder of your
computer.
2. Use your terminal > Navigate to the directory where the file is saved
3. Enter "python garden.py" to run the program

# 2. Usage
After running the program, once you have opened the terminal window, you will
see the breakdown of undertaken N on the sentence.
as below.
![Option 1](/pictures/output.png)
NLP input: Sentence input
Tokenise: Converted each word into a token.
Stop-word: Identifying stop-words ie most commonly used words in language. Ideally, these should be removed before proceeding with NLP steps. However, they are kept in for demostrating purposes from lemmantising.
Lemmantising: Combining words with the same origin into one. For eg here a stop-word "is" replaced by "be". Please note in the real model, we remove stop words before this step.
Entity recognition: Labelling data based on Spacy model entity recognition.

# 3. Credits
This project was completed by me -  Ankur Kaushal, as part of Software Engineering
Bootcamp under the supervision of HyperionDrive.
