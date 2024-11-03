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
page_img_bg ="""
<style>
[data-testid="stAppViewContainer"] {
    background-color: .magicpattern { 
  width: 100%;
  height: 100%;
  background-size: cover;
  background-position: center center;
  background-repeat: repeat;
  background-image: url("data:image/svg+xml;utf8,%3Csvg viewBox=%220 0 2000 1400%22 xmlns=%22http:%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Cdefs%3E%3Cfilter id=%22b%22 x=%22-200%25%22 y=%22-200%25%22 width=%22500%25%22 height=%22500%25%22%3E%3CfeGaussianBlur in=%22SourceGraphic%22 stdDeviation=%2220%22%2F%3E%3C%2Ffilter%3E%3C%2Fdefs%3E%3Cpath fill=%22%23000336%22 d=%22M0 0h2000v1400H0z%22%2F%3E%3Cellipse cx=%2211.394%22 cy=%2252.006%22 rx=%221.594%22 ry=%221.212%22 fill=%22%23fff%22 opacity=%22.108%22%2F%3E%3Cellipse cx=%22322.547%22 cy=%2223.727%22 rx=%221.999%22 ry=%221.622%22 fill=%22%23fff%22 opacity=%22-.162%22%2F%3E%3Cellipse cx=%22559.714%22 cy=%2275.188%22 rx=%222.138%22 ry=%221.984%22 fill=%22%23fff%22 opacity=%22.297%22%2F%3E%3Cellipse cx=%22710.477%22 cy=%22104.043%22 rx=%221.656%22 ry=%221.17%22 fill=%22%23fff%22 opacity=%22.043%22%2F%3E%3Cellipse cx=%22972.7%22 cy=%22127.591%22 rx=%221.683%22 ry=%221.31%22 fill=%22%23fff%22 opacity=%22.68%22%2F%3E%3Cellipse cx=%221004.292%22 cy=%22119.605%22 rx=%221.703%22 ry=%221.522%22 fill=%22%23fff%22 opacity=%22.793%22%2F%3E%3Cellipse cx=%221380.863%22 cy=%2228.742%22 rx=%221.851%22 ry=%221.554%22 fill=%22%23fff%22 opacity=%22.698%22%2F%3E%3Cellipse cx=%221464.438%22 cy=%22121.737%22 rx=%221.477%22 ry=%221.358%22 fill=%22%23fff%22 opacity=%22.32%22%2F%3E%3Cellipse cx=%221624.07%22 cy=%22111.515%22 rx=%221.402%22 ry=%221.29%22 fill=%22%23fff%22 opacity=%22.733%22%2F%3E%3Cellipse cx=%221853.641%22 cy=%2237.239%22 rx=%221.464%22 ry=%221.077%22 fill=%22%23fff%22 opacity=%22.522%22%2F%3E%3Cellipse cx=%2284.075%22 cy=%22180.223%22 rx=%222.364%22 ry=%221.944%22 fill=%22%23fff%22 opacity=%22-.028%22%2F%3E%3Cellipse cx=%22268.974%22 cy=%22238.203%22 rx=%221.624%22 ry=%221.594%22 fill=%22%23fff%22 opacity=%22.411%22%2F%3E%3Cellipse cx=%22532.872%22 cy=%22161.749%22 rx=%221.811%22 ry=%221.517%22 fill=%22%23fff%22 opacity=%22.013%22%2F%3E%3Cellipse cx=%22724.094%22 cy=%22151.294%22 rx=%221.074%22 ry=%221.058%22 fill=%22%23fff%22 opacity=%22.138%22%2F%3E%3Cellipse cx=%22972.548%22 cy=%22223.761%22 rx=%222.173%22 ry=%221.951%22 fill=%22%23fff%22 opacity=%22-.222%22%2F%3E%3Cellipse cx=%221063.098%22 cy=%22140.19%22 rx=%221.834%22 ry=%221.631%22 fill=%22%23fff%22 opacity=%22.914%22%2F%3E%3Cellipse cx=%221285.641%22 cy=%22206.95%22 rx=%221.847%22 ry=%221.625%22 fill=%22%23fff%22 opacity=%22.001%22%2F%3E%3Cellipse cx=%221478.252%22 cy=%22269.625%22 rx=%222.131%22 ry=%221.819%22 fill=%22%23fff%22 opacity=%22-.159%22%2F%3E%3Cellipse cx=%221767.994%22 cy=%22145.669%22 rx=%221.514%22 ry=%221.041%22 fill=%22%23fff%22 opacity=%22.482%22%2F%3E%3Cellipse cx=%221889.827%22 cy=%22206.492%22 rx=%221.801%22 ry=%221.72%22 fill=%22%23fff%22 opacity=%22-.232%22%2F%3E%3Cellipse cx=%22109.766%22 cy=%22406.772%22 rx=%222.422%22 ry=%221.976%22 fill=%22%23fff%22 opacity=%22.326%22%2F%3E%3Cellipse cx=%22329.976%22 cy=%22343.13%22 rx=%221.99%22 ry=%221.728%22 fill=%22%23fff%22 opacity=%22.793%22%2F%3E%3Cellipse cx=%22417.919%22 cy=%22368.529%22 rx=%221.967%22 ry=%221.537%22 fill=%22%23fff%22 opacity=%22.899%22%2F%3E%3Cellipse cx=%22738.756%22 cy=%22281.449%22 rx=%221.649%22 ry=%221.633%22 fill=%22%23fff%22 opacity=%22.766%22%2F%3E%3Cellipse cx=%22882.585%22 cy=%22395.706%22 rx=%221.959%22 ry=%221.849%22 fill=%22%23fff%22 opacity=%22.823%22%2F%3E%3Cellipse cx=%221130.024%22 cy=%22383.888%22 rx=%221.644%22 ry=%221.633%22 fill=%22%23fff%22 opacity=%22.538%22%2F%3E%3Cellipse cx=%221375.568%22 cy=%22322.854%22 rx=%221.252%22 ry=%221.143%22 fill=%22%23fff%22 opacity=%22.627%22%2F%3E%3Cellipse cx=%221408.665%22 cy=%22332.13%22 rx=%221.68%22 ry=%221.376%22 fill=%22%23fff%22 opacity=%22.76%22%2F%3E%3Cellipse cx=%221685.665%22 cy=%22367.458%22 rx=%221.772%22 ry=%221.661%22 fill=%22%23fff%22 opacity=%22.382%22%2F%3E%3Cellipse cx=%221913.783%22 cy=%22399.523%22 rx=%221.654%22 ry=%221.379%22 fill=%22%23fff%22 opacity=%22.035%22%2F%3E%3Cellipse cx=%22106.014%22 cy=%22512.535%22 rx=%221.797%22 ry=%221.602%22 fill=%22%23fff%22 opacity=%22-.121%22%2F%3E%3Cellipse cx=%22240.079%22 cy=%22493.363%22 rx=%221.168%22 ry=%221.157%22 fill=%22%23fff%22 opacity=%22.54%22%2F%3E%3Cellipse cx=%22516.613%22 cy=%22509.726%22 rx=%221.974%22 ry=%221.864%22 fill=%22%23fff%22 opacity=%22.952%22%2F%3E%3Cellipse cx=%22720.873%22 cy=%22477.705%22 rx=%221.79%22 ry=%221.729%22 fill=%22%23fff%22 opacity=%22.443%22%2F%3E%3Cellipse cx=%22964.038%22 cy=%22549.016%22 rx=%221.575%22 ry=%221.434%22 fill=%22%23fff%22 opacity=%22.332%22%2F%3E%3Cellipse cx=%221099.156%22 cy=%22548.176%22 rx=%221.758%22 ry=%221.656%22 fill=%22%23fff%22 opacity=%22.046%22%2F%3E%3Cellipse cx=%221387.196%22 cy=%22483.548%22 rx=%221.709%22 ry=%221.484%22 fill=%22%23fff%22 opacity=%22.442%22%2F%3E%3Cellipse cx=%221589.171%22 cy=%22455.484%22 rx=%221.972%22 ry=%221.683%22 fill=%22%23fff%22 opacity=%22.453%22%2F%3E%3Cellipse cx=%221689.252%22 cy=%22458.899%22 rx=%221.601%22 ry=%221.231%22 fill=%22%23fff%22 opacity=%22.779%22%2F%3E%3Cellipse cx=%221956.088%22 cy=%22546.794%22 rx=%221.359%22 ry=%221.098%22 fill=%22%23fff%22 opacity=%22.53%22%2F%3E%3Cellipse cx=%22162.828%22 cy=%22597.735%22 rx=%221.481%22 ry=%221.144%22 fill=%22%23fff%22 opacity=%22.488%22%2F%3E%3Cellipse cx=%22278.215%22 cy=%22623.412%22 rx=%221.873%22 ry=%221.529%22 fill=%22%23fff%22 opacity=%22.315%22%2F%3E%3Cellipse cx=%22547.121%22 cy=%22693.322%22 rx=%221.247%22 ry=%221.049%22 fill=%22%23fff%22 opacity=%22.765%22%2F%3E%3Cellipse cx=%22705.98%22 cy=%22699.281%22 rx=%221.716%22 ry=%221.431%22 fill=%22%23fff%22 opacity=%22.562%22%2F%3E%3Cellipse cx=%22847.308%22 cy=%22599.067%22 rx=%221.706%22 ry=%221.697%22 fill=%22%23fff%22 opacity=%22.332%22%2F%3E%3Cellipse cx=%221004.58%22 cy=%22614.308%22 rx=%222.11%22 ry=%221.934%22 fill=%22%23fff%22 opacity=%22.703%22%2F%3E%3Cellipse cx=%221211.66%22 cy=%22664.135%22 rx=%222.333%22 ry=%221.928%22 fill=%22%23fff%22 opacity=%22.021%22%2F%3E%3Cellipse cx=%221591.575%22 cy=%22636.764%22 rx=%221.801%22 ry=%221.385%22 fill=%22%23fff%22 opacity=%22.693%22%2F%3E%3Cellipse cx=%221698.69%22 cy=%22638.58%22 rx=%221.953%22 ry=%221.914%22 fill=%22%23fff%22 opacity=%22.477%22%2F%3E%3Cellipse cx=%221973.783%22 cy=%22662.214%22 rx=%222.146%22 ry=%221.813%22 fill=%22%23fff%22 opacity=%22.757%22%2F%3E%3Cellipse cx=%22116.583%22 cy=%22740.099%22 rx=%221.302%22 ry=%221.022%22 fill=%22%23fff%22 opacity=%22.774%22%2F%3E%3Cellipse cx=%22284.661%22 cy=%22745.232%22 rx=%221.438%22 ry=%221.157%22 fill=%22%23fff%22 opacity=%22.198%22%2F%3E%3Cellipse cx=%22580.349%22 cy=%22808.119%22 rx=%222.032%22 ry=%221.799%22 fill=%22%23fff%22 opacity=%22.789%22%2F%3E%3Cellipse cx=%22655.383%22 cy=%22811.748%22 rx=%221.188%22 ry=%221.172%22 fill=%22%23fff%22 opacity=%22.054%22%2F%3E%3Cellipse cx=%22860.034%22 cy=%22717.661%22 rx=%222.11%22 ry=%221.919%22 fill=%22%23fff%22 opacity=%22.774%22%2F%3E%3Cellipse cx=%221191.346%22 cy=%22770.55%22 rx=%221.463%22 ry=%221.331%22 fill=%22%23fff%22 opacity=%22.412%22%2F%3E%3Cellipse cx=%221253.29%22 cy=%22712.74%22 rx=%222.244%22 ry=%221.929%22 fill=%22%23fff%22 opacity=%22.017%22%2F%3E%3Cellipse cx=%221410.941%22 cy=%22817.263%22 rx=%221.597%22 ry=%221.198%22 fill=%22%23fff%22 opacity=%22-.1%22%2F%3E%3Cellipse cx=%221715.71%22 cy=%22754.438%22 rx=%221.651%22 ry=%221.557%22 fill=%22%23fff%22 opacity=%22.271%22%2F%3E%3Cellipse cx=%221998.44%22 cy=%22748.748%22 rx=%221.627%22 ry=%221.626%22 fill=%22%23fff%22 opacity=%22-.015%22%2F%3E%3Cellipse cx=%2239.521%22 cy=%22871.882%22 rx=%221.684%22 ry=%221.599%22 fill=%22%23fff%22 opacity=%22.563%22%2F%3E%3Cellipse cx=%22331.358%22 cy=%22957.434%22 rx=%221.29%22 ry=%221.127%22 fill=%22%23fff%22 opacity=%22.329%22%2F%3E%3Cellipse cx=%22588.408%22 cy=%22944.469%22 rx=%222.36%22 ry=%221.861%22 fill=%22%23fff%22 opacity=%22.158%22%2F%3E%3Cellipse cx=%22601.373%22 cy=%22895.881%22 rx=%221.598%22 ry=%221.351%22 fill=%22%23fff%22 opacity=%22.905%22%2F%3E%3Cellipse cx=%22859.663%22 cy=%22923.784%22 rx=%221.386%22 ry=%221.016%22 fill=%22%23fff%22 opacity=%22.081%22%2F%3E%3Cellipse cx=%221112.092%22 cy=%22885.322%22 rx=%221.684%22 ry=%221.559%22 fill=%22%23fff%22 opacity=%22.142%22%2F%3E%3Cellipse cx=%221326.903%22 cy=%22964.672%22 rx=%221.963%22 ry=%221.672%22 fill=%22%23fff%22 opacity=%22.618%22%2F%3E%3Cellipse cx=%221571.176%22 cy=%22873.095%22 rx=%221.598%22 ry=%221.59%22 fill=%22%23fff%22 opacity=%22.369%22%2F%3E%3Cellipse cx=%221687.994%22 cy=%22852.97%22 rx=%221.621%22 ry=%221.382%22 fill=%22%23fff%22 opacity=%22.338%22%2F%3E%3Cellipse cx=%221874.553%22 cy=%22866.83%22 rx=%222.071%22 ry=%221.825%22 fill=%22%23fff%22 opacity=%22.067%22%2F%3E%3Cellipse cx=%2235.192%22 cy=%221013.56%22 rx=%221.808%22 ry=%221.395%22 fill=%22%23fff%22 opacity=%22.202%22%2F%3E%3Cellipse cx=%22325.273%22 cy=%221040.202%22 rx=%222.029%22 ry=%221.788%22 fill=%22%23fff%22 opacity=%22.511%22%2F%3E%3Cellipse cx=%22422.86%22 cy=%221000.336%22 rx=%221.979%22 ry=%221.916%22 fill=%22%23fff%22 opacity=%22.795%22%2F%3E%3Cellipse cx=%22604.305%22 cy=%221094.955%22 rx=%221.314%22 ry=%221.237%22 fill=%22%23fff%22 opacity=%22.341%22%2F%3E%3Cellipse cx=%22986.794%22 cy=%221113.341%22 rx=%221.622%22 ry=%221.209%22 fill=%22%23fff%22 opacity=%22.244%22%2F%3E%3Cellipse cx=%221172.036%22 cy=%221072.875%22 rx=%221.557%22 ry=%221.406%22 fill=%22%23fff%22 opacity=%22-.061%22%2F%3E%3Cellipse cx=%221245.881%22 cy=%221040.432%22 rx=%221.828%22 ry=%221.336%22 fill=%22%23fff%22 opacity=%22.243%22%2F%3E%3Cellipse cx=%221585.067%22 cy=%221070.092%22 rx=%221.85%22 ry=%221.495%22 fill=%22%23fff%22 opacity=%22.57%22%2F%3E%3Cellipse cx=%221661.952%22 cy=%221046.335%22 rx=%221.443%22 ry=%221.198%22 fill=%22%23fff%22 opacity=%22.657%22%2F%3E%3Cellipse cx=%221840.212%22 cy=%221039.665%22 rx=%221.669%22 ry=%221.459%22 fill=%22%23fff%22 opacity=%22.578%22%2F%3E%3Cellipse cx=%2259.599%22 cy=%221245.066%22 rx=%221.67%22 ry=%221.272%22 fill=%22%23fff%22 opacity=%22.223%22%2F%3E%3Cellipse cx=%22344.449%22 cy=%221169.487%22 rx=%221.765%22 ry=%221.39%22 fill=%22%23fff%22 opacity=%22.247%22%2F%3E%3Cellipse cx=%22472.59%22 cy=%221222.939%22 rx=%222.384%22 ry=%221.974%22 fill=%22%23fff%22 opacity=%22.523%22%2F%3E%3Cellipse cx=%22661.055%22 cy=%221130.994%22 rx=%221.317%22 ry=%221.097%22 fill=%22%23fff%22 opacity=%22-.061%22%2F%3E%3Cellipse cx=%22826.798%22 cy=%221240.897%22 rx=%221.849%22 ry=%221.804%22 fill=%22%23fff%22 opacity=%22.042%22%2F%3E%3Cellipse cx=%221088.599%22 cy=%221245.084%22 rx=%221.191%22 ry=%221.02%22 fill=%22%23fff%22 opacity=%22.389%22%2F%3E%3Cellipse cx=%221237.909%22 cy=%221200.184%22 rx=%221.142%22 ry=%221.004%22 fill=%22%23fff%22 opacity=%22.386%22%2F%3E%3Cellipse cx=%221510.579%22 cy=%221168.819%22 rx=%221.46%22 ry=%221.005%22 fill=%22%23fff%22 opacity=%22.765%22%2F%3E%3Cellipse cx=%221759.609%22 cy=%221157.344%22 rx=%221.514%22 ry=%221.372%22 fill=%22%23fff%22 opacity=%22.776%22%2F%3E%3Cellipse cx=%221832.25%22 cy=%221249.346%22 rx=%221.599%22 ry=%221.378%22 fill=%22%23fff%22 opacity=%22.058%22%2F%3E%3Cellipse cx=%22163.657%22 cy=%221318.465%22 rx=%221.911%22 ry=%221.805%22 fill=%22%23fff%22 opacity=%22.605%22%2F%3E%3Cellipse cx=%22364.989%22 cy=%221297.928%22 rx=%222.014%22 ry=%221.606%22 fill=%22%23fff%22 opacity=%22-.139%22%2F%3E%3Cellipse cx=%22543.951%22 cy=%221379.706%22 rx=%221.437%22 ry=%221.044%22 fill=%22%23fff%22 opacity=%22-.127%22%2F%3E%3Cellipse cx=%22709.69%22 cy=%221331.798%22 rx=%222.098%22 ry=%221.984%22 fill=%22%23fff%22 opacity=%22.717%22%2F%3E%3Cellipse cx=%22980.198%22 cy=%221366.379%22 rx=%221.073%22 ry=%221.016%22 fill=%22%23fff%22 opacity=%22.951%22%2F%3E%3Cellipse cx=%221124.364%22 cy=%221301.778%22 rx=%221.98%22 ry=%221.862%22 fill=%22%23fff%22 opacity=%22.728%22%2F%3E%3Cellipse cx=%221297.738%22 cy=%221381.697%22 rx=%221.372%22 ry=%221.255%22 fill=%22%23fff%22 opacity=%22.334%22%2F%3E%3Cellipse cx=%221406.53%22 cy=%221381.757%22 rx=%221.241%22 ry=%221.194%22 fill=%22%23fff%22 opacity=%22.749%22%2F%3E%3Cellipse cx=%221689.369%22 cy=%221318.911%22 rx=%221.958%22 ry=%221.809%22 fill=%22%23fff%22 opacity=%22.457%22%2F%3E%3Cellipse cx=%221947.372%22 cy=%221300.667%22 rx=%221.388%22 ry=%221.318%22 fill=%22%23fff%22 opacity=%22.396%22%2F%3E%3Cg transform=%22rotate(-64.116 993.324 -1535.284)%22%3E%3Cdefs%3E%3ClinearGradient id=%22a%22 x1=%220%22 y1=%221%22 x2=%22281.347%22 y2=%221%22 gradientUnits=%22userSpaceOnUse%22%3E%3Cstop stop-color=%22%23fff%22%2F%3E%3Cstop offset=%22.3%22 stop-color=%22%23fff%22 stop-opacity=%22.1%22%2F%3E%3Cstop offset=%22.7%22 stop-color=%22%23fff%22 stop-opacity=%220%22%2F%3E%3C%2FlinearGradient%3E%3C%2Fdefs%3E%3Crect x=%22-14.067%22 y=%22-12.5%22 width=%22112.539%22 height=%2225%22 rx=%2225%22 ry=%2225%22 fill=%22url(%23a)%22 filter=%22url(%23b)%22 opacity=%22.4%22%2F%3E%3Crect width=%22168.808%22 height=%228%22 rx=%228%22 ry=%228%22 fill=%22url(%23a)%22%2F%3E%3C%2Fg%3E%3Cg transform=%22rotate(-61.883 662.534 -409.078)%22 fill=%22url(%23a)%22%3E%3Crect x=%22-16.108%22 y=%22-12.5%22 width=%22128.863%22 height=%2225%22 rx=%2225%22 ry=%2225%22 filter=%22url(%23b)%22 opacity=%22.4%22%2F%3E%3Crect width=%22193.295%22 height=%228%22 rx=%228%22 ry=%228%22%2F%3E%3C%2Fg%3E%3Cg transform=%22rotate(-62.006 1136.866 -717.81)%22 fill=%22url(%23a)%22%3E%3Crect x=%22-14.092%22 y=%22-12.5%22 width=%22112.737%22 height=%2225%22 rx=%2225%22 ry=%2225%22 filter=%22url(%23b)%22 opacity=%22.4%22%2F%3E%3Crect width=%22169.106%22 height=%228%22 rx=%228%22 ry=%228%22%2F%3E%3C%2Fg%3E%3Cg transform=%22rotate(-57.953 1390.502 -525.276)%22 fill=%22url(%23a)%22%3E%3Crect x=%22-12.827%22 y=%22-12.5%22 width=%22102.618%22 height=%2225%22 rx=%2225%22 ry=%2225%22 filter=%22url(%23b)%22 opacity=%22.4%22%2F%3E%3Crect width=%22153.928%22 height=%228%22 rx=%228%22 ry=%228%22%2F%3E%3C%2Fg%3E%3Cg transform=%22rotate(-62.694 1171.313 424.681)%22 fill=%22url(%23a)%22%3E%3Crect x=%22-17.287%22 y=%22-12.5%22 width=%22138.297%22 height=%2225%22 rx=%2225%22 ry=%2225%22 filter=%22url(%23b)%22 opacity=%22.4%22%2F%3E%3Crect width=%22207.446%22 height=%228%22 rx=%228%22 ry=%228%22%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E");
}

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
 
