# Natural Language Processing using SpaCy.

import spacy #importing spacy

nlp = spacy.load('en_core_web_sm')

gardenpathSentences = []
#Sentence 1
gardenpathSentences.append("Helen is expecting tomorrow to be a bad day.")
#Sentence 2
gardenpathSentences.append("The man who whistles tunes pianos.")
#Sentence 3
gardenpathSentences.append("Mary gave the child the dog bit a Band-Aid.")
#Sentence 4
gardenpathSentences.append("The cotton clothing is made of grows in Mississippi.")
#Sentence 5
gardenpathSentences.append("That Jill is never here hurts.")

for sentence in gardenpathSentences:
    doc = nlp(sentence)
    print("Sentence: ", sentence)
    print("NLP DOP: ", doc)

    # Tokenisation without punctuation or whitespace
    output = [(token, token.orth_, token.orth) for token in doc if not \
              token.is_punct | token.is_space]
    print("Output: ", output)
    # Stopwords
    stop_words = [word for word in doc if word.is_stop == True]
    print("Stop Word: ",stop_words)

    #Lemmantising
    lemmant = [word.lemma_ for word in doc]
    print("Lemmant: ",lemmant)

    # Entity recognition
    entity = [[(i, i.label_, i.label) for i in doc.ents]]
    print("Entity:", entity)

    print("")

# Comments on Entity
#1. In sentence 1, "tomorrow" and "day" are recognised as "dates".
#2. In sentence 3 and 5, "Mary" and "Jill" are correctly recognised a "Person" entity
#3. In sentence 4, "Mississippi" is "GPE" entity
#4. No entities were understood for sentence 2.
# General Observation - Garden sentences were used, which are hard to
# understand especially for computers, as general grammar rules are not followed.
# Hence the accurate meaning is challenging to deduce using Entity recognition.
