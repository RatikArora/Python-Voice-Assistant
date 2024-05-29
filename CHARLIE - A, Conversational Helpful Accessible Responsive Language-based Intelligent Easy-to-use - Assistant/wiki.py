import wikipedia  

def wiki(text):
    wiki = wikipedia.summary(text, sentences=4) 
    return wiki 

# print(wiki())