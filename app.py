import streamlit as st


# NLP PKGS
import spacy
from textblob import TextBlob

def text_analyzer (my_text):
    print(my_text)
    nlp = spacy.load('en_core_web_sm')
    docx = nlp(my_text)

    tokens = [token.text for token in docx]
    allData = [('"Tokens":{},\n"Lemma":{}'.format(token.text,token.lemma_))for token in docx]
    return allData


def entity_analyzer (my_text):
    print(my_text)
    nlp = spacy.load('en_core_web_sm')
    docx = nlp(my_text)
    tokens = [token.text for token in docx]
    entities = [(entity.text, entity.label_) for entity in docx.ents ]
    return entities
# PKGS


def main():
    """NLP App With Streamlit """
    st.title("NLPiffy with streamlit")
    st.subheader("Natural Language Processing on the go")

    # Tokenization
    if st.checkbox("Show Tokens and Lemma"):
       st.subheader("Tokenize Your Text")
       message = st.text_area("Enter Your Text","Type Here", key='text')
       if st.button("Analyze"):
            nlp_result = text_analyzer(message)
            st.json(nlp_result)



    # Names Entity
       if st.checkbox("Show Named Entites"):
        st.subheader("Extract Entites from Your Text")
        message = st.text_area("Enter Your Text","Type Here", key='entity')
        if st.button("Extract"):
            nlp_result = entity_analyzer(message)
            st.json(nlp_result)

    # Sentiment Analysis

    # Text Summarization



if __name__ == '__main__':
     main()