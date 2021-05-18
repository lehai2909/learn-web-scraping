import streamlit as st
import numpy as np
import pandas as pd 
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

#Set title for my page
st.title("HaiHai")

#Why you will (probably need this page)
st.header("I will help simplify your search with Wiki URL")

#Define where to input Wiki URL
query = st.text_input('Wiki URL')

if st.button('Travel'):
    col1, col2, col3 = st.beta_columns([1,0.5,4])
    html = urlopen(query)
    
    # Use Beautiful Soup library to parse Wiki page
    bs = BeautifulSoup(html, 'html.parser')
    with col3: 
        result =''

    # Try to find all paragraph at the introduction of the page, the most overall information
        try:  
            if bs.find('p').attrs['class']:
                intro = bs.find('p').find_next('p')
        except KeyError:
            intro = bs.find('p')
        while (intro != '\n'):
            result = result + intro.get_text() + '\n'
            intro = intro.next_sibling
        st.text_area('Result',result, height = 500)

    # Collect the introductory picture and save it to 'image' folder
    with col1:
        image_url = 'https:'+bs.find('a', href = re.compile('^(/wiki/File)')).find('img').attrs['src']
        img_data = requests.get(image_url).content
        st.image(img_data, caption='Nuclear reaction (Wikipedia)')
        with open('image\image.png', 'wb') as handler:
            handler.write(img_data)