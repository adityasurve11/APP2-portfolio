import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/aditya1.jpg")

with col2:
    st.title("Aditya Surve")
    content = """
    Artificial Intelligence and Machine Learning graduate with a strong foundation in Cybersecurity,
    managing security risks, networks and network security using Linux, SQL and tools like tcpdump,
    Wireshark, SIEM tools and to manage and determine Assets, Threats, and Vulnerabilities by detecting 
    and responding using Python to automate Cybersecurity tasks. 
    In my journey to become a skilled Cybersecurity Analyst, I leverage my passion for the industry to 
    fuel continuous learning and development.
    I am eager to contribute my skills and knowledge to a cybersecurity role, mitigating threats and 
    safeguarding your organization.
    """
    st.info(content)

content2 = """
Below you can find some of the apps I have built in Python. Feel free to contact me! 
"""
st.write(content2)

col3, col4 = st.columns(2)

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row['title'])

with col4:
    for index, row in df[10:].iterrows():
        st.header(row['title'])
