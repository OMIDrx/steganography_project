import streamlit as st
from stegano import lsb
from PIL import Image
import random



st.set_page_config(page_title='Stegano Project') 

option = st.sidebar.selectbox('select your option',('Hide Text','Reveal text'))

if option == 'Hide Text':
    uploaded_file = st.file_uploader('browese your image',type=['png','jpg'])
    
    secret_msg = st.text_area('Enter your text')
    
    if uploaded_file and secret_msg:
        temp_img = Image.open(uploaded_file)
        
        secret_msg = lsb.hide(temp_img,secret_msg)
        
        q = '123456789qwertyuiop'

        x = random.choices(q, k=7)
        x = './' + ''.join(x) + '.png'
        
        output_img = x
        
        if st.button('SAVE FINAL IMAGE'):
            secret_msg.save(output_img)
            st.success('img created')

elif option == 'Reveal text':
    
    secret_file = st.file_uploader('select your final image',type= ['png'])
    
    if secret_file:
        new_image = Image.open(secret_file)
        
        message = lsb.reveal(new_image)
        
        if st.button('reveal'):
            st.write(message)
            st.success('successfuly')
    else:
        st.error('upload wrong file')