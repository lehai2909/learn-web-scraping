import streamlit as st
import numpy as np
import pandas as pd 


st.title('Haigle')
st.write("Here's my first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))



#line chart
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)



#Checkbox
if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    st.line_chart(chart_data)



from datetime import datetime
start_time = st.slider(
     "When do you start?",
     value=datetime(2020, 1, 1, 9, 30),
     format="MM/DD/YY - hh:mm")
st.write("Start time:", start_time)


#text input
title = st.text_input('Movie Title','Life of Brian')
st.write('Title of the movie: ',title)

st.text_area('Result','''
Hello, My name is LH
I can help you with time travel
Trust me :)
''')





col1, col2, col3 = st.beta_columns(3)

with col1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg")


from PIL import Image
import requests
from io import BytesIO

url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/57/Li6-D_Reaction.svg/600px-Li6-D_Reaction.svg.png'
response = requests.get(url)
img = Image.open(BytesIO(response.content))
st.image(img, caption='Nuclear reaction (Wikipedia)')
