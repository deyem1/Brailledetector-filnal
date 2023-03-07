# import pywhatkit as pywhatkit
# import speech_recognition as sr
# import pyttsx3
import numpy as np
# import pandas as pd
import streamlit as st

# listener = sr.Recognizer()
# engine = pyttsx3.init()

# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[1].id)


# engine.say('i am here')
# engine.runAndWait()

# def talk(text):
#     engine.say(text)
#     engine.runAndWait()

# talk('i am  here')
# @st.cache
# def download1(url1):
#     url = url1
#     filename = url.split('/')[-1]
#     urllib.request.urlretrieve(url, filename)

try:

    from tensorflow.keras.models import load_model
    # import cv2
    import cv2
    import tensorflow as tf

    st.title('Braille Detector:book:')
    # st.title(' ')
    st.markdown("<h3 style='text-align: center; '></h3>", unsafe_allow_html=True)
    st.markdown(
        "<p style='text-align: center; '>This program checks an image to determine if there is braille within an image</p>",
        unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; '></h3>", unsafe_allow_html=True)

    from gtts import gTTS

    from io import BytesIO

    sound_file = BytesIO()

    st.sidebar.markdown('---')
    confidence = st.sidebar.slider('Braille confidence', min_value=0.5, max_value=1.0, value=0.6)

    st.sidebar.markdown('---')
    st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/4/4c/Braille_closeup.jpg", caption='An example of a braille')
    st.sidebar.markdown('---')
    st.sidebar.markdown('Keele Group coursework, 2023. Do not Copy!')
    # feedback = st.sidebar.write()



    def predict_upload():
        resize = tf.image.resize(cv2_imgg, (120, 120))
        print('got here4')

        yhat = new_model.predict(np.expand_dims(resize / 120, 0))
        print(yhat)
        ans = round(yhat[0][0][0] * 100, 2)
        print('probability value:', yhat[0])

        sample_coords = yhat[1][0]
        frame = cv2_imgg

        if yhat[0] < confidence:
            text = f'The uploaded image does not have braille ❌.\n There is a {ans}% chance that this picture has ' \
                   f'braille '
            # print(f'Predicted class does not have braille')
            st.error(text)
            print(text)
            tts = gTTS(
                f'The uploaded image does not have braille. There is a {ans}% chance that this picture has braille.',
                lang='en')
            tts.write_to_fp(sound_file)
            st.audio(sound_file)


            # talk('image does not have braille')
        elif yhat[0] > confidence:
            st.snow()
            text = f'Predicted class is braille ✔. \n There is a {ans}% chance that this picture has braille'
            print(text)
            st.success(text)
            tts = gTTS(f'Predicted class is braille. There is a {ans}% chance that this picture has braille', lang='en')
            tts.write_to_fp(sound_file)
            st.audio(sound_file)
            st.write('To interpret the braille, ABEG head-over to my senior man')
            st.markdown('<a href = "https://angelina-reader.ru/">or Visit Angelinas website </a>', unsafe_allow_html=True)
            # Controls the main rectangle
            cv2.rectangle(frame,
                          tuple(np.multiply(sample_coords[:2], [450, 450]).astype(int)),
                          tuple(np.multiply(sample_coords[2:], [450, 450]).astype(int)),
                          (255, 0, 0), 2)
            # Controls the label rectangle
            cv2.rectangle(frame,
                          tuple(np.add(np.multiply(sample_coords[:2], [450, 450]).astype(int),
                                       [0, -30])),
                          tuple(np.add(np.multiply(sample_coords[:2], [450, 450]).astype(int),
                                       [80, 0])),
                          (255, 0, 0), -1)

            # Controls the text rendered
            cv2.putText(frame, f'braille', tuple(np.add(np.multiply(sample_coords[:2], [450, 450]).astype(int),
                                                        [0, -5])),
                        cv2.FONT_HERSHEY_SIMPLEX, .7, (255, 255, 255), 2, cv2.LINE_AA)
            cv2.putText(frame, f'confidence: {ans} %',
                        tuple(np.add(np.multiply(sample_coords[:2], [450, 350]).astype(int),
                                     [0, -5])),
                        cv2.FONT_HERSHEY_SIMPLEX, .7, (255, 255, 255), 2, cv2.LINE_AA)
            # image = cv2.imshow('braille',frame)
            # print(type(image))
            st.image(frame, caption='Annotated Image')

            # talk(f'image has have braille'+ 'with a probability of'+ yhat[0][0])


    # def uploadingFile():
    #

    typer = st.radio(
        "Select an option to upload media",
        ('upload image', 'take a photo'))

    if typer == 'take a photo':
        st.write('To take a photo, click on capture below \n note camera functionality is limited at the moment')
        img_file_buffer = st.camera_input("Take a picture")
        st.write('nice face!!!')
        if img_file_buffer is not None:
            st.image(img_file_buffer)
            print('got here23')
            # To read image file buffer with OpenCV:
            bytes_data = img_file_buffer.getvalue()
            cv2_imgg = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
            print('got here2')
            new_model = load_model('brailledetect2.h5',
                                   compile=False)
            trigger = st.button('Predict', on_click=predict_upload)




    else:
        st.write("Kindly upload an image")
        img_file_buffer = st.file_uploader('Choose a file. Note! Allowed formats are :red[".JPG, JPEG, .PNG"]', type=["jpg", "jpeg", "png"])

        # uploadingFile()
        print('a')
        if img_file_buffer is not None:
            # To read file as bytes:
            print('got here0')
            bytes_data = img_file_buffer.getvalue()
            cv2_imgg = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
            # cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)

            print('got here2')
            new_model = load_model('brailledetect2.h5',
                                   compile=False)
            print('got here2')
            trigger = st.button('Predict', on_click=predict_upload)
        else:
            print('no image')



except:
    print('errorrrrr1')
