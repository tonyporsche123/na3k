
import streamlit as st
import time
import json
import requests 
from streamlit_lottie import st_lottie 
from PIL import Image
import emoji

def load_lottiefile(filepath: str):
      with open(filepath, "r") as f:
          return json.load(f)
def load_lottieurl(url: str):
      r = requests.get(url)
      if r.status_code != 200:
          return None
      return r.json()
st.write(emoji.emojize("""# PEM Bké """))

lottie_coding = load_lottiefile("welcome.json")
lottie_hello = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_69HH48.json")

st_lottie(
lottie_hello,
speed=1,
reverse=False,
loop=True,
quality="low", # medium ; high
#renderer="svg", # canvas
height=None,
width=None,
key=None,
)
st.balloons()
