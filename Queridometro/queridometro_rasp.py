from tkinter import Button
import streamlit as st
from streamlit import caching
import pandas as pd
from urllib.request import urlopen
from PIL import Image
import os.path
from datetime import datetime
import pytz

Button1=False
Button2=False

st.title('Queridometro')

T_br = pytz.timezone('America/Sao_Paulo')
today = datetime.now(T_br)

arquivo= 'historico_queridometro.csv'
if os.path.isfile(arquivo):
    resultado=pd.read_csv(arquivo,index_col=False) 
else:
    print('Criando base de dados')
    dia = today.strftime("%d/%m/%Y")
    horario = today.strftime("%H:%M:%S")
    data_pd = {'Status': ['Gostoso(a)', 'Coração','Cobra'], 'Bruno': [0, 0,0],'Geeh': [0, 0,0]} 
    resultado=pd.DataFrame(data_pd)
    resultado.to_csv(arquivo, index=False)


col1, col2 = st.columns(2)



with col1:
    #with st.form(key='form1'):
        imageBTC= Image.open(urlopen('https://scontent.fpll5-1.fna.fbcdn.net/v/t39.30808-6/259640659_4575564699203105_7423654804219245827_n.jpg?_nc_cat=104&ccb=1-5&_nc_sid=09cbfe&_nc_eui2=AeFhF6qY4WcvjUdBqgYik9aFg-Bwa7lXzqqD4HBruVfOqkyMDDh6WalqVifuefJV8at4SItp-y9WvylCyN1YWDkO&_nc_ohc=PHGCyxzHPJUAX-Xd6qB&tn=8e8RX8BIIyy5wxmH&_nc_ht=scontent.fpll5-1.fna&oh=00_AT_pVdHEPnXDlJR8BrhtKyFxvVWN2ccts-BA33jB-N2IPA&oe=623DEA3D'))
        st.image(imageBTC,width=100)

        genre = st.radio(
            "Escolha o status do seu queridometro para o Bruno",
            ('','Gostoso pra caralho', 'Coração', 'Cobra'))

        if genre == 'Gostoso pra caralho' :
            st.write('Você tem bom gosto deseja salvar?.')
            resultado['Bruno'][0]=resultado['Bruno'][0]+1
            Button1=False
        elif genre == 'Coração' :
            st.write("*-* você é um amor, deseja salvar?.")
            resultado['Bruno'][1]=resultado['Bruno'][1]+1
            Button1=False

        elif genre == 'Cobra':
            st.write("Haaa vá a merda.")
            resultado['Bruno'][2]=resultado['Bruno'][2]+1
            Button1=False
        else: 
            pass

            
        #if st.form_submit_button('Salvar?'):
        #    Button1=True
        #    print(Button1)
        #    st.write('Salvo com sucesso')
        #    resultado.to_csv(arquivo, index=False)

        #else:
        #    st.write(' ')



with col2:
    #with st.form(key='form2'):
        imageBTC= Image.open(urlopen('https://scontent.fpll5-1.fna.fbcdn.net/v/t39.30808-6/261884778_2029567483886217_9044407873053388144_n.jpg?_nc_cat=108&ccb=1-5&_nc_sid=09cbfe&_nc_eui2=AeEvn8YU7YEep7AAJF2esxuzY0YH8EWbxJdjRgfwRZvEl12KRs1mDuyYshc3b5RKDPzZvxuqY8HqbgMAkdXeDpmw&_nc_ohc=oIMcVDIYqUgAX-RnLPw&_nc_ht=scontent.fpll5-1.fna&oh=00_AT_WahysdS7Nflh_VoTPLupw7tAy4GeFRefjQhQAa6uLaw&oe=623EFB2C'))
        st.image(imageBTC,width=100)

        genre2 = st.radio(
            "Escolha o status do seu queridometro para a Geeh",
            ('','Gostosa pra caralho', 'Coração', 'Cobra'))

        if genre2 == 'Gostosa pra caralho':
            st.write('Você tem bom gosto deseja salvar?.')
            resultado['Geeh'][0]=resultado['Geeh'][0]+1
            Button2=False
        elif genre2 == 'Coração':
            st.write("*-* você é um amor, deseja salvar?.")
            resultado['Geeh'][1]=resultado['Geeh'][1]+1
            Button2=False
        elif genre2 == 'Cobra' :
            st.write("Haaa vá a merda.")
            resultado['Geeh'][2]=resultado['Geeh'][2]+1
            Button2=False
        else: 
            pass

            
        #if st.form_submit_button('Salvar?'):
        #    st.write('Salvo com sucesso')
        #    resultado.to_csv(arquivo, index=False)
        #    Button2=True
        #else:
        #    st.write(' ')

if st.button('Salvar?'):
        st.write('Salvo com sucesso')
        resultado.to_csv(arquivo, index=False)
else:
        st.write(' ')


st.title('Resultado do Mês '+str(today.month)+" :")
st.dataframe(resultado)