import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as html
from  PIL import Image
import numpy as np
import pandas as pd
import io 
from keras.models import model_from_json
from pathlib import Path
from tensorflow.keras.preprocessing import image
import numpy as np
from keras.applications import vgg16
import requests 
import base64
import openpyxl



css = '''
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap" rel="stylesheet">
<style>
   h1 {
      font-size: 36px;
      text-align: center;
      font-family: "Outfit", sans-serif;
   }
</style>
'''


st.markdown(css, unsafe_allow_html=True)




with st.sidebar:
    choose = option_menu("KYI", ["Home Page" , "About Us", "Image Classification", "Search Bar", "Contact Us"],
                         icons=['house','kanban','camera fill', 'book','person lines fill'],
                         menu_icon="app-indicator", default_index=0,
                         styles={
        "container": {"padding": "5!important", "background-color": "#fafafa"},
        "icon": {"color": "orange", "font-size": "25px"}, 
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#02ab21"},
    }
    )

if choose == "Home Page" :
    #st.set_page_config(layout="wide")
       
    

    col1, col2 = st.columns([1,3])
    with col2:
        st.title("Welcome to KYI 🎉!")
    with col1:
        col11, col22, col33 = st.columns(3)
        with col33:
            st.image("Logo.jpg",width=100)
    st.subheader("Know Your Insect 🐜🇹🇭!")
    st.balloons()
    st.info(("    Glad to be assisting you today,  feel free to browse our menu")
            )
    st.toast("Lets get started 🏁 ")
    st.toast("welcome to our web-based application!📚")  
    col1, col2, col3 ,col4 ,col5 = st.columns(5)
    with col2:
        st.image("Insect.jpg")

    with col3:
        st.image("robot.jpg",width=175)
if choose == "About Us" :
    st.title('About Us')
    css = '''
    <link href="https://fonts.googleapis.com/css2?family=Niramit:ital,wght@0,200;0,300;0,400;0,500;0,600;0,700;1,200;1,300;1,400;1,500;1,600;1,700&family=Outfit:wght@100..900&display=swap" rel="stylesheet">
    <p style="color:Black; font-size: 20px; font-family:Niramit;">แนะนำสมาชิกในกลุ่ม</p>
    '''
    st.markdown(css, unsafe_allow_html=True)


    st.image("aoon.jpg",width=300, caption="ด.ญ. กานต์ปภา ประจิตร์ ม.2/3 เลขที่ 21 (หัวหน้ากลุ่ม)")
    st.image("placeholder.jpg",width=300, caption="ด.ญ. ชนันธร มามีชัย ม.2/3 เลขที่ 23")
    st.image("miu.jpg",width=300,caption="ด.ญ. ฐิตามร กณิกนันต์ ม.2/3 เลขที่ 24")






if choose == 'Image Classification' :
    st.title('Image Classification')
    
    css = '''
    <link href="https://fonts.googleapis.com/css2?family=Niramit:ital,wght@0,200;0,300;0,400;0,500;0,600;0,700;1,200;1,300;1,400;1,500;1,600;1,700&family=Outfit:wght@100..900&display=swap" rel="stylesheet">
    <p style="color:Black; font-size: 20px; font-family:Niramit;">กรอกข้อมูลผู้ใช้</p>
    '''
    st.markdown(css, unsafe_allow_html=True)


    first = st.text_input("First name")
    last = st.text_input("Last name")
    age = st.slider("Age", 0, 100)
    city = st.selectbox("city", ["Chiang Mai","Chiang Rai","Lampang","Lamphun", "Mae Hong Son","Nan","Phayao","Phrae","Uttaradit","Kalasin","Khon Kaen","Chaiyaphum", "Nakhon Phanom","Nakhon Ratchasima","Bueng Kan", "Buriram", "Maha Sarakham","Mukdahan", "Yasothon","Roi Et","Loei","Sakon Nakhon","Surin","Sisaket","Nong Khai","Nong Bua Lamphu","Udon Thani","Ubon Ratchathani","Amnat Charoen", "Bangkok","Kamphaeng Phet","Chai Nat","Nakhon Nayok","Nakhon Pathom","Nakhon Sawan","Nonthaburi", "Pathum Thani","Phra Nakhon Si Ayutthaya","Phichit","Phitsanulok","Phetchabun","Lopburi","Sa mut Prakan","Samut Songkhram","Samut Sakhon","Sing Buri","Sukhothai","Suphan Buri","Saraburi", "Ang Thong","Uthai Thani", "Chanthaburi","Chachoengsao","Chonburi","Trat", "Prach inburi","Rayong", "Sa Kaeo","Kanchanaburi","Tak","PrachuapKhiriKhan","Phetchaburi","Ratchaburi","Krabi", "Chumphon","Trang", "Nakhon Si Thammarat","Narathiwat","Pattani","Phang Nga","Phatthalung","Phuket","Ranong","Satun","Songkhla","Sur at Thani","Yala"])

    st.divider()


    css = '''
    <link href="https://fonts.googleapis.com/css2?family=Niramit:ital,wght@0,200;0,300;0,400;0,500;0,600;0,700;1,200;1,300;1,400;1,500;1,600;1,700&family=Outfit:wght@100..900&display=swap" rel="stylesheet">
    <p style="color:Black; font-size: 20px; font-family:Niramit;">เลือกวิธีการทำนายภาพเเมลง</p>
    '''
    st.markdown(css, unsafe_allow_html=True)

    css = '''
    <link href="https://fonts.googleapis.com/css2?family=Niramit:ital,wght@0,200;0,300;0,400;0,500;0,600;0,700;1,200;1,300;1,400;1,500;1,600;1,700&family=Outfit:wght@100..900&display=swap" rel="stylesheet">
    <p style="color:Black; font-size: 14px; font-family:Niramit;">วิธีที่ 1 อัปโหลดภาพ</p>
    '''
    st.markdown(css, unsafe_allow_html=True)
 
 
 
 
 
 
 
    
    my_image1 = st.file_uploader("Upload a picture")
    if my_image1:
        st.image(my_image1)
    
    st.divider()

    css = '''
    <link href="https://fonts.googleapis.com/css2?family=Niramit:ital,wght@0,200;0,300;0,400;0,500;0,600;0,700;1,200;1,300;1,400;1,500;1,600;1,700&family=Outfit:wght@100..900&display=swap" rel="stylesheet">
    <p style="color:Black; font-size: 14px; font-family:Niramit;">วิธีที่ 2 ถ่ายภาพ</p>
    '''
    st.markdown(css, unsafe_allow_html=True)

    enable = st.checkbox("เปิดใช้งานกล้อง")
    


    my_image2 = st.camera_input("Take a picture", disabled=not enable)
    if my_image2:
        st.image(my_image2)


