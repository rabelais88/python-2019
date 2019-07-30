import spacy
nlp = spacy.load("kr_core_web_sm")
doc = nlp("우리 집엔 강아지가 있다")
