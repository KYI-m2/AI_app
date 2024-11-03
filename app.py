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

page_bg_img = """
<style>
[data-testid="stAppViewContainer"]{.magicpattern { 
  width: 100%;
  height: 100%;
  background-size: cover;
  background-position: center center;
  background-repeat: repeat;
  background-image: url("data:image/svg+xml;utf8,%3Csvg viewBox=%220 0 2000 1400%22 xmlns=%22http:%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Cdefs%3E%3Cfilter id=%22b%22 x=%22-200%25%22 y=%22-200%25%22 width=%22500%25%22 height=%22500%25%22%3E%3CfeGaussianBlur in=%22SourceGraphic%22 stdDeviation=%2220%22%2F%3E%3C%2Ffilter%3E%3C%2Fdefs%3E%3Cpath fill=%22%2382daa8%22 d=%22M0 0h2000v1400H0z%22%2F%3E%3Cellipse cx=%2295.29%22 cy=%2257.455%22 rx=%221.581%22 ry=%221.152%22 fill=%22%23fff%22 opacity=%22.426%22%2F%3E%3Cellipse cx=%22322.77%22 cy=%2239.642%22 rx=%222.412%22 ry=%221.97%22 fill=%22%23fff%22 opacity=%22.206%22%2F%3E%3Cellipse cx=%22475.219%22 cy=%2217.504%22 rx=%221.469%22 ry=%221.093%22 fill=%22%23fff%22 opacity=%22-.046%22%2F%3E%3Cellipse cx=%22780.189%22 cy=%2224.15%22 rx=%221.656%22 ry=%221.525%22 fill=%22%23fff%22 opacity=%22.703%22%2F%3E%3Cellipse cx=%22932.865%22 cy=%22104.263%22 rx=%221.931%22 ry=%221.454%22 fill=%22%23fff%22 opacity=%22.264%22%2F%3E%3Cellipse cx=%221096.844%22 cy=%2227.901%22 rx=%221.291%22 ry=%221.185%22 fill=%22%23fff%22 opacity=%22.266%22%2F%3E%3Cellipse cx=%221393.197%22 cy=%2215.991%22 rx=%221.178%22 ry=%221.036%22 fill=%22%23fff%22 opacity=%22.401%22%2F%3E%3Cellipse cx=%221535.537%22 cy=%221.011%22 rx=%221.562%22 ry=%221.107%22 fill=%22%23fff%22 opacity=%22.719%22%2F%3E%3Cellipse cx=%221731.71%22 cy=%2253.891%22 rx=%221.847%22 ry=%221.596%22 fill=%22%23fff%22 opacity=%22.409%22%2F%3E%3Cellipse cx=%221809.421%22 cy=%2270.544%22 rx=%221.514%22 ry=%221.128%22 fill=%22%23fff%22 opacity=%22.621%22%2F%3E%3Cellipse cx=%22199.057%22 cy=%22152.836%22 rx=%221.661%22 ry=%221.429%22 fill=%22%23fff%22 opacity=%22.751%22%2F%3E%3Cellipse cx=%22359.412%22 cy=%22233.151%22 rx=%221.313%22 ry=%221.029%22 fill=%22%23fff%22 opacity=%22.395%22%2F%3E%3Cellipse cx=%22483.839%22 cy=%22254.329%22 rx=%221.644%22 ry=%221.425%22 fill=%22%23fff%22 opacity=%22-.129%22%2F%3E%3Cellipse cx=%22609.657%22 cy=%22152.948%22 rx=%221.172%22 ry=%221.022%22 fill=%22%23fff%22 opacity=%22.21%22%2F%3E%3Cellipse cx=%22811.784%22 cy=%22205.971%22 rx=%222.116%22 ry=%221.821%22 fill=%22%23fff%22 opacity=%22.493%22%2F%3E%3Cellipse cx=%221112.715%22 cy=%22213.402%22 rx=%221.776%22 ry=%221.479%22 fill=%22%23fff%22 opacity=%22.067%22%2F%3E%3Cellipse cx=%221219.905%22 cy=%22220.514%22 rx=%221.504%22 ry=%221.119%22 fill=%22%23fff%22 opacity=%22.586%22%2F%3E%3Cellipse cx=%221581.48%22 cy=%22235.309%22 rx=%221.353%22 ry=%221.12%22 fill=%22%23fff%22 opacity=%22.303%22%2F%3E%3Cellipse cx=%221752.849%22 cy=%22209.581%22 rx=%221.753%22 ry=%221.274%22 fill=%22%23fff%22 opacity=%22.9%22%2F%3E%3Cellipse cx=%221991.813%22 cy=%22172.557%22 rx=%222.034%22 ry=%221.865%22 fill=%22%23fff%22 opacity=%22.652%22%2F%3E%3Cellipse cx=%2262.772%22 cy=%22290.052%22 rx=%221.569%22 ry=%221.134%22 fill=%22%23fff%22 opacity=%22.31%22%2F%3E%3Cellipse cx=%22237.017%22 cy=%22282.975%22 rx=%221.331%22 ry=%221.105%22 fill=%22%23fff%22 opacity=%22.378%22%2F%3E%3Cellipse cx=%22570.221%22 cy=%22310.291%22 rx=%222.065%22 ry=%221.694%22 fill=%22%23fff%22 opacity=%22.463%22%2F%3E%3Cellipse cx=%22612.666%22 cy=%22336.807%22 rx=%221.515%22 ry=%221.204%22 fill=%22%23fff%22 opacity=%22-.008%22%2F%3E%3Cellipse cx=%22971.344%22 cy=%22349.82%22 rx=%221.676%22 ry=%221.505%22 fill=%22%23fff%22 opacity=%22.681%22%2F%3E%3Cellipse cx=%221176.615%22 cy=%22292.303%22 rx=%222.314%22 ry=%221.887%22 fill=%22%23fff%22 opacity=%22.546%22%2F%3E%3Ccircle cx=%221251.656%22 cy=%22308.162%22 fill=%22%23fff%22 opacity=%22.106%22 r=%221.158%22%2F%3E%3Cellipse cx=%221401.373%22 cy=%22309.763%22 rx=%221.809%22 ry=%221.75%22 fill=%22%23fff%22 opacity=%22-.013%22%2F%3E%3Cellipse cx=%221686.096%22 cy=%22332.027%22 rx=%221.224%22 ry=%221.154%22 fill=%22%23fff%22 opacity=%22.724%22%2F%3E%3Cellipse cx=%221820.273%22 cy=%22397.404%22 rx=%221.714%22 ry=%221.679%22 fill=%22%23fff%22 opacity=%22.317%22%2F%3E%3Cellipse cx=%2293.362%22 cy=%22486.027%22 rx=%222.074%22 ry=%221.898%22 fill=%22%23fff%22 opacity=%22-.012%22%2F%3E%3Cellipse cx=%22313.612%22 cy=%22452.431%22 rx=%221.594%22 ry=%221.441%22 fill=%22%23fff%22 opacity=%22.205%22%2F%3E%3Cellipse cx=%22419.18%22 cy=%22543.753%22 rx=%221.477%22 ry=%221.141%22 fill=%22%23fff%22 opacity=%22.326%22%2F%3E%3Cellipse cx=%22652.286%22 cy=%22550.994%22 rx=%221.352%22 ry=%221.329%22 fill=%22%23fff%22 opacity=%22.12%22%2F%3E%3Cellipse cx=%22947.152%22 cy=%22544.397%22 rx=%221.571%22 ry=%221.135%22 fill=%22%23fff%22 opacity=%22.612%22%2F%3E%3Cellipse cx=%221048.563%22 cy=%22434.723%22 rx=%222.072%22 ry=%221.572%22 fill=%22%23fff%22 opacity=%22.039%22%2F%3E%3Cellipse cx=%221244.422%22 cy=%22526.791%22 rx=%221.344%22 ry=%221.049%22 fill=%22%23fff%22 opacity=%22.142%22%2F%3E%3Cellipse cx=%221409.538%22 cy=%22475.367%22 rx=%221.166%22 ry=%221.104%22 fill=%22%23fff%22 opacity=%22-.098%22%2F%3E%3Cellipse cx=%221731.352%22 cy=%22460.324%22 rx=%221.247%22 ry=%221.065%22 fill=%22%23fff%22 opacity=%22.674%22%2F%3E%3Cellipse cx=%221905.677%22 cy=%22473.843%22 rx=%222.013%22 ry=%221.855%22 fill=%22%23fff%22 opacity=%22.143%22%2F%3E%3Cellipse cx=%22116.689%22 cy=%22662.254%22 rx=%221.841%22 ry=%221.688%22 fill=%22%23fff%22 opacity=%22.357%22%2F%3E%3Cellipse cx=%22258.544%22 cy=%22611.592%22 rx=%222.128%22 ry=%221.812%22 fill=%22%23fff%22 opacity=%22.078%22%2F%3E%3Cellipse cx=%22591.762%22 cy=%22677.372%22 rx=%221.398%22 ry=%221.062%22 fill=%22%23fff%22 opacity=%22.552%22%2F%3E%3Cellipse cx=%22739.937%22 cy=%22678.156%22 rx=%221.824%22 ry=%221.636%22 fill=%22%23fff%22 opacity=%22.625%22%2F%3E%3Cellipse cx=%22980.854%22 cy=%22583.365%22 rx=%221.788%22 ry=%221.55%22 fill=%22%23fff%22 opacity=%22-.135%22%2F%3E%3Cellipse cx=%221109.84%22 cy=%22597.916%22 rx=%221.508%22 ry=%221.054%22 fill=%22%23fff%22 opacity=%22.322%22%2F%3E%3Cellipse cx=%221278.329%22 cy=%22571.663%22 rx=%221.794%22 ry=%221.316%22 fill=%22%23fff%22 opacity=%22.597%22%2F%3E%3Cellipse cx=%221509.077%22 cy=%22568.14%22 rx=%221.601%22 ry=%221.289%22 fill=%22%23fff%22 opacity=%22.243%22%2F%3E%3Cellipse cx=%221659.276%22 cy=%22691.67%22 rx=%221.18%22 ry=%221.047%22 fill=%22%23fff%22 opacity=%22.393%22%2F%3E%3Cellipse cx=%221875.442%22 cy=%22639.172%22 rx=%221.637%22 ry=%221.569%22 fill=%22%23fff%22 opacity=%22.951%22%2F%3E%3Cellipse cx=%2273.047%22 cy=%22757.171%22 rx=%221.466%22 ry=%221.257%22 fill=%22%23fff%22 opacity=%22.288%22%2F%3E%3Cellipse cx=%22228.639%22 cy=%22784.5%22 rx=%221.859%22 ry=%221.728%22 fill=%22%23fff%22 opacity=%22-.049%22%2F%3E%3Cellipse cx=%22484.138%22 cy=%22795.157%22 rx=%221.541%22 ry=%221.521%22 fill=%22%23fff%22 opacity=%22.878%22%2F%3E%3Cellipse cx=%22784.27%22 cy=%22713.867%22 rx=%221.802%22 ry=%221.582%22 fill=%22%23fff%22 opacity=%22.607%22%2F%3E%3Cellipse cx=%22939.261%22 cy=%22752.582%22 rx=%221.936%22 ry=%221.573%22 fill=%22%23fff%22 opacity=%22.309%22%2F%3E%3Cellipse cx=%221155.888%22 cy=%22722.316%22 rx=%221.56%22 ry=%221.458%22 fill=%22%23fff%22 opacity=%22.393%22%2F%3E%3Cellipse cx=%221316.002%22 cy=%22774.629%22 rx=%222.218%22 ry=%221.724%22 fill=%22%23fff%22 opacity=%22.876%22%2F%3E%3Cellipse cx=%221579.966%22 cy=%22716.49%22 rx=%222.091%22 ry=%221.919%22 fill=%22%23fff%22 opacity=%22.065%22%2F%3E%3Cellipse cx=%221613.764%22 cy=%22775.396%22 rx=%222.056%22 ry=%221.847%22 fill=%22%23fff%22 opacity=%22.039%22%2F%3E%3Cellipse cx=%221896.322%22 cy=%22717.32%22 rx=%221.477%22 ry=%221.454%22 fill=%22%23fff%22 opacity=%22.082%22%2F%3E%3Cellipse cx=%2245.336%22 cy=%22919.414%22 rx=%221.526%22 ry=%221.44%22 fill=%22%23fff%22 opacity=%22.392%22%2F%3E%3Cellipse cx=%22256.791%22 cy=%22934.434%22 rx=%221.967%22 ry=%221.846%22 fill=%22%23fff%22 opacity=%22.268%22%2F%3E%3Cellipse cx=%22512.795%22 cy=%22859.536%22 rx=%221.464%22 ry=%221.259%22 fill=%22%23fff%22 opacity=%22.288%22%2F%3E%3Cellipse cx=%22614.371%22 cy=%22844.891%22 rx=%221.848%22 ry=%221.719%22 fill=%22%23fff%22 opacity=%22.05%22%2F%3E%3Cellipse cx=%22920.222%22 cy=%22901.532%22 rx=%221.774%22 ry=%221.683%22 fill=%22%23fff%22 opacity=%22.204%22%2F%3E%3Cellipse cx=%221040.159%22 cy=%22936.014%22 rx=%221.533%22 ry=%221.037%22 fill=%22%23fff%22 opacity=%22-.18%22%2F%3E%3Cellipse cx=%221209.835%22 cy=%22969.617%22 rx=%222.342%22 ry=%221.92%22 fill=%22%23fff%22 opacity=%22.349%22%2F%3E%3Cellipse cx=%221473.706%22 cy=%22864.469%22 rx=%222.147%22 ry=%221.848%22 fill=%22%23fff%22 opacity=%22.825%22%2F%3E%3Cellipse cx=%221651.011%22 cy=%22945.147%22 rx=%222.089%22 ry=%221.708%22 fill=%22%23fff%22 opacity=%22-.208%22%2F%3E%3Cellipse cx=%221864.078%22 cy=%22920.38%22 rx=%222.298%22 ry=%221.925%22 fill=%22%23fff%22 opacity=%22.323%22%2F%3E%3Cellipse cx=%22165.469%22 cy=%221018.841%22 rx=%221.909%22 ry=%221.428%22 fill=%22%23fff%22 opacity=%22.816%22%2F%3E%3Cellipse cx=%22261.63%22 cy=%22998.653%22 rx=%221.123%22 ry=%221.067%22 fill=%22%23fff%22 opacity=%22.752%22%2F%3E%3Cellipse cx=%22475.356%22 cy=%22991.58%22 rx=%221.893%22 ry=%221.684%22 fill=%22%23fff%22 opacity=%22-.207%22%2F%3E%3Cellipse cx=%22774.22%22 cy=%221046.366%22 rx=%221.389%22 ry=%221.384%22 fill=%22%23fff%22 opacity=%22.806%22%2F%3E%3Cellipse cx=%22982.223%22 cy=%221027.081%22 rx=%221.845%22 ry=%221.802%22 fill=%22%23fff%22 opacity=%22-.04%22%2F%3E%3Cellipse cx=%221091.845%22 cy=%221102.67%22 rx=%221.451%22 ry=%221.333%22 fill=%22%23fff%22 opacity=%22.156%22%2F%3E%3Cellipse cx=%221346.489%22 cy=%221061.439%22 rx=%221.487%22 ry=%221.42%22 fill=%22%23fff%22 opacity=%22.036%22%2F%3E%3Cellipse cx=%221420.449%22 cy=%221095.465%22 rx=%221.981%22 ry=%221.974%22 fill=%22%23fff%22 opacity=%22.215%22%2F%3E%3Cellipse cx=%221695.613%22 cy=%221065.789%22 rx=%222.263%22 ry=%221.779%22 fill=%22%23fff%22 opacity=%22.341%22%2F%3E%3Cellipse cx=%221923.527%22 cy=%221082.074%22 rx=%221.6%22 ry=%221.472%22 fill=%22%23fff%22 opacity=%22.034%22%2F%3E%3Cellipse cx=%22184.155%22 cy=%221166.694%22 rx=%221.656%22 ry=%221.163%22 fill=%22%23fff%22 opacity=%22.697%22%2F%3E%3Cellipse cx=%22222.084%22 cy=%221236.182%22 rx=%222.197%22 ry=%221.723%22 fill=%22%23fff%22 opacity=%22-.035%22%2F%3E%3Cellipse cx=%22594.421%22 cy=%221161.417%22 rx=%221.486%22 ry=%221.228%22 fill=%22%23fff%22 opacity=%22.564%22%2F%3E%3Cellipse cx=%22715.075%22 cy=%221165.618%22 rx=%222.122%22 ry=%221.674%22 fill=%22%23fff%22 opacity=%22.116%22%2F%3E%3Cellipse cx=%221078.691%22 cy=%221176.722%22 rx=%221.778%22 ry=%221.329%22 fill=%22%23fff%22 opacity=%22.392%22%2F%3E%3Cellipse cx=%221363.959%22 cy=%221179.448%22 rx=%221.317%22 ry=%221.176%22 fill=%22%23fff%22 opacity=%22.13%22%2F%3E%3Cellipse cx=%221568.479%22 cy=%221178.052%22 rx=%221.947%22 ry=%221.602%22 fill=%22%23fff%22 opacity=%22-.069%22%2F%3E%3Cellipse cx=%221700.25%22 cy=%221225.136%22 rx=%221.761%22 ry=%221.286%22 fill=%22%23fff%22 opacity=%22.454%22%2F%3E%3Cellipse cx=%221927.246%22 cy=%221177.26%22 rx=%221.646%22 ry=%221.265%22 fill=%22%23fff%22 opacity=%22.285%22%2F%3E%3Cellipse cx=%22116.504%22 cy=%221260.936%22 rx=%222.254%22 ry=%221.945%22 fill=%22%23fff%22 opacity=%22.427%22%2F%3E%3Cellipse cx=%22217.957%22 cy=%221267.221%22 rx=%221.77%22 ry=%221.338%22 fill=%22%23fff%22 opacity=%22.194%22%2F%3E%3Cellipse cx=%22499.864%22 cy=%221370.956%22 rx=%221.576%22 ry=%221.544%22 fill=%22%23fff%22 opacity=%22.311%22%2F%3E%3Cellipse cx=%22683.414%22 cy=%221373.34%22 rx=%221.929%22 ry=%221.772%22 fill=%22%23fff%22 opacity=%22.21%22%2F%3E%3Cellipse cx=%22826.183%22 cy=%221345.278%22 rx=%221.697%22 ry=%221.336%22 fill=%22%23fff%22 opacity=%22-.124%22%2F%3E%3Cellipse cx=%221170.121%22 cy=%221296.861%22 rx=%221.56%22 ry=%221.213%22 fill=%22%23fff%22 opacity=%22-.088%22%2F%3E%3Cellipse cx=%221328.278%22 cy=%221329.12%22 rx=%221.47%22 ry=%221.05%22 fill=%22%23fff%22 opacity=%22.218%22%2F%3E%3Cellipse cx=%221591.508%22 cy=%221293.201%22 rx=%222.07%22 ry=%221.772%22 fill=%22%23fff%22 opacity=%22.365%22%2F%3E%3Cellipse cx=%221674.316%22 cy=%221299.174%22 rx=%222.059%22 ry=%221.961%22 fill=%22%23fff%22 opacity=%22-.086%22%2F%3E%3Cellipse cx=%221945.74%22 cy=%221313.281%22 rx=%221.365%22 ry=%221.068%22 fill=%22%23fff%22 opacity=%22.429%22%2F%3E%3Cg transform=%22rotate(-62.678 467.253 -682.914)%22%3E%3Cdefs%3E%3ClinearGradient id=%22a%22 x1=%220%22 y1=%221%22 x2=%22219.351%22 y2=%221%22 gradientUnits=%22userSpaceOnUse%22%3E%3Cstop stop-color=%22%23fff%22%2F%3E%3Cstop offset=%22.3%22 stop-color=%22%23fff%22 stop-opacity=%22.1%22%2F%3E%3Cstop offset=%22.7%22 stop-color=%22%23fff%22 stop-opacity=%220%22%2F%3E%3C%2FlinearGradient%3E%3C%2Fdefs%3E%3Crect x=%22-10.968%22 y=%22-12.5%22 width=%2287.74%22 height=%2225%22 rx=%2225%22 ry=%2225%22 fill=%22url(%23a)%22 filter=%22url(%23b)%22 opacity=%22.4%22%2F%3E%3Crect width=%22131.611%22 height=%228%22 rx=%228%22 ry=%228%22 fill=%22url(%23a)%22%2F%3E%3C%2Fg%3E%3Cg transform=%22rotate(-59.569 778.432 -241.264)%22 fill=%22url(%23a)%22%3E%3Crect x=%22-16.443%22 y=%22-12.5%22 width=%22131.546%22 height=%2225%22 rx=%2225%22 ry=%2225%22 filter=%22url(%23b)%22 opacity=%22.4%22%2F%3E%3Crect width=%22197.319%22 height=%228%22 rx=%228%22 ry=%228%22%2F%3E%3C%2Fg%3E%3Cg transform=%22rotate(-57.315 1152.894 -517.987)%22 fill=%22url(%23a)%22%3E%3Crect x=%22-16.785%22 y=%22-12.5%22 width=%22134.277%22 height=%2225%22 rx=%2225%22 ry=%2225%22 filter=%22url(%23b)%22 opacity=%22.4%22%2F%3E%3Crect width=%22201.415%22 height=%228%22 rx=%228%22 ry=%228%22%2F%3E%3C%2Fg%3E%3Cg transform=%22rotate(-63.68 1198.859 75.67)%22 fill=%22url(%23a)%22%3E%3Crect x=%22-12.815%22 y=%22-12.5%22 width=%22102.519%22 height=%2225%22 rx=%2225%22 ry=%2225%22 filter=%22url(%23b)%22 opacity=%22.4%22%2F%3E%3Crect width=%22153.779%22 height=%228%22 rx=%228%22 ry=%228%22%2F%3E%3C%2Fg%3E%3Cg transform=%22rotate(-63.156 1681.004 -447.73)%22 fill=%22url(%23a)%22%3E%3Crect x=%22-10.97%22 y=%22-12.5%22 width=%2287.762%22 height=%2225%22 rx=%2225%22 ry=%2225%22 filter=%22url(%23b)%22 opacity=%22.4%22%2F%3E%3Crect width=%22131.642%22 height=%228%22 rx=%228%22 ry=%228%22%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E");
}

</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)



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
    destination = "model_100.weights.h5"  # ชื่อไฟล์ที่ต้องการบันทึก
    download_file_from_google_drive(file_id, destination)



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
    st.info("KYI-Know Your Insect เป็นเว็บแอปพลิเคชันที่สร้างขึ้นด้วย Machine Learning, Python เเละ Streamlit   จัดทำขึ้นเป็นโครงงานเพื่อสร้างแหล่งข้อมูลแมลงที่มีพิษเเละเป็นอันตรายในประเทศไทยที่น่าเชื่อถือและสามารถเข้าถึงได้ง่าย เป็นโครงงานที่เกิดจากการผสมผสานของความรู้และเทคโนโลยี นำเสนอโดยนักเรียนชั้นมัธยมศึกษาปีที่ 2  จากโรงเรียนบดินทรเดชา(สิงห์ สิงหเสนี), จังหวัดกรุงเทพมหานคร, ประเทศไทย เว็บเเอปพลิเคชันนี้สามารถทำอะไรได้บ้าง? เพียงเเค่อัปโหลดภาพเเมลง หรือ ใช้การถ่ายภาพเเมลงที่สนใจลงในเว็บเเอปพลิเคชัน   เว็บเเอปพลิเคชันนี้ก็จะสามารถจำเเนกเเมลงที่มีพิษเเละเป็นอันตรายที่พบได้ในประเทศไทยได้นอกจากนี้ยังมี Search Bar ให้ผู้ใช้งานได้ค้นหาด้วยชื่อเเมลงอีกด้วย")
    st.divider()
    st.info("This is a Web-Application created with ML, Python, Streamlit made as a project to create a reliable and accessable data source of dangerous insects in Thailand, combining knowledge and technology, Brought to you by the M.2 students from Bodindecha (Sing Singhaseni) School, based in Bangkok, Thailand.  What can this Web Application do? It can be used to classify the  dangerous insects found mostly in Thailand with the method of just uploading your desired picture.")
    st.toast("Lets get started 🏁 ")
    st.toast("welcome to our web-based application!📚")  
    col1, col2, col3 ,col4 ,col5 = st.columns(5)
    with col2:
        st.image("Insect.jpg")
    with col3:
        st.image("robot.jpg",width=175)
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
        results = df[df["insect_name"].str.lower() == search_query.lower()]
        insect_name = search_query
        if not results.empty:
            st.write("Results:")
            for index, row in results.iterrows():
                if insect_name == 'ด้วงน้ำมัน':
                    st.image("A001_001.jpg")
                elif insect_name == 'ด้วงก้นกระดก':
                    st.image("A002_027.jpg")
                elif insect_name == 'แมลงตด':
                    st.image("A003_021.jpg")
                elif insect_name == 'แมลงบุกบ้าน':
                    st.image("A004_006.jpg")
                elif insect_name == 'ผึ้งหลวง':
                    st.image("A005_019.jpg")
                elif insect_name == 'ผึ้งเลี้ยง':
                    st.image("A006_001.jpg")
                elif insect_name == 'ตัวต่อหัวเสือ':
                    st.image("A007_083.jpg")
                elif insect_name == 'แตน':
                    st.image("A008_008.jpg")
                elif insect_name == 'มวนเพชรฆาต':
                    st.image("A009_001.jpg")
                elif insect_name == 'เรือด':
                    st.image("A010_001.jpg")
                elif insect_name == 'หนอนบุ้งร่าน':
                    st.image("A11_080.jpg")
                elif insect_name == 'แมลงสาบอเมริกัน':
                    st.image("A012_003.jpg")
                elif insect_name == 'แมลงสาบเยอรมัน':
                    st.image("A013_001.jpg")
                elif insect_name == 'แมลงสาบผี':
                    st.image("A014_031.jpg")
                elif insect_name == 'โลน':
                    st.image("A015_101.jpg")
                elif insect_name == 'มดคันไฟ':
                    st.image("A016_073.jpg")
                elif insect_name == 'มดง่าม':
                    st.image("A017_084.jpg")
                elif insect_name == 'มดดำ':
                    st.image("A018_098.jpg")
                elif insect_name == 'มดตะนอย':
                    st.image("A019_085.jpg")
                elif insect_name == 'แมลงวันบ้าน':
                    st.image("A020_052.jpg")
                elif insect_name == 'หมาร่า':
                    st.image("A021_072.jpg")
                elif insect_name == 'แมลงวันหัวเขียว':
                    st.image("A022_001.jpg")
                elif insect_name == 'แมลงวันคอกสัตว์':
                    st.image("A023_001.jpg")
                elif insect_name == 'แมลงวันตา':
                    st.image("A024_070.jpg")
                elif insect_name == 'แมลงวันหลังลาย':
                    st.image("A025_001.jpg")
                elif insect_name == 'แมลงวันเซ็ทซี':
                    st.image("A026_094.jpg")
                elif insect_name == 'ยุงก้นปล่อง':
                    st.image("A027_096.jpg")
                elif insect_name == 'ยุงรำคาญ':
                    st.image("A028_001.jpg")
                elif insect_name == 'ยุงลายบ้าน':
                    st.image("A029_056.jpg")
                elif insect_name == 'ยุงลายสวน':
                    st.image("A030_085.jpg")
                elif insect_name == 'ยุงลายเสือ':
                    st.image("A031_055.jpg")
                elif insect_name == 'ริ้นดำ หรือตัวคุ่น':
                    st.image("A032_099.jpg")
                elif insect_name == 'ริ้นน้ำเค็ม':
                    st.image("A033_098.jpg")
                elif insect_name == 'ริ้นฝอยทราย':
                    st.image("A034_027.jpg")
                elif insect_name == 'หมัด':
                    st.image("A035_025.jpg")
                else:
                    st.image("A036_028.jpg")
                

                st.write(row['อ้างอิงตัวอย่างแมลง'])
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
                elif insect_name == 'ด้วงน้ำมัน':
                    st.write("แผล:")
                    st.image("A001_แมลงด้วงน้ำมัน 2.jpg")
                elif insect_name == 'แมลงตด':
                    st.write("แผล:")
                    st.image("A003_แมลงตด.jpg")
                elif insect_name == 'ผึ้งหลวง':
                    st.write("แผล:")
                    st.image("A005_ผึ้งหลวง.jpg")
                elif insect_name == 'ผึ้งพันธุ์':
                    st.write("แผล:")
                    st.image("A006_ผึ้งพันธุ์ 2.jpg")
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
                    st.image("A010_เรือด 2.jpg")
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
                    st.image("A018_มดดำ 2.jpg")
                elif insect_name == 'มดตะนอย':
                    st.write("แผล:")
                    st.image("A019_มดตะนอย 2.jpg")
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
                    st.image("A028_ยุงรำคาญ (โรคไข้สมองอักเสบ).jpg")
                elif insect_name == 'ยุงลายบ้าน':
                    st.write("แผล:")
                    st.image("A029_ยุงลายบ้าน (ไข้เลือดออก).jpg")
                elif insect_name == 'ยุงลายสวน':
                    st.write("แผล:")
                    st.image("A030_ยุงลายสวน (ชิคุนกุนยา).jpg")
                elif insect_name == 'ยุงลายเสือ':
                    st.write("แผล:")
                    st.image("A031_ยุงลายเสือ (โรคเท้าช้าง).jpg")
                elif insect_name == 'ริ้นดำ':
                    st.write("แผล:")
                    st.image("A032_ริ้นดำ.jpg")
                elif insect_name == 'ริ้นน้ำเค็ม':
                    st.write("แผล:")
                    st.image("A033_ริ้นน้ำเค็ม 2.jpg")
                elif insect_name == 'ริ้นฝอยทราย':
                    st.write("แผล:")
                    st.image("A034_ริ้นฝอยทราย (โรคลิชมาเนีย).jpg")
                elif insect_name == 'หมัดสุนัข':
                    st.write("แผล:")
                    st.image("A035_หมัดสุนัข 2.jpg")
                elif insect_name == 'เหา':
                    st.write("แผล:")
                    st.image("A036_เหา 2.jpg")
                else:
                    st.write("แผล: -")
                st.write(row['อ้างอิง ภาพแผล'])
                
                st.write("How to protect:", row['How to protect'])
                st.write("---")  # Separator for clarity
                st.write(row['แหล่งข้อมูล'])
        else:
            st.write("No results found.")
        

if choose == "Contact Us" :
    st.title('Contact Us')
    
    st.write("ช่องทางการติดต่อของเรา: \n Gmail: webapplication.m2@gmail.com")
    


if choose == 'Image Classification' :
    st.title('การจำเเนกเเมลงด้วยภาพ/Image Classifycation')
    predicted_name = ''
    df_1 = pd.read_excel("output.xlsx",index_col = 0)
    new_index = len(df_1)
    css = '''
    <link href="https://fonts.googleapis.com/css2?family=Niramit:ital,wght@0,200;0,300;0,400;0,500;0,600;0,700;1,200;1,300;1,400;1,500;1,600;1,700&family=Outfit:wght@100..900&display=swap" rel="stylesheet">
    <p style="color:Black; font-size: 20px; font-family:Niramit;">กรอกข้อมูลผู้ใช้/Enter your information</p>
    '''
    st.markdown(css, unsafe_allow_html=True)

    gender = st.selectbox("เพศ (Gender)", ["ผู้ชาย/male", "ผู้หญิง/female", "อื่นๆ/other"])
    st.write("ตัวอย่างการกรอกข้อมูล/Example of data input 20/2/2567 18:30")
    date = st.text_input("วันที่ (Date) dd/mm/yyyy พุทธศักราช")
    time = st.text_input("เวลา (Time) xx:xx ")
    age = st.slider("อายุ (Age)", 0, 100)
    city = st.selectbox("จังหวัด (Province)", ["กรุงเทพมหานคร/Krung Thep Maha Nakhon (Bangkok)","กระบี่/Krabi","กาญจนบุรี/Kanchanaburi","กาฬสินธุ์/Kalasin","กำแพงเพชร/Kamphaeng Phet","ขอนแก่น/Khon Kaen","จันทบุรี/Chanthaburi","ฉะเชิงเทรา/Chachoengsao","ชลบุรี/Chonburi","ชัยนาท/Chainat","ชัยภูมิ/Chaiyaphum","ชุมพร/Chumphon","เชียงราย/Chiang Rai","เชียงใหม่/Chiang Mai","ตรัง/Trang ","ตราด/Trat","ตาก/Tak","นครนายก/Nakhon Nayok","นครปฐม/Nakhon Pathom","นครพนม/Nakhon Phanom",
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
                    elif predicted_name == 'ด้วงน้ำมัน':
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
 
