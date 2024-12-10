import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as html
from  PIL import Image
import numpy as np
import pandas as pd 
import io 
import keras
from keras.models import model_from_json
from pathlib import Path
from tensorflow.keras.preprocessing import image
import numpy as np
from keras.applications import vgg16
import requests 
import base64
import openpyxl
from streamlit_webrtc import webrtc_streamer
import streamlit as st
import requests
import json
import requests
import streamlit_lottie
from streamlit_lottie import st_lottie 
import gspread
from oauth2client.service_account import ServiceAccountCredentials

page_bg_img= """
<style>
[data-testid="stAppViewContainer"] {
background-color: #b3ffb3;
opacity: 0.8;
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

side_bg_img= """
<style>
[data-testid="stSidebar"] {
background-color: #b3ffb3;
opacity: 0.8;
}
</style>
"""
st.markdown(side_bg_img, unsafe_allow_html=True)

    
import requests
import streamlit as st


def download_file_from_google_drive(file_id, destination):
    base_url = "https://drive.google.com/uc?export=download"
    session = requests.Session()

    # First request to get the download confirmation token (if required)
    response = session.get(base_url, params={'id': file_id}, stream=True)
    token = get_confirm_token(response)

    if token:
        # Add the confirmation token to the params for the second request
        params = {'id': file_id, 'confirm': token}
        response = session.get(base_url, params=params, stream=True)

    # Save the file
    save_response_content(response, destination)

def get_confirm_token(response):
    """Extract the confirmation token from cookies."""
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value
    return None

def save_response_content(response, destination):
    """Save the file content to the specified destination."""
    with open(destination, "wb") as f:
        for chunk in response.iter_content(32768):
            if chunk:  # Filter out keep-alive chunks
                f.write(chunk)

# Automatically download the file when the app opens
with st.spinner("Downloading..."):
    try:
        file_id = "1vvfkI-Qeo7xu1DS7FVGFqt9qKG950HhX"  # Replace with your Google Drive file ID
        destination = "model_ny9new.weights.h5"  # Desired filename
        download_file_from_google_drive(file_id, destination)
    except Exception:
        pass  # Silently handle errors if any

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
    st.write("KYI-Know Your Insect เป็นเว็บแอปพลิเคชันที่สร้างขึ้นด้วย Machine Learning, Python เเละ Streamlit   จัดทำขึ้นเป็นโครงงานเพื่อสร้างแหล่งข้อมูลแมลงที่มีพิษเเละเป็นอันตรายในประเทศไทยที่น่าเชื่อถือและสามารถเข้าถึงได้ง่าย เป็นโครงงานที่เกิดจากการผสมผสานของความรู้และเทคโนโลยี นำเสนอโดยนักเรียนชั้นมัธยมศึกษาปีที่ 2  จากโรงเรียนบดินทรเดชา(สิงห์ สิงหเสนี), จังหวัดกรุงเทพมหานคร, ประเทศไทย เว็บเเอปพลิเคชันนี้สามารถทำอะไรได้บ้าง? เพียงเเค่อัปโหลดภาพเเมลง หรือ ใช้การถ่ายภาพเเมลงที่สนใจลงในเว็บเเอปพลิเคชัน   เว็บเเอปพลิเคชันนี้ก็จะสามารถจำเเนกเเมลงที่มีพิษเเละเป็นอันตรายที่พบได้ในประเทศไทยได้นอกจากนี้ยังมี Search Bar ให้ผู้ใช้งานได้ค้นหาด้วยชื่อเเมลงอีกด้วย")
    st.divider()
    st.write("This is a Web-Application created with ML, Python, Streamlit made as a project to create a reliable and accessable data source of dangerous insects in Thailand, combining knowledge and technology, Brought to you by the M.2 students from Bodindecha (Sing Singhaseni) School, based in Bangkok, Thailand.  What can this Web Application do? It can be used to classify the  dangerous insects found mostly in Thailand with the method of just uploading your desired picture.")
    st.toast("Lets get started 🏁 ")
    st.toast("welcome to our web-based application!📚")  
    col1, col2, col3 ,col4 ,col5 = st.columns(5)
    with col2:
        st.image("Insect.jpg")
    def load_lottieurl(url: str):
        r = requests.get(url)
        if r.status_code !=200: 
            return None 
        return r.json()
      
    lottie_hello = load_lottieurl("https://lottie.host/8103cbaf-fa16-4f16-b2b4-6651a2726912/PfOOZRZgup.json")
    st_lottie(lottie_hello)  
 
 
        
if choose == "About Us" :
 st.title('About Us เกี่ยวกับเรา')
 css = '''
 <link href="https://fonts.googleapis.com/css2?family=Niramit:ital,wght@0,200;0,300;0,400;0,500;0,600;0,700;1,200;1,300;1,400;1,500;1,600;1,700&family=Outfit:wght@100..900&display=swap" rel="stylesheet">
 <p style="color:Black; font-size: 20px; font-family:Niramit;">แนะนำสมาชิกในกลุ่ม</p>
 '''
 st.markdown(css, unsafe_allow_html=True)
 st.image("aoon.jpg",width=300, caption="ด.ญ. กานต์ปภา ประจิตร์ ม.2/3 เลขที่ 21 (หัวหน้ากลุ่ม)")
 st.image("peem.jpg",width=300, caption="ด.ญ. ชนันธร มามีชัย ม.2/3 เลขที่ 23")
 st.image("miu.jpg",width=300,caption="ด.ญ. ฐิตามร กณิกนันต์ ม.2/3 เลขที่ 24")
 #helloworld


    
if choose == 'Search Bar':
    st.title('Search Bar')
    def load_lottieurl(url: str):
        r = requests.get(url)
        if r.status_code !=200: 
            return None 
        return r.json()
    lottie_hello = load_lottieurl("https://lottie.host/7cd0e391-66dc-42d9-9ca6-9a26aa8da25e/xn4QK6WpVX.json")
    st_lottie(lottie_hello)  
    # Load data from Google Sheets
    df = pd.read_csv(
        "https://docs.google.com/spreadsheets/d/e/2PACX-1vRbJASheYsGWBGRERpBkHJ0tGyLepOue779r-kCYiz9i063jnUqCVRRq5jpkkAfRf5J1O44tT6Tc2Z7/pub?gid=587778608&single=true&output=csv"
    )
    
    # Map insect names to image paths
    image_map = {
        "ด้วงน้ำมัน": "A001_001.jpg",
        "ด้วงก้นกระดก": "A002_027.jpg",
        "แมลงตด": "A003_021.jpg",
        "แมลงบุกบ้าน": "A004_006.jpg",
        "ผึ้งหลวง": "A005_019.jpg",
        "ผึ้งเลี้ยง": "A006_001.jpg",
        "ตัวต่อหัวเสือ": "A007_083.jpg",
        "แตน": "A008_008.jpg",
        "มวนเพชฌฆาต": "A009_001.jpg",
        "เรือด": "A010_001.jpg",
        "หนอนบุ้งร่าน": "A11_080.jpg",
        "แมลงสาบอเมริกัน": "A012_003.jpg",
        "แมลงสาบเยอรมัน": "A013_001.jpg",
        "แมลงสาบผี": "A014_031.jpg",
        "โลน": "A015_101.jpg",
        "มดคันไฟ": "A016_073.jpg",
        "มดง่าม": "A017_084.jpg",
        "มดดำ": "A018_098.jpg",
        "มดตะนอย": "A019_085.jpg",
        "แมลงวันบ้าน": "A020_052.jpg",
        "หมาร่า": "A021_072.jpg",
        "แมลงวันหัวเขียว": "A022_001.jpg",
        "แมลงวันคอกสัตว์": "A023_001.jpg",
        "แมลงวันตา": "A024_070.jpg",
        "แมลงวันหลังลาย": "A025_001.jpg",
        "แมลงวันเซ็ทซี": "A026_094.jpg",
        "ยุงก้นปล่อง": "A027_096.jpg",
        "ยุงรำคาญ": "A028_001.jpg",
        "ยุงลายบ้าน": "A029_056.jpg",
        "ยุงลายสวน": "A030_085.jpg",
        "ยุงลายเสือ": "A031_055.jpg",
        "ริ้นดำ": "A032_099.jpg",
        "ริ้นน้ำเค็ม": "A033_098.jpg",
        "ริ้นฝอยทราย": "A034_027.jpg",
        "หมัด": "A035_025.jpg",
        "เหา": "A036_028.jpg",
    }
    
    # App title
    st.title("Insect Search")
    
    # Search bar
    query = st.text_input("Search for an insect:", "")
    
    # Search logic
    if query:
        # Filter the dataset based on the query
        results = df[df["insect_name"].str.contains(query, case=False, na=False)]
    
        # Display results dynamically
        if not results.empty:
            st.write(f"### Search Results for '{query}':")
            for _, row in results.iterrows():
                # Display insect details
                st.subheader(row["insect_name"])  # Display insect name
                if row["insect_name"] in image_map:
                    st.image(image_map[row["insect_name"]], caption=row["insect_name"])
                else:
                    st.write("No image available.")
                
                # Display other insect details
                st.write("**Scientific Name:**", row["insect_sci_name"])
                st.write("**Type:**", row["type"])
                st.write("**Characteristics:**", row["characteristics"])
                st.write("**Found In:**", row["find"])
                st.write("**Poison:**", row["poision"])
                st.write("**Symptoms:**", row["symptom"])
                st.write("**How to Protect:**", row["How to protect"])
                st.write("---")  # Separator for clarity
        else:
            st.write(f"No results found for '{query}'.")
    else:
        st.write("Enter an insect name to search.")
    
            

if choose == "Contact Us" :
    st.title('Contact Us')
    
    st.write("ช่องทางการติดต่อของเรา: \n Gmail: webapplication.m2@gmail.com")
    def load_lottieurl(url: str):
         r = requests.get(url)
         if r.status_code !=200: 
             return None 
         return r.json() 
    lottie_hello = load_lottieurl("https://lottie.host/7c423378-4342-4a85-a43f-182d60239a2d/Kexj7XXBoQ.json")
    st_lottie(lottie_hello)


if choose == 'Image Classification' :
    def load_lottieurl(url: str):
        r = requests.get(url)
        if r.status_code !=200: 
            return None 
        return r.json()
      
    lottie_hello = load_lottieurl("https://lottie.host/291ab457-690e-43ef-a83b-81e146fa7f1b/frEvKtHszs.json")
    st_lottie(lottie_hello)  
 
    st.title('การจำเเนกเเมลงด้วยภาพ/Image Classifycation')
    predicted_name = ''
    df_1 = pd.read_excel("output.xlsx",index_col = 0)
    new_index = len(df_1)
    

    st.divider()
    

    css = '''
    <link href="https://fonts.googleapis.com/css2?family=Niramit:ital,wght@0,200;0,300;0,400;0,500;0,600;0,700;1,200;1,300;1,400;1,500;1,600;1,700&family=Outfit:wght@100..900&display=swap" rel="stylesheet">
    <p style="color:Black; font-size: 20px; font-family:Niramit;">เลือกวิธีการทำนายภาพเเมลง/Choose your classifycation method</p>
    '''
    st.markdown(css, unsafe_allow_html=True)

    css = '''
    <link href="https://fonts.googleapis.com/css2?family=Niramit:ital,wght@0,200;0,300;0,400;0,500;0,600;0,700;1,200;1,300;1,400;1,500;1,600;1,700&family=Outfit:wght@100..900&display=swap" rel="stylesheet">
    <p style="color:Black; font-size: 14px; font-family:Niramit;">วิธีที่ 1 อัปโหลดภาพ</p>
    '''
    st.markdown(css, unsafe_allow_html=True)
 
 
 
 
 
 
 
    
    my_image1 = st.file_uploader("อัปโหลดรูปภาพ/Upload a picture")
    if my_image1:
        st.image(my_image1)
    
    st.divider()
    
    css = '''
    <link href="https://fonts.googleapis.com/css2?family=Niramit:ital,wght@0,200;0,300;0,400;0,500;0,600;0,700;1,200;1,300;1,400;1,500;1,600;1,700&family=Outfit:wght@100..900&display=swap" rel="stylesheet">
    <p style="color:Black; font-size: 14px; font-family:Niramit;">วิธีที่ 2 ถ่ายภาพ</p>
    '''
    st.markdown(css, unsafe_allow_html=True)

    enable = st.checkbox("เปิดใช้งานกล้อง/Enable camera")
    


    my_image2 = st.camera_input("การถ่ายภาพ/Take a picture", disabled=not enable)
    if my_image2:
        st.image(my_image2)
     # Load the json file that contains the model's structure
    f = Path("model_structure_ny9new.json")
    model_structure = f.read_text()


    model = model_from_json(model_structure)
    model.load_weights("model_ny9new.weights.h5")

    if my_image1 or my_image2 :
        if st.button('Predict'):
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
                predicted_name = 'เรือด'
            elif predicted_class==6:
                predicted_name = 'โลน'
            elif predicted_class==7:
                predicted_name = 'ยุงลายบ้าน'
            elif predicted_class==8:
                predicted_name = 'ริ้นฝอยทราย'
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
                    elif predicted_name == 'เรือด':
                        st.image("A010_001.jpg")
                    elif predicted_name == 'โลน':
                        st.image("A015_101.jpg")
                    elif predicted_name == 'ยุงลายบ้าน':
                        st.image("A029_056.jpg")
                    elif predicted_name == 'ริ้นฝอยทราย':
                        st.image("A034_027.jpg")
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
                    elif predicted_name == 'เรือด':
                        st.image("A010.jpeg")
                    elif predicted_name == 'โลน':
                        st.image("A015.jpeg")
                    elif predicted_name == 'ยุงลายบ้าน':
                        st.image("A029.jpeg")
                    elif predicted_name == 'ริ้นฝอยทราย':
                        st.image("A034.jpeg")
                    
                    st.subheader("ส่วนที่เป็นพิษ") 
                    st.write(df['poision'][index])
                    st.subheader("อาการเมื่อถูกพิษ")
                    st.write(df['symptom'][index])
                    
                    if predicted_name == 'ด้วงก้นกระดก':
                        st.write("แผล:")
                        st.image("A002_แมลงก้นกระดก.jpg")
                    elif predicted_name == 'ด้วงน้ำมัน':
                        st.write("แผล:")
                        st.image("A001_แมลงด้วงน้ำมัน 2.jpg")
                    elif predicted_name == 'แมลงตด':
                        st.write("แผล:")
                        st.image("A003_แมลงตด.jpg")
                    elif predicted_name == 'ผึ้งหลวง':
                        st.write("แผล:")
                        st.image("A006_ผึ้งพันธุ์ 2.jpg")
                    elif predicted_name == 'เรือด':
                        st.write("แผล:")
                        st.image("A010_เรือด.jpg")
                    elif predicted_name == 'โลน':
                        st.write("แผล:")
                        st.image("A015_โลน.jpg")
                    elif predicted_name == 'ยุงลายบ้าน':
                        st.write("แผล:")
                        st.image("A029_ยุงลายบ้าน (ไข้เลือดออก).jpg")
                    elif predicted_name == 'ริ้นฝอยทราย':
                        st.write("แผล:")
                        st.image("A034_ริ้นฝอยทราย (โรคลิชมาเนีย).jpg")
                    else :
                        st.write("แผล: -")
                    st.write(df['อ้างอิง ภาพแผล'][index]) 
                    st.subheader("วิธีป้องกัน")
                    st.write(df['How to protect'][index])
                    st.write("แหล่งข้อมูล : " , df['แหล่งข้อมูล'][index])



            
        
    # ตั้งค่า API URL ของ SheetDB
    SHEETDB_URL = "https://sheetdb.io/api/v1/9qm7a3nx8jjvs"
    
    # สร้างฟอร์มใน Streamlit
    st.title("ประเมินประโยชน์การใช้งานของเว็บเเอปพลิเคชันการจำเเนกเเมลงที่มีพิษเเละเป็นอันตรายในประเทศไทย")
    
    with st.form("data_form"):
        city = st.selectbox("จังหวัดที่พบแมลง (Province)", ["กรุงเทพมหานคร/Krung Thep Maha Nakhon (Bangkok)","กระบี่/Krabi","กาญจนบุรี/Kanchanaburi","กาฬสินธุ์/Kalasin","กำแพงเพชร/Kamphaeng Phet","ขอนแก่น/Khon Kaen","จันทบุรี/Chanthaburi","ฉะเชิงเทรา/Chachoengsao","ชลบุรี/Chonburi","ชัยนาท/Chainat","ชัยภูมิ/Chaiyaphum","ชุมพร/Chumphon","เชียงราย/Chiang Rai","เชียงใหม่/Chiang Mai","ตรัง/Trang ","ตราด/Trat","ตาก/Tak","นครนายก/Nakhon Nayok","นครปฐม/Nakhon Pathom","นครพนม/Nakhon Phanom",
    "นครราชสีมา/Nakhon Ratchasima",
    "นครศรีธรรมราช/Nakhon Si Thammarat",
     "นครสวรรค์/Nakhon Sawan",
     "นนทบุรี/Nonthaburi",
     "นราธิวาส/Narathiwat",
     "น่าน/Nan",
    "บึงกาฬ/Bueng Kan",
     "บุรีรัมย์/Buriram",
     "ปทุมธานี/Pathum Thani",
     "ประจวบคีรีขันธ์/Prachuap Khiri Khan ",
     "ปราจีนบุรี/Prachinburi ",                                                              
    "ปัตตานี/Pattani ",
     "พระนครศรีอยุธยา/Phra Nakhon Si Ayutthaya ",
    "พะเยา/Phayao ",
     "พังงา/Phang Nga ",
     "พัทลุง/Phatthalung",
     "พิจิตร/Phichit ",
     "พิษณุโลก/Phitsanulok",
     "เพชรบุรี/Phetchaburi",
     "เพชรบูรณ์/Phetchabun",
     "แพร่/Phrae ",
     "ภูเก็ต/Phuket ",
     "มหาสารคาม/Maha Sarakham ",
     "มุกดาหาร/Mukdahan ",
     "แม่ฮ่องสอน/Mae Hong Son ",
     "ยโสธร/Yasothon ",
     "ยะลา/Yala ",
     "ร้อยเอ็ด/Roi Et ",
     "ระนอง/Ranong ",
     "ระยอง/Rayong ",
     "ราชบุรี/Ratchaburi ",
     "ลพบุรี/Lopburi ",
     "ลำปาง/Lampang ",
     "ลำพูน/Lamphun ",
     "เลย/Loei ",
     "ศรีสะเกษ/Sisaket ",
     "สกลนคร/Sakon Nakhon ",
     "สงขลา/Songkhla ",
     "สตูล/Satun ",
     "สมุทรปราการ/Samut Prakan ",
     "สมุทรสงคราม/Samut Songkhram ",
     "สมุทรสาคร/Samut Sakhon ",
     "สระแก้ว/Sa Kaeo ",
     "สระบุรี/Saraburi ",
     "สิงห์บุรี/Sing Buri ",
     "สุโขทัย/Sukhothai ",
     "สุพรรณบุรี/Suphan Buri ",
     "สุราษฎร์ธานี/Surat Thani ",
     "สุรินทร์/Surin ",
     "หนองคาย/Nong Khai ",
     "หนองบัวลำภู/Nong Bua Lamhu ",
     "อ่างทอง Ang/Thong ",
     "อำนาจเจริญ/Amnat Charen ",
     "อุดรธานี/Udon Thani ",
     "อุตรดิตถ์/Uttaradit ",
     "อุทัยธานี/Uthai Thani",
     "อุบลราชธานี/Ubon Ratchathani" ])
        predicted_name = st.selectbox("ชนิดของแมลงที่พบ", ["ด้วงน้ำมัน", "ด้วงก้นกระดก", "แมลงตด", "แมลงบุกบ้าน", "ผึ้งหลวง",  "เรือด",
        "โลน","ยุงลายบ้าน","ริ้นฝอยทราย"])
        
        performance = st.selectbox("ความถูกต้องของเว็บแอปพลิเคชั่น", ["ทำนายภาพได้ถูกต้อง", "ทำนายภาพได้ไม่ถูกต้อง"])
        check = st.selectbox("ประเมินประโยชน์จากการใช้งานของเว็บแอปพลิเคชั่น", ["⭐⭐⭐⭐⭐ ดีมาก(Excellent)", "⭐⭐⭐⭐ ดี(Good)", "⭐⭐⭐ พอใช้(Fair)", "⭐⭐ น้อย(Poor)", "⭐ น้อยที่สุด(Very poor)"])
        Feed_back = st.text_input("ข้อเสนอเเนะ(Enter your comments here)")

        submitted = st.form_submit_button("ส่งข้อมูล")
        
        
        if submitted:
            # ส่งข้อมูลไปยัง SheetDB
            data = {"data": [{"City": city, "Insecct": predicted_name, "Check": check, "Feedback": Feed_back, "Performmance": performance }]}
            response = requests.post(SHEETDB_URL, json=data)
    
            if response.status_code == 201:
                st.success("บันทึกข้อมูลสำเร็จ!")
            else:
                st.error(f"เกิดข้อผิดพลาด: {response.text}")
