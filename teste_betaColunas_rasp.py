from tkinter import Button
import streamlit as st
from streamlit import caching
import pandas as pd
from urllib.request import urlopen
from PIL import Image
import os.path
from datetime import datetime
import pytz

col1, col2 = st.beta_columns(2)
original= Image.open(urlopen('https://scontent.fpll5-1.fna.fbcdn.net/v/t39.30808-6/259640659_4575564699203105_7423654804219245827_n.jpg?_nc_cat=104&ccb=1-5&_nc_sid=09cbfe&_nc_eui2=AeFhF6qY4WcvjUdBqgYik9aFg-Bwa7lXzqqD4HBruVfOqkyMDDh6WalqVifuefJV8at4SItp-y9WvylCyN1YWDkO&_nc_ohc=PHGCyxzHPJUAX-Xd6qB&tn=8e8RX8BIIyy5wxmH&_nc_ht=scontent.fpll5-1.fna&oh=00_AT_pVdHEPnXDlJR8BrhtKyFxvVWN2ccts-BA33jB-N2IPA&oe=623DEA3D'))

col1.header("Original")
col1.image(original, use_column_width=True)

grayscale = original.convert('LA')
col2.header("Grayscale")
col2.image(grayscale, use_column_width=True)