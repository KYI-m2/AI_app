import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as html
from  PIL import Image
import numpy as np
import pandas as pd
import io 
from pathlib import Path
import numpy as np
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


    
if choose == 'Search Bar':
    st.title('Search Bar')
    df = pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vRbJASheYsGWBGRERpBkHJ0tGyLepOue779r-kCYiz9i063jnUqCVRRq5jpkkAfRf5J1O44tT6Tc2Z7/pub?gid=587778608&single=true&output=csv")
    insect_names = df["insect_name"]
    data = [
        "ด้วงน้ำมัน", "ด้วงก้นกระดก", "แมลงตด", "แมลงบุกบ้าน", "ผึ้งหลวง", 
        "ผึ้งเลี้ยง", "ตัวต่อหัวเสือ", "แตน", "มวนเพชฌฆาต", "เรือด",
        "หนอนบุ้งร่าน", "แมลงสาบอเมริกัน", "แมลงสาบเยอรมัน", "แมลงสาบผี",
        "โลน", "มดคันไฟ", "มดง่าม", "มดดำ", "มดตะนอย", "แมลงวันบ้าน", 
        "หมาร่า", "แมลงวันหัวเขียว", "แมลงวันคอกสัตว์", "แมลงวันตา", 
        "แมลงวันหลังลาย", "แมลงวันเซ็ทซี", "ยุงก้นปล่อง", "ยุงรำคาญ", 
        "ยุงลายบ้าน", "ยุงลายสวน", "ยุงลายเสือ", "ริ้นดำ", 
        "ริ้นน้ำเค็ม", "ริ้นฝอยทราย", "หมัด", "เหา"
    ]
    
    search_query = st.text_input("Search for an insect:")
    
    if search_query:
        # Filter results based on the search query
        results = df[df["insect_name"].str.contains(search_query, case=False, na=False)]
        insect_name = search_query
        if not results.empty:
            st.write("Results:")
            for index, row in results.iterrows():
                if insect_name == 'ด้วงน้ำมัน':
                    st.image("A001_101.jpg")
                elif insect_name == 'ด้วงก้นกระดก':
                    st.image("A002_101.jpg")
                elif insect_name == 'แมลงตด':
                    st.image("A003_101.jpg")
                elif insect_name == 'แมลงบุกบ้าน':
                    st.image("A004_101.jpg")
                elif insect_name == 'ผึ้งหลวง':
                    st.image("A005_101.jpg")
                elif insect_name == 'ผึ้งเลี้ยง':
                    st.image("A006_101.jpg")
                elif insect_name == 'ตัวต่อหัวเสือ':
                    st.image("A007_101.jpg")
                elif insect_name == 'แตน':
                    st.image("A008_101.jpg")
                elif insect_name == 'มวนเพชรฆาต':
                    st.image("A009_101.jpg")
                elif insect_name == 'เรือด':
                    st.image("A010_101.jpg")
                elif insect_name == 'หนอนบุ้งร่าน':
                    st.image("A011_101.jpg")
                elif insect_name == 'แมลงสาบอเมริกัน':
                    st.image("A012_101.jpg")
                elif insect_name == 'แมลงสาบเยอรมัน':
                    st.image("A013_101.jpg")
                elif insect_name == 'แมลงสาบผี':
                    st.image("A014_101.jpg")
                elif insect_name == 'โลน':
                    st.image("A015_101.jpg")
                elif insect_name == 'มดคันไฟ':
                    st.image("A016_101.jpg")
                elif insect_name == 'มดง่าม':
                    st.image("A017_101.jpg")
                elif insect_name == 'มดดำ':
                    st.image("A018_101.jpg")
                elif insect_name == 'มดตะนอย':
                    st.image("A019_101.jpg")
                elif insect_name == 'แมลงวันบ้าน':
                    st.image("A020_101.jpg")
                elif insect_name == 'หมาร่า':
                    st.image("A021_101.jpg")
                elif insect_name == 'แมลงวันหัวเขียว':
                    st.image("A022_101.jpg")
                elif insect_name == 'แมลงวันคอกสัตว์':
                    st.image("A023_101.jpg")
                elif insect_name == 'แมลงวันตา':
                    st.image("A024_101.jpg")
                elif insect_name == 'แมลงวันหลังลาย':
                    st.image("A025_101.jpg")
                elif insect_name == 'แมลงวันเซ็ทซี':
                    st.image("A026_101.jpg")
                elif insect_name == 'ยุงก้นปล่อง':
                    st.image("A027_101.jpg")
                elif insect_name == 'ยุงรำคาญ':
                    st.image("A028_101.jpg")
                elif insect_name == 'ยุงลายบ้าน':
                    st.image("A029_101.jpg")
                elif insect_name == 'ยุงลายสวน':
                    st.image("A030_101.jpg")
                elif insect_name == 'ยุงลายเสือ':
                    st.image("A031_101.jpg")
                elif insect_name == 'ริ้นดำ หรือตัวคุ่น':
                    st.image("A032_101.jpg")
                elif insect_name == 'ริ้นน้ำเค็ม':
                    st.image("A033_101.jpg")
                elif insect_name == 'ริ้นฝอยทราย':
                    st.image("A034_101.jpg")
                elif insect_name == 'หมัด':
                    st.image("A035_101.jpg")
                else:
                    st.image("A036_101.jpg")

                st.write("Insect Name:", row["insect_name"])
                st.write("Scientific Name:", row['insect_sci_name'])
                st.write("Type:", row['type'])
                st.write("Characteristics:", row['characteristics'])
                st.write("find:", row['find'])
                if insect_name == 'ด้วงน้ำมัน':
                    st.image("A001.jpg")
                elif insect_name == 'ด้วงก้นกระดก':
                    st.image("A002.jpeg")
                elif insect_name == 'แมลงตด':
                    st.image("A003.jpeg")
                elif insect_name == 'แมลงบุกบ้าน':
                    st.image("A004.jpeg")
                elif insect_name == 'ผึ้งหลวง':
                    st.image("A005.jpeg")
                elif insect_name == 'ผึ้งเลี้ยง':
                    st.image("A006.jpeg")
                elif insect_name == 'ตัวต่อหัวเสือ':
                    st.image("A007.jpg")
                elif insect_name == 'แตน':
                    st.image("A008.jpg")
                elif insect_name == 'มวนเพชรฆาต':
                    st.image("A009.jpeg")
                elif insect_name == 'เรือด':
                    st.image("A010.jpeg")
                elif insect_name == 'หนอนบุ้งร่าน':
                    st.image("A011.jpeg")
                elif insect_name == 'แมลงสาบอเมริกัน':
                    st.image("A012.jpeg")
                elif insect_name == 'แมลงสาบเยอรมัน':
                    st.image("A013.jpeg")
                elif insect_name == 'แมลงสาบผี':
                    st.image("A014.jpeg")
                elif insect_name == 'โลน':
                    st.image("A015.jpeg")
                elif insect_name == 'มดคันไฟ':
                    st.image("A016.jpeg")
                elif insect_name == 'มดง่าม':
                    st.image("A017.jpeg")
                elif insect_name == 'มดดำ':
                    st.image("A018.jpeg")
                elif insect_name == 'มดตะนอย':
                    st.image("A019.jpeg")
                elif insect_name == 'แมลงวันบ้าน':
                    st.image("A020.jpeg")
                elif insect_name == 'หมาร่า':
                    st.image("A021.jpeg")
                elif insect_name == 'แมลงวันหัวเขียว':
                    st.image("A022.jpg")
                elif insect_name == 'แมลงวันคอกสัตว์':
                    st.image("A023.jpg")
                elif insect_name == 'แมลงวันตา':
                    st.image("A024.jpeg")
                elif insect_name == 'แมลงวันหลังลาย':
                    st.image("A025.jpeg")
                elif insect_name == 'แมลงวันเซ็ทซี':
                    st.image("A026.jpeg")
                elif insect_name == 'ยุงก้นปล่อง':
                    st.image("A027.jpeg")
                elif insect_name == 'ยุงรำคาญ':
                    st.image("A028.jpeg")
                elif insect_name == 'ยุงลายบ้าน':
                    st.image("A029.jpeg")
                elif insect_name == 'ยุงลายสวน':
                    st.image("A030.jpeg")
                elif insect_name == 'ยุงลายเสือ':
                    st.image("A031.jpeg")
                elif insect_name == 'ริ้นดำ หรือตัวคุ่น':
                    st.image("A032.jpeg")
                elif insect_name == 'ริ้นน้ำเค็ม':
                    st.image("A033.jpeg")
                elif insect_name == 'ริ้นฝอยทราย':
                    st.image("A034.jpeg")
                elif insect_name == 'หมัด':
                    st.image("A035.jpeg")
                else:
                    st.image("A036.jpeg")
                st.write("poision:", row['poision'])
                st.write("symptom:", row['symptom'])
                
                
                if insect_name == 'ด้วงก้นกระดก':
                    st.write("แผล:")
                    st.image("A002_แมลงก้นกระดก.jpg")
                elif insect_name == 'แมลงตด':
                    st.write("แผล:")
                    st.image("A003_แมลงตด.jpg")
                elif insect_name == 'ผึ้งหลวง':
                    st.write("แผล:")
                    st.image("A005_ผึ้งหลวง.jpg")
                elif insect_name == 'ผึ้งพันธุ์':
                    st.write("แผล:")
                    st.image("A006_ผึ้งพันธุ์.jpg")
                elif insect_name == 'ต่อหัวเสือ':
                    st.write("แผล:")
                    st.image("A007_ต่อหัวเสือ.jpg")
                elif insect_name == 'แตนลาม':
                    st.write("แผล:")
                    st.image("A008_แตนลาม.jpg")
                elif insect_name == 'มวนเพชฌฆาต':
                    st.write("แผล:")
                    st.image("A009_มวนเพชฌฆาต.jpg")
                elif insect_name == 'เรือด':
                    st.write("แผล:")
                    st.image("A010_เรือด.jpg")
                elif insect_name == 'หนอนบุ้งร่าน':
                    st.write("แผล:")
                    st.image("A011_หนอนบุ้งร่าน.jpg")
                elif insect_name == 'โลน':
                    st.write("แผล:")
                    st.image("A015_โลน.jpg")
                elif insect_name == 'มดคันไฟ':
                    st.write("แผล:")
                    st.image("A016_มดคันไฟ.jpg")
                elif insect_name == 'มดง่าม':
                    st.write("แผล:")
                    st.image("A017_มดง่าม.jpg")
                elif insect_name == 'มดดำ':
                    st.write("แผล:")
                    st.image("A018_มดดำ.jpg")
                elif insect_name == 'มดตะนอย':
                    st.write("แผล:")
                    st.image("A019_มดตะนอย.jpg")
                elif insect_name == 'แมลงวันบ้าน':
                    st.write("แผล:")
                    st.image("A020_แมลงวันบ้าน.jpg")
                elif insect_name == 'แมลงวันคอกสัตว์':
                    st.write("แผล:")
                    st.image("A023_แมลงวันคอกสัตว์.jpg")
                elif insect_name == 'แมลงวันตา':
                    st.write("แผล:")
                    st.image("A024_แมลงวันตา.jpg")
                elif insect_name == 'ยุงรำคาญ':
                    st.write("แผล:")
                    st.image("A028_ยุงรำคาญ.jpg")
                elif insect_name == 'ยุงลายบ้าน':
                    st.write("แผล:")
                    st.image("A029_ยุงลายบ้าน.jpg")
                elif insect_name == 'ยุงลายสวน':
                    st.write("แผล:")
                    st.image("A030_ยุงลายสวน.jpg")
                elif insect_name == 'ยุงลายเสือ':
                    st.write("แผล:")
                    st.image("A031_ยุงลายเสือ.jpg")
                elif insect_name == 'ริ้นดำ':
                    st.write("แผล:")
                    st.image("A032_ริ้นดำ.jpg")
                elif insect_name == 'ริ้นน้ำเค็ม':
                    st.write("แผล:")
                    st.image("A033_ริ้นน้ำเค็ม.jpg")
                elif insect_name == 'ริ้นฝอยทราย':
                    st.write("แผล:")
                    st.image("A034_ริ้นฝอยทราย.jpg")
                elif insect_name == 'หมัดสุนัข':
                    st.write("แผล:")
                    st.image("A035_หมัดสุนัข.jpg")
                elif insect_name == 'เหา':
                    st.write("แผล:")
                    st.image("A036_เหา.jpg")
                else:
                    st.write("แผล: -")
                st.write("How to protect:", row['How to protect'])
                st.write("---")  # Separator for clarity
        else:
            st.write("No results found.")
        

if choose == "Contact Us" :
    st.title('Contact Us')
    st.write('แนะนำสมาชิกในกลุ่ม')

    st.write("We are the developers!!<3")
    st.write("ช่องทางการติดต่อของเรา: \n Gmail: webapplication.m2@gmail.com")



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
       
    chart_data = pd.DataFrame( {'name': ['A001','A002','A003'], 'value':[10,20,30]} )
    st.bar_chart(chart_data, x="name", y="value", stack=False)
