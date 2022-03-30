import streamlit as st
import os
import random
def app():
    st.title("Randomize painting")

    #getting the names of the images
    images_names = os.listdir('images/portfolio_instagram')
    images_names = [images_name for images_name in images_names if '.jpg' in images_name]
    images_names.remove('2017-01-16_21-42-18_UTC_profile_pic.jpg')
    images_names.sort()
    images_names = images_names[::-1]
    dico_images_descriptions = {}
    for images_name in images_names:
        if '_2.jpg' in images_name:
            with open('images/portfolio_instagram/' + images_name[:-6] + '.txt') as f:
                lines = f.readlines()
                dico_images_descriptions[images_name] = lines[0].split('#')[0]
        elif '_1.jpg' in images_name:
            dico_images_descriptions[images_name] = ''
        else:
            with open('images/portfolio_instagram/' + images_name[:-4] + '.txt') as f:
                lines = f.readlines()
                dico_images_descriptions[images_name] = lines[0].split('#')[0]

    if st.button('Click me to load randomly one of my paintings !'):
        a_random_image_name = list(dico_images_descriptions.keys())[random.randint(0,len(list(dico_images_descriptions.keys()))-1)]
        st.image('images/portfolio_instagram/' + a_random_image_name,
                caption=dico_images_descriptions[a_random_image_name])
    else:
        a_random_image_name = list(dico_images_descriptions.keys())[random.randint(0,len(list(dico_images_descriptions.keys()))-1)]
        st.image('images/portfolio_instagram/' + a_random_image_name,
                caption=dico_images_descriptions[a_random_image_name])
