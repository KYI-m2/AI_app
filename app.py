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

import streamlit as st
import requests

def download_file_from_google_drive(file_id, destination):
    base_url = "https://docs.google.com/uc?export=download"
    session = requests.Session()

    # สร้าง URL สำหรับดาวน์โหลด
    response = session.get(base_url, params={'id': file_id}, stream=True)
    token = get_confirm_token(response)

    if token:
        params = {'id': file_id, 'confirm': token}
        response = session.get(base_url, params=params, stream=True)

    # บันทึกไฟล์
    with open(destination, "wb") as f:
        for chunk in response.iter_content(32768):
            if chunk:
                f.write(chunk)

def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value
    return None

# เริ่มการดาวน์โหลดไฟล์โดยอัตโนมัติเมื่อเปิดแอป
with st.spinner("Downloading..."):
    file_id = "1Nga5BhuUjMBt88KRd3NqNxyIosQUJjSw"  # ID จากลิงก์ที่ให้
    destination = "downloaded_file"  # ชื่อไฟล์ที่ต้องการบันทึก
    download_file_from_google_drive(file_id, destination)

st.success("File downloaded successfully!")

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
    predicted_name = ''
    df_1 = pd.read_excel("output.xlsx",index_col = 0)
    new_index = len(df_1)
    css = '''
    <link href="https://fonts.googleapis.com/css2?family=Niramit:ital,wght@0,200;0,300;0,400;0,500;0,600;0,700;1,200;1,300;1,400;1,500;1,600;1,700&family=Outfit:wght@100..900&display=swap" rel="stylesheet">
    <p style="color:Black; font-size: 20px; font-family:Niramit;">กรอกข้อมูลผู้ใช้</p>
    '''
    st.markdown(css, unsafe_allow_html=True)

    gender = st.selectbox("เพศ (Gender)", ["male", "female", "other"])
    date = st.text_input("วันที่ (Date) dd/mm/yyyy พุทธศักราช")
    time = st.text_input("เวลา (Time) xx:xx เวลาไทย")
    age = st.slider("อายุ (Age)", 0, 100)
    city = st.selectbox("จังหวัด (city)", ["Chiang Mai","Chiang Rai","Lampang","Lamphun", "Mae Hong Son","Nan","Phayao","Phrae","Uttaradit","Kalasin","Khon Kaen","Chaiyaphum", "Nakhon Phanom","Nakhon Ratchasima","Bueng Kan", "Buriram", "Maha Sarakham","Mukdahan", "Yasothon","Roi Et","Loei","Sakon Nakhon","Surin","Sisaket","Nong Khai","Nong Bua Lamphu","Udon Thani","Ubon Ratchathani","Amnat Charoen", "Bangkok","Kamphaeng Phet","Chai Nat","Nakhon Nayok","Nakhon Pathom","Nakhon Sawan","Nonthaburi", "Pathum Thani","Phra Nakhon Si Ayutthaya","Phichit","Phitsanulok","Phetchabun","Lopburi","Sa mut Prakan","Samut Songkhram","Samut Sakhon","Sing Buri","Sukhothai","Suphan Buri","Saraburi", "Ang Thong","Uthai Thani", "Chanthaburi","Chachoengsao","Chonburi","Trat", "Prach inburi","Rayong", "Sa Kaeo","Kanchanaburi","Tak","PrachuapKhiriKhan","Phetchaburi","Ratchaburi","Krabi", "Chumphon","Trang", "Nakhon Si Thammarat","Narathiwat","Pattani","Phang Nga","Phatthalung","Phuket","Ranong","Satun","Songkhla","Sur at Thani","Yala"])

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

     # Load the json file that contains the model's structure
    f = Path("model_structure_100.json")
    model_structure = f.read_text()


    model = model_from_json(model_structure)
    model.load_weights("model_100.weights.h5")

    if my_image1 or my_image2 :
        if st.button('predict'):
            my_image = my_image1 if my_image1 else my_image2
                
            img = image.load_img(my_image, target_size=(224, 224))
            image_array = image.img_to_array(img)
            images = np.expand_dims(image_array, axis=0)
            images = vgg16.preprocess_input(images)

            feature_extraction_model = vgg16.VGG16(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
            features = feature_extraction_model.predict(images)

                

            # Given the extracted features, make a final prediction using our own model
            results = model.predict(features)
            print('Probability:', results)

            predicted_class = np.argmax(results)

            predicted_name = 'None'
            if predicted_class==0:
                predicted_name = 'ด้วงน้ำมัน'
            elif predicted_class==1:
                predicted_name = 'ด้วงก้นกระดก'
            elif predicted_class==2:
                predicted_name = 'แมลงตด'
            elif predicted_class==3:
                predicted_name = 'แมลงบุกบ้าน'
            elif predicted_class==4:
                predicted_name = 'ผึ้งหลวง'
            elif predicted_class==5:
                predicted_name = 'ผึ้งเลี้ยง'
            elif predicted_class==6:
                predicted_name = 'ตัวต่อหัวเสือ'
            elif predicted_class==7:
                predicted_name = 'แตน'
            elif predicted_class==8:
                predicted_name = 'มวนเพชรฆาต'
            elif predicted_class==9:
                predicted_name = 'เรือด'
            elif predicted_class==10:
                predicted_name = 'หนอนบุ้งร่าน'
            elif predicted_class==11:
                predicted_name = 'แมลงสาบอเมริกัน'
            elif predicted_class==12:
                predicted_name = 'แมลงสาบเยอรมัน'
            elif predicted_class==13:
                predicted_name = 'แมลงสาบผี'
            elif predicted_class==14:
                predicted_name = 'โลน'
            elif predicted_class==15:
                predicted_name = 'มดคันไฟ'
            elif predicted_class==16:
                predicted_name = 'มดง่าม'
            elif predicted_class==17:
                predicted_name = 'มดดำ'
            elif predicted_class==18:
                predicted_name = 'มดตะนอย'
            elif predicted_class==19:
                predicted_name = 'แมลงวันบ้าน'
            elif predicted_class==20:
                predicted_name = 'หมาร่า'
            elif predicted_class==21:
                predicted_name = 'แมลงวันหัวเขียว'
            elif predicted_class==22:
                predicted_name = 'แมลงวันคอกสัตว์'
            elif predicted_class==23:
                predicted_name = 'แมลงวันตา'
            elif predicted_class==24:
                predicted_name = 'แมลงวันหลังลาย'
            elif predicted_class==25:
                predicted_name = 'แมลงวันเซ็ทซี'
            elif predicted_class==26:
                predicted_name = 'ยุงก้นปล่อง'
            elif predicted_class==27:
                predicted_name = 'ยุงรำคาญ'
            elif predicted_class==28:
                predicted_name = 'ยุงลายบ้าน'
            elif predicted_class==29:
                predicted_name = 'ยุงลายสวน'
            elif predicted_class==30:
                predicted_name = 'ยุงลายเสือ'
            elif predicted_class==31:
                predicted_name = 'ริ้นดำ หรือตัวคุ่น'
            elif predicted_class==32:
                predicted_name = 'ริ้นน้ำเค็ม'
            elif predicted_class==33:
                predicted_name = 'ริ้นฝอยทราย'
            elif predicted_class==34:
                predicted_name = 'หมัด'
            else :
                predicted_name = 'เหา'
            result_text ='This is '+ predicted_name +' with confidence: ' + str(results[0][np.argmax(results)]*100)
            st.success(result_text)

            df = pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vRbJASheYsGWBGRERpBkHJ0tGyLepOue779r-kCYiz9i063jnUqCVRRq5jpkkAfRf5J1O44tT6Tc2Z7/pub?gid=587778608&single=true&output=csv")
            insect_names = df["insect_name"]
            
            
            
            for index, i in enumerate(insect_names):
                if predicted_name == i:
                    if predicted_name == 'ด้วงน้ำมัน':
                        st.image("A001_001.jpg")
                    elif predicted_name == 'ด้วงก้นกระดก':
                        st.image("A002_027.jpg")
                    elif predicted_name == 'แมลงตด':
                        st.image("A003_021.jpg")
                    elif predicted_name == 'แมลงบุกบ้าน':
                        st.image("A004_006.jpg")
                    elif predicted_name == 'ผึ้งหลวง':
                        st.image("A005_019.jpg")
                    elif predicted_name == 'ผึ้งเลี้ยง':
                        st.image("A006_001.jpg")
                    elif predicted_name == 'ตัวต่อหัวเสือ':
                        st.image("A007_083.jpg")
                    elif predicted_name == 'แตน':
                        st.image("A008_008.jpg")
                    elif predicted_name == 'มวนเพชรฆาต':
                        st.image("A009_001.jpg")
                    elif predicted_name == 'เรือด':
                        st.image("A010_001.jpg")
                    elif predicted_name == 'หนอนบุ้งร่าน':
                        st.image("A11_080.jpg")
                    elif predicted_name == 'แมลงสาบอเมริกัน':
                        st.image("A012_003.jpg")
                    elif predicted_name == 'แมลงสาบเยอรมัน':
                        st.image("A013_001.jpg")
                    elif predicted_name == 'แมลงสาบผี':
                        st.image("A014_031.jpg")
                    elif predicted_name == 'โลน':
                        st.image("A015_101.jpg")
                    elif predicted_name == 'มดคันไฟ':
                        st.image("A016_073.jpg")
                    elif predicted_name == 'มดง่าม':
                        st.image("A017_084.jpg")
                    elif predicted_name == 'มดดำ':
                        st.image("A018_098.jpg")
                    elif predicted_name == 'มดตะนอย':
                        st.image("A019_085.jpg")
                    elif predicted_name == 'แมลงวันบ้าน':
                        st.image("A020_052.jpg")
                    elif predicted_name == 'หมาร่า':
                        st.image("A021_072.jpg")
                    elif predicted_name == 'แมลงวันหัวเขียว':
                        st.image("A022_001.jpg")
                    elif predicted_name == 'แมลงวันคอกสัตว์':
                        st.image("A023_001.jpg")
                    elif predicted_name == 'แมลงวันตา':
                        st.image("A024_070.jpg")
                    elif predicted_name == 'แมลงวันหลังลาย':
                        st.image("A025_001.jpg")
                    elif predicted_name == 'แมลงวันเซ็ทซี':
                        st.image("A026_094.jpg")
                    elif predicted_name == 'ยุงก้นปล่อง':
                        st.image("A027_096.jpg")
                    elif predicted_name == 'ยุงรำคาญ':
                        st.image("A028_001.jpg")
                    elif predicted_name == 'ยุงลายบ้าน':
                        st.image("A029_056.jpg")
                    elif predicted_name == 'ยุงลายสวน':
                        st.image("A030_085.jpg")
                    elif predicted_name == 'ยุงลายเสือ':
                        st.image("A031_055.jpg")
                    elif predicted_name == 'ริ้นดำ หรือตัวคุ่น':
                        st.image("A032_099.jpg")
                    elif predicted_name == 'ริ้นน้ำเค็ม':
                        st.image("A033_098.jpg")
                    elif predicted_name == 'ริ้นฝอยทราย':
                        st.image("A034_027.jpg")
                    elif predicted_name == 'หมัด':
                        st.image("A035_025.jpg")
                    else:
                        st.image("A036_028.jpg")
                    st.write(df['อ้างอิงตัวอย่างแมลง'][index])
                    st.header(df["insect_name"][index])
                    st.text(df['insect_sci_name'][index])
                    st.text(df['type'][index])
                    st.subheader("ลักษณะของแมลง")
                    st.write(df['characteristics'][index])
                    st.subheader("แหล่งที่พบ")
                    st.write(df['find'][index])
                    if predicted_name == 'ด้วงน้ำมัน':
                        st.image("A001.jpg")
                    elif predicted_name == 'ด้วงก้นกระดก':
                        st.image("A002.jpeg")
                    elif predicted_name == 'แมลงตด':
                        st.image("A003.jpeg")
                    elif predicted_name == 'แมลงบุกบ้าน':
                        st.image("A004.jpeg")
                    elif predicted_name == 'ผึ้งหลวง':
                        st.image("A005.jpeg")
                    elif predicted_name == 'ผึ้งเลี้ยง':
                        st.image("A006.jpeg")
                    elif predicted_name == 'ตัวต่อหัวเสือ':
                        st.image("A007.jpg")
                    elif predicted_name == 'แตน':
                        st.image("A008.jpg")
                    elif predicted_name == 'มวนเพชรฆาต':
                        st.image("A009.jpeg")
                    elif predicted_name == 'เรือด':
                        st.image("A010.jpeg")
                    elif predicted_name == 'หนอนบุ้งร่าน':
                        st.image("A011.jpeg")
                    elif predicted_name == 'แมลงสาบอเมริกัน':
                        st.image("A012.jpeg")
                    elif predicted_name == 'แมลงสาบเยอรมัน':
                        st.image("A013.jpeg")
                    elif predicted_name == 'แมลงสาบผี':
                        st.image("A014.jpeg")
                    elif predicted_name == 'โลน':
                        st.image("A015.jpeg")
                    elif predicted_name == 'มดคันไฟ':
                        st.image("A016.jpeg")
                    elif predicted_name == 'มดง่าม':
                        st.image("A017.jpeg")
                    elif predicted_name == 'มดดำ':
                        st.image("A018.jpeg")
                    elif predicted_name == 'มดตะนอย':
                        st.image("A019.jpeg")
                    elif predicted_name == 'แมลงวันบ้าน':
                        st.image("A020.jpeg")
                    elif predicted_name == 'หมาร่า':
                        st.image("A021.jpeg")
                    elif predicted_name == 'แมลงวันหัวเขียว':
                        st.image("A022.jpg")
                    elif predicted_name == 'แมลงวันคอกสัตว์':
                        st.image("A023.jpg")
                    elif predicted_name == 'แมลงวันตา':
                        st.image("A024.jpeg")
                    elif predicted_name == 'แมลงวันหลังลาย':
                        st.image("A025.jpeg")
                    elif predicted_name == 'แมลงวันเซ็ทซี':
                        st.image("A026.jpeg")
                    elif predicted_name == 'ยุงก้นปล่อง':
                        st.image("A027.jpeg")
                    elif predicted_name == 'ยุงรำคาญ':
                        st.image("A028.jpeg")
                    elif predicted_name == 'ยุงลายบ้าน':
                        st.image("A029.jpeg")
                    elif predicted_name == 'ยุงลายสวน':
                        st.image("A030.jpeg")
                    elif predicted_name == 'ยุงลายเสือ':
                        st.image("A031.jpeg")
                    elif predicted_name == 'ริ้นดำ หรือตัวคุ่น':
                        st.image("A032.jpeg")
                    elif predicted_name == 'ริ้นน้ำเค็ม':
                        st.image("A033.jpeg")
                    elif predicted_name == 'ริ้นฝอยทราย':
                        st.image("A034.jpeg")
                    elif predicted_name == 'หมัด':
                        st.image("A035.jpeg")
                    else:
                        st.image("A036.jpg")
                    
                    st.subheader("ส่วนที่เป็นพิษ") 
                    st.write(df['poision'][index])
                    st.subheader("อาการเมื่อถูกพิษ")
                    st.write(df['symptom'][index])
                    
                    if predicted_name == 'ด้วงก้นกระดก':
                        st.write("แผล:")
                        st.image("A002_แมลงก้นกระดก.jpg")
                    elif insect_name == 'ด้วงน้ำมัน':
                        st.write("แผล:")
                        st.image("A001_แมลงด้วงน้ำมัน 2.jpg")
                    elif predicted_name == 'แมลงตด':
                        st.write("แผล:")
                        st.image("A003_แมลงตด.jpg")
                    elif predicted_name == 'ผึ้งหลวง':
                        st.write("แผล:")
                        st.image("A005_ผึ้งหลวง.jpg")
                    elif predicted_name == 'ผึ้งเลี้ยง':
                        st.write("แผล:")
                        st.image("A006_ผึ้งพันธุ์.jpg")
                    elif predicted_name == 'ต่อหัวเสือ':
                        st.write("แผล:")
                        st.image("A007_ต่อหัวเสือ.jpg")
                    elif predicted_name == 'แตนลาม':
                        st.write("แผล:")
                        st.image("A008_แตนลาม.jpg")
                    elif predicted_name == 'มวนเพชฌฆาต':
                        st.write("แผล:")
                        st.image("A009_มวนเพชฌฆาต.jpg")
                    elif predicted_name == 'เรือด':
                        st.write("แผล:")
                        st.image("A010_เรือด.jpg")
                    elif predicted_name == 'หนอนบุ้งร่าน':
                        st.write("แผล:")
                        st.image("A011_หนอนบุ้งร่าน.jpg")
                    elif predicted_name == 'โลน':
                        st.write("แผล:")
                        st.image("A015_โลน.jpg")
                    elif predicted_name == 'มดคันไฟ':
                        st.write("แผล:")
                        st.image("A016_มดคันไฟ.jpg")
                    elif predicted_name == 'มดง่าม':
                        st.write("แผล:")
                        st.image("A017_มดง่าม.jpg")
                    elif predicted_name == 'มดดำ':
                        st.write("แผล:")
                        st.image("A018_มดดำ.jpg")
                    elif predicted_name == 'มดตะนอย':
                        st.write("แผล:")
                        st.image("A019_มดตะนอย.jpg")
                    elif predicted_name == 'แมลงวันบ้าน':
                        st.write("แผล:")
                        st.image("A020_แมลงวันบ้าน.jpg")
                    elif predicted_name == 'แมลงวันคอกสัตว์':
                        st.write("แผล:")
                        st.image("A023_แมลงวันคอกสัตว์.jpg")
                    elif predicted_name == 'แมลงวันตา':
                        st.write("แผล:")
                        st.image("A024_แมลงวันตา.jpg")
                    elif predicted_name == 'ยุงรำคาญ':
                        st.write("แผล:")
                        st.image("A028_ยุงรำคาญ.jpg")
                    elif predicted_name == 'ยุงลายบ้าน':
                        st.write("แผล:")
                        st.image("A029_ยุงลายบ้าน.jpg")
                    elif predicted_name == 'ยุงลายสวน':
                        st.write("แผล:")
                        st.image("A030_ยุงลายสวน.jpg")
                    elif predicted_name == 'ยุงลายเสือ':
                        st.write("แผล:")
                        st.image("A031_ยุงลายเสือ.jpg")
                    elif predicted_name == 'ริ้นดำ':
                        st.write("แผล:")
                        st.image("A032_ริ้นดำ.jpg")
                    elif predicted_name == 'ริ้นน้ำเค็ม':
                        st.write("แผล:")
                        st.image("A033_ริ้นน้ำเค็ม.jpg")
                    elif predicted_name == 'ริ้นฝอยทราย':
                        st.write("แผล:")
                        st.image("A034_ริ้นฝอยทราย.jpg")
                    elif predicted_name == 'หมัดสุนัข':
                        st.write("แผล:")
                        st.image("A035_หมัดสุนัข.jpg")
                    elif predicted_name == 'เหา':
                        st.write("แผล:")
                        st.image("A036_เหา.jpg")
                    else:
                        st.write("แผล: -")
                    st.write(df['อ้างอิง ภาพแผล'][index]) 
                    st.subheader("วิธีป้องกัน")
                    st.write(df['How to protect'][index])
                    st.write("แหล่งข้อมูล : " , df['แหล่งข้อมูล'][index])

    
    
                    df_1.loc[new_index,'gender'] = gender
                    df_1.loc[new_index,'date'] = date
                    df_1.loc[new_index,'Age'] = age
                    df_1.loc[new_index,'City'] = city
                    df_1.loc[new_index,'Insects'] = predicted_name


                        
                    st.dataframe(df_1)
                    df_1.to_excel("output.xlsx")
                    count_1 = df_1['Insects'].value_counts().reset_index()
                    count_1.columns = ['Insects', 'Count']
                    st.bar_chart(count_1, x='Insects', y='Count')
                    st.header("โปรดทำเเบบประเมินความพึงพอใจ(เลือกเพียง 1 ตัวเลือก)📚")
        st.subheader("โปรดประเมินประโยชน์การใช้งานของเว็บเเอปพลิเคชัน📚(Please fill out this form)")
        check = st.checkbox("⭐⭐⭐⭐⭐ ดีมาก(Excellent)")
        if check:
            st.write("การใช้งานเว็บเเอปพลิเคชันมีประโยชน์มากที่สุด(This Web Application is the most useful)")

        check_2 = st.checkbox("⭐⭐⭐⭐ ดี(Good)")
        if check_2:
            st.write("การใช้งานเว็บเเอปพลิเคชันมีประโยชน์มาก(This Web Application is very useful)")

        check_3 = st.checkbox("⭐⭐⭐ พอใช้(Fair)")
        if check_3:
            st.write("การใช้งานเว็บเเอปพลิเคชันมีประโยชน์ปานกลาง(This Web Application is neutrally useful)")

        check_4 = st.checkbox("⭐⭐ น้อย(Poor)")
        if check_4:
            st.write("การใช้งานเว็บเเอปพลิเคชันมีประโยชน์น้อย(This Web Application is less useful)")

        check_5 = st.checkbox("⭐ น้อยที่สุด(Very poor)")
        if check_5:
            st.write("การใช้งานเว็บเเอปพลิเคชันมีประโยชน์น้อยที่สุด(This Web Application poorly useful)")

        Feed_back = st.text_input("ข้อเสนอเเนะ(Enter your comments here)")

        result = st.button("Submit")
        if result:
            st.balloons()
            st.subheader("ขอบคุณสำหรับความร่วมมือ(Thank you for your kind cooperation)")
 
