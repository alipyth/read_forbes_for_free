#pip install streamlit
#pip install requests
#pip install selectolax



import databutton as db
import streamlit as st
import requests
from selectolax.parser import HTMLParser
st.title('read Not Free forbes articles for free :)')

#r = 'https://fortune.com/crypto/2023/09/01/uniswap-class-action-dismissal-coinbase-tornado-cash-implications/'

r = st.text_input('paste the url of forbes article')
st.info('By Ali Jahani https://jahaniwww.com')
sub = st.button('read :)')
if r is not None and sub :
    rr = requests.get(r)
    #articleContent
    parser = HTMLParser(rr.content)
    
    p= parser.css_first('.article-body')
    links = []
    images = []

    st.write(p.text())
