#dictionary.py
#Note: run command in terminal first, 'pip install nltk'

import nltk 
nltk.download('wordnet')
nltk.download('omw-1.4')  # For multilingual wordnet
from nltk.corpus import wordnet 

def get_word_info(word):
    # Get synsets
    synsets = wordnet.synsets(word)
    
    if not synsets:
        return {
            "definition": "No definition found.",
            "synonyms": "No synonyms found.",
            "related_words": "No related words found."
        }
    
    # Get definitions
    definitions = [synset.definition() for synset in synsets]
    
    # Get synonyms
    synonyms = set()
    for synset in synsets:
        synonyms.update(lemma.name() for lemma in synset.lemmas())
    
    # Get related words (hypernyms and hyponyms)
    related_words = set()
    for synset in synsets:
        for hypernym in synset.hypernyms():
            related_words.update(lemma.name() for lemma in hypernym.lemmas())
        for hyponym in synset.hyponyms():
            related_words.update(lemma.name() for lemma in hyponym.lemmas())
    
    return {
        "definition": definitions[0] if definitions else "No definition found.",
        "synonyms": ', '.join(synonyms) if synonyms else "No synonyms found.",
        "related_words": ', '.join(related_words) if related_words else "No related words found."
    }

# Example usage
word = input("Enter a word: ")
info = get_word_info(word)

print(f"Definition: {info['definition']}")
print(f"Synonyms: {info['synonyms']}")
print(f"Related Words: {info['related_words']}")
