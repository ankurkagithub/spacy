# Title - Natural Language Processing (NLP) using Spacy

# Project Description
A program with preloaded garden path sentence data to carry out entity recognistion using NLP Spacy library.
More details on garden-path sentences can be found here: https://en.wikipedia.org/wiki/Garden-path_sentence

# Table of Content
1. Installation
1. Usage
1. Credits

# 1. Installation
1. Download or fork "garden.py" file in a local folder of your
computer.
1. Run this file in your chosen IDE and press on run button to execute
1. Alternatively after step 1,
    1. use your terminal > Navigate to directory where file is saved
    1. enter "python garden.py" to run the program

# 2. Usage
After running the program, once you have open the terminal window, you will
see the breakdown of undertaken N on the sentence.
as below.
![Option 1](/pictures/output.png)
NLP input: Sentence input
Tokenise: Converted each word into a token.
Stop-word: Identifying stop-words ie most common used words in language.Ideally these should be removed before preceeding with NLP steps. However they are kept in for demostrating purposes from lemmantising.
Lemmantising: Combining words with same origin into one. For eg here a stop-word "is" replaced by "be". Please note in real model, we remove stop words prior to this step.
Entity recoginistion: Labelling data based on Spacy model entity recoginistion.

# 3. Credits
This project was completed by me -  Ankur Kaushal, as part of Software Engineering
Bootcamp under the supervison of HyperionDrive.
