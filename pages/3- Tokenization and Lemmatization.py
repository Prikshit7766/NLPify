# Function to Analyse Tokens and Lemma
# Core Pkgs
import streamlit as st 
import os


# NLP Pkgs
from textblob import TextBlob 
import spacy
from gensim.summarization import summarize

# Sumy Summary Pkg
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
html_temp = """
<div style ="background-color:yellow;padding:13px">
<h1 style ="color:black;text-align:center;"> NLPify !📔 </h1>
</div>
"""
st.markdown(html_temp, unsafe_allow_html = True)
@st.cache
def text_analyzer(my_text):
	nlp = spacy.blank('en')
	docx = nlp(my_text)
	# tokens = [ token.text for token in docx]
	allData = [('"Token":{},\n"Lemma":{}'.format(token.text,token.lemma_))for token in docx ]
	return allData

def main():
    	# Title
	st.subheader("Tokenization and Lemmatization")
	st.markdown("""
    	**Tokenization** - Tokenization is the process of breaking up text into text units 
        (words, sentences or phrases, symbols, or some other meaningful element).
        Before natural language processing, you need to define the words that make up the character string.  
    	""")
	st.markdown("""**Lemmatizaton** : Lemmatization, on the other hand, takes into consideration the 
				morphological analysis of the words. To do so, it is necessary to have detailed dictionaries
				which the algorithm can look through to link the form back to its lemma. Again, you can see
				how it works with the same example words.""")
	# Tokenization
	if st.checkbox("Show Tokens and Lemma"):
		st.subheader("Tokenize Your Text")

		message = st.text_area("Enter Text","Type Here ..")
		if st.button("Analyze"):
			nlp_result = text_analyzer(message)
			st.json(nlp_result)
st.sidebar.subheader("About App")
st.sidebar.text("NLPify App with Streamlit")


st.sidebar.subheader("By")
st.sidebar.text("Rakshit Khajuria - 19bec109")
st.sidebar.text("Prikshit Sharma - 19bec062")
st.sidebar.text("Angat Datta - 19bec010")
st.sidebar.text("Bhargav Chalotra - 19bec019")


if __name__ == '__main__':
	main()
