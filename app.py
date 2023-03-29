import streamlit as st
import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt
import altair as alt
st.title("Welcome to my profile ") 

#st.header("Hi I")
#st.subheader("subheader")

st.text("Hi I am Hritick Lohani and this web page is my profile")

st.image("hritick_crop-modified.png", width= 200)


rad = st.sidebar.radio("Navigation", ["About", "Experience", "My school", "skills", "Courses"])
#df1 = pd.DataFrame(data= data)
if rad == "About":
    st.markdown('''_I am a final Year UG pursuing a B. Tech. in Instrumentation and Control Engineering from the National Institute of Technology, Jalandhar, and a Diploma in data science from IIT Madras. Building strategies and formulating solutions are what excite me. I believe in proactive approaches to solving problems and look forward to opportunities that provide a steep and aggressive learning curve. I always look forward to learning new technologies_ <br> <br>''', True)
    
    st.markdown(''' check out my [ LinkedIn ](https://www.linkedin.com/in/hritick-lohani-26b0311b4/) <br>
    check out my [ Github ](https://www.github.com/HL7988)''', True)

if rad == "Experience":
    st.markdown(""" ### DeepSight AI Labs: <br>
    Role : Computer Vision Software Intern <br>
    Location : Gurgaon <br>
    Starting date : 09-sept-2022 <br>
    """, True)
    if st.checkbox("Show discription of Deepsight"):
        st.write("in process")
    st.markdown(""" ### DRDO-IRDE: <br>
    Role : Project Intern <br>
    Location : Dehradun <br>
    Starting date : 12-june-2022 <br>
    Ending date : 30 july 2022 <br>
    """, True)
    if st.checkbox("Show discription of DRDO "):
        st.write("in process")
    
    st.markdown(""" ### Institute for Sustainable Technology (IEEE): <br>
    Role : ResearchIntern <br>
    Location : Radom, Poland <br>
    Starting date : 1-Jan-2021 <br>
    Ending date : 30 march 2022 <br>
    """, True)

    if st.checkbox("Show discription of IEEE"):
        st.write("in process")
    st.markdown(""" ### BHEL: <br>
    Role : Training <br>
    Location : Haridwar (Ranipur) <br>
    Starting date : 5-Dec-2021 <br>
    Ending date : 5 Jan 2022 <br>
    """, True)

    if st.checkbox("Show discription of BHEL"):
        st.write("in process")
    
    
if rad == "My school":
    st.markdown(""" # Education """)
    d= { "college" :{"Degree" : "Bachelor of Technology", "Stream": "Instrumentation and control", "city" : " Jalandhar "},
        "Itermediate": {"Degree" : "12th", "stream" : "science", "city" : "gaya"},
        "Secondary school" : {"Degree" : "10th", "Board" : "CBSE", "City" : "gaya"}}
    my_school = pd.DataFrame({
        'Education' : ['NIT JALANDHAR', 'HANSRAJ PUBLIC SCHOOL, GAYA , BIHAR', 'DAV PUBLIC SCHOOL CANTT AREA GAYA'],
        'lat' : [31.3959, 24.7322, 24.7387],
        'lon' : [75.5358, 84.9627, 84.9658]})
    st.write(d)
    if st.button(" Locate my school"):
        st.map(my_school)
