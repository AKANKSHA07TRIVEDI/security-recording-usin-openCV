from numpy import complex128
import streamlit as st
from recorder import recordVideo
import json


st.title("SECURITY RECORDING USING OPENCV")
st.image('hero.jpg', use_column_width=True)
sidebar = st.sidebar
config = {}
try:
    with open('settings.json', 'r') as f:
        config = json.load(f)
except Exception as e:
    print(e)
    st.error('Error Loading Settings')
sidebar.title('User Options')


def introduction():
    st.title("COMPUTER VISION ")
    st.markdown("""
     As computer vision has become a part of our daily life.
      Using smartphones features like face recognition is all a part of computer vision. 
      In this paper, we will talk aboutCV or Computer Vision which is preferably used to
       read and display a video stream in real time through which one can access the web camera
        and using machine learning one can let their system learn through data sent by user or 
        through datasets which is easily available on the internet and then system trains itself. After training part it is ready to solve the real life problems
        
    """)
    st.image('cv.jpg', use_column_width=True)
    
    
    st.title("OPENCV")
    st.markdown("""
    As computer vision has become a part of our daily life.
      Using smartphones features like face recognition is all a part of computer vision. 
      In this paper, we will talk aboutCV or Computer Vision which is preferably used to
       read and display a video stream in real time through which one can access the web camera
        and using machine learning one can let their system learn through data sent by user or 
        through datasets which is easily available on the internet and then system trains itself. After training part it is ready to solve the real life problems
        
    """)

    
    st.image('opencv.jpg', use_column_width=True)
    st.image_size=(300,300)
    c1, c2 = st.columns(2)

    c1.header("FEATURE")
   
    st.markdown("""2.Fast Speed. Since the OpenCV library is originally written in C/C++, it is fast and efficient.
                   
    """)
    st.markdown("""3.Easy to Integrate. 
                   """)
    st.markdown("""4.Read and write images.""")

def execute():
    st.subheader('project working here')
    st.title("security recorder")
    video_name = st.text_input("Enter video name")
    record = st.checkbox('Record Video')
    if video_name and record:
        recordVideo(video_name, config)
        sidebar = st.sidebar
    st.title("USAGE")
    st.markdown("""Peace of mind.
    """)
    st.markdown("""Deterrent and crime prevention.
    """)
    st.markdown("""
    Prosecution.
    """)
def setting():
    st.title("OPTION")
    c1, c2, c3 = st.columns(3)

    height = c1.text_input("Hight")

    width = c2.text_input("width")
    
      

    fps = c3.text_input("fps")

    save_btn = st.button('Save Settings')

    if save_btn:
        with open('settings.json', 'r') as f:
            config = json.load(f)
            config = {"width": width, "height": height, "fps": fps}

            with open('settings.json', 'w') as f:
                json.dump(config, f)
            st.success('Settings Saved...')


print(config)

options = ['Project Introduction','Execution','setting']
selOption = sidebar.selectbox("Select an Option", options)

if selOption == options[0]:
    introduction()
elif selOption == options[1]:
    execute()
elif selOption == options[2]:
    setting()



