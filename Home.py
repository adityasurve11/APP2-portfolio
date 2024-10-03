import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/aditya1.jpg")

with col2:
    st.title("Aditya Surve")
    content = """ 
    In my journey to become a skilled Cybersecurity Analyst, 
    I'm deeply committed to advancing my skills in cybersecurity, dedicating myself to studying and practicing every day.
    """
    st.info(content)

content2 = """
Below you can find some of the apps I have built in Python. Feel free to contact me!
(In progress!) 
"""
st.write(content2)

col3, empty_col, col4 = st.columns([2.2, 0.3, 2.2])

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:11].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image("images/" + row["image"])
        st.write(f"[App-URL]{row['url']}")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image("images/" + row["image"])
        st.write(f"[Source code]({row['url']}")
