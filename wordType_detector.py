# import required modules
import spacy

"""
Spacy token.pos_ :
    ADJ: adjective
    ADP: adposition
    ADV: adverb
    AUX: auxiliary
    CCONJ: coordinating conjunction
    DET: determiner
    INTJ: interjection
    NOUN: noun
    NUM: numeral
    PART: particle
    PRON: pronoun
    PROPN: proper noun
    PUNCT: punctuation
    SCONJ: subordinating conjunction
    SYM: symbol
    VERB: verb
    X: other
"""
def noun_detector(text, lang):
    nlp = spacy.load("es_core_news_sm") if lang == "es" else spacy.load("en_core_web_sm")

    # returns a document of object
    doc = nlp(text)

    # checking if it is a noun or not
    for word in doc:
        if (word.pos_ == 'NOUN'):
            print(word, " is a noun.")
        else:
            print(word, " is not a noun.")

def adjective_detector(text, lang):
    nlp = spacy.load("es_core_news_sm") if lang == "es" else spacy.load("en_core_web_sm")

    # returns a document of object
    doc = nlp(text)

    # checking if it is a noun or not
    for word in doc:
        if (word.pos_ == 'ADJ'):
            print(word, " is an adjective.")
        else:
            print(word, " is not an adjective.")


#noun_detector_en("Bad written house")
noun_detector("Una casa bonita", lang='es')
adjective_detector("Una casa bonita", lang='es')