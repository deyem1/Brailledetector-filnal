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

try:

    from tensorflow.keras.models import load_model
    # import cv2
    import cv2
    import tensorflow as tf


    st.title('Braille Detector:book:')
    # st.title(' ')
    st.markdown("<h3 style='text-align: center; '></h3>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; '>This program checks an image to determine if there is braille within an image</p>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; '></h3>", unsafe_allow_html=True)

    from gtts import gTTS


    from io import BytesIO
    sound_file = BytesIO()



    def predict_upload():
        resize = tf.image.resize(cv2_imgg, (120, 120))
        print('got here4')

        yhat = new_model.predict(np.expand_dims(resize / 120, 0))
        print(yhat)
        ans = round(yhat[0][0][0]*100, 2)
        print('probability value:', yhat[0])
        if yhat[0] < 0.6:
            text = f'The uploaded image does not have braille ❌.\n There is a {ans}% chance that this picture has braille '
            # print(f'Predicted class does not have braille')
            st.error(text)
            print(text)
            tts = gTTS(f'The uploaded image does not have braille. There is a {ans}% chance that this picture has braille.' , lang='en')
            tts.write_to_fp(sound_file)
            st.audio(sound_file)
            # talk('image does not have braille')
        else:
            text = f'Predicted class is braille ✔. \n There is a {ans}% chance that this picture has braille'
            print(text)
            st.success(text)
            tts = gTTS(f'Predicted class is braille. There is a {ans}% chance that this picture has braille', lang='en')
            tts.write_to_fp(sound_file)
            st.audio(sound_file)
            # talk(f'image has have braille'+ 'with a probability of'+ yhat[0][0])


    # def uploadingFile():
    #


    typer = st.radio(
        "Select an option to upload media",
        ('upload image', 'take a photo'))

    if typer == 'take a photo':
        st.write('To take a photo, click on capture below')
        img_file_buffer = st.camera_input("Take a picture")

    else:
        st.write("Kindly upload an image")
        uploaded_file = st.file_uploader("Choose a file")
        # uploadingFile()
        print('a')
        if uploaded_file is not None:
            # To read file as bytes:
            print('got here0')
            bytes_data = uploaded_file.getvalue()
            cv2_imgg = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
            # cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)

            print('got here2')
            new_model = load_model('brailledetect2.h5',
                                   compile=False)
            print('got here2')
            trigger = st.button('Predict', on_click=predict_upload)
        else:
            print('no image')

    # genre = st.radio(

    #     "What\'s your favorite movie genre",
    #     ('Comedy', 'Drama', 'Documentary'))
    #
    # if genre == 'Comedy':
    #     st.write('You selected comedy.')
    #     # uploadingFile()
    # else:
    #     st.write("You didn\'t select comedy.")


except:
    print('errorrrrr1')

# import wikipedia
# import csv
# from datetime import date
#
# import datetime
# import pywhatkit
# import PyAudio
# ass_Name = "alexa"
# def take_command():
#     try:
#         with sr.Microphone() as source:
#             print("This is Adeyemi's Voice Assistant")
#             print("listening....")
#             print("Please speak now!")
#             voice = listener.listen(source)
#             command = listener.recognize_google(voice)
#             command = command.lower()
#             # command = command.replace('snow', '')
#             return command
#
#             # if "snow" in command:
#             #     # talk("This is Adeyemi's Voice Assistant called snow")
#             #     # talk("what would you like me to do")
#             #
#             #     talk('what would you like me to do')
#             #     talk("hello")
#             #     print(command)
#             #     return command
#             # else:
#             #     talk('my name is snow')
#
#                 # return command
#             # talk("This is Adeyemi's Voice Assistant called snow")
#     except:
#         pass
#
# #
# def wake_up_call():
#     command = take_command()
#     command = command.lower()
#     if "snow" in command:
#         # talk("This is Adeyemi's Voice Assistant called snow")
#         # talk("what would you like me to do")
#         command = command.replace('snow', '')
#
#         talk("hello")
#         talk('what would you like me to do')
#
#         print("wake up call activated")
#         # other_command()
#         run_snow()
#         # return other_command()
#         # take_command()
#     else:
#         talk('my name is snow')
#         print(command)
#
#
#
# def onboard():
#     talk('Who do you want to onboard?')
#     new_employee = other_command()
#     # new_employee = new_employee.lower()
#     print(new_employee)
#     talk("is the name of the new employee " + new_employee)
#     talk('is that correct?')
#     print('5')
#     # new_employee = onboard()
#     answer = other_command()
#     answer = answer.lower()
#     if answer == 'yes':
#         talk('Creating contract for' + new_employee)
#
#         talk('what department?')
#         new_department = other_command()
#
#         talk('which city branch?')
#         new_branch = other_command()
#
#
#
#         today = date.today()
#
#
#
#     elif answer == 'no':
#         # new_employee = other_command()
#         # onboard()
#         # talk('please repeat the name of who you would like to on board')
#         # new_employee = other_command()
#         # new_employee = new_employee.lower()
#
#         onboard()
#         # repeat_onboard()
#     else:
#         talk('is that a yes or a no')
#         onboard()
#
#     return new_employee
#
# # def repeat_onboard():
#
#
#
#
# def run_snow():
#     command = other_command()
#     # command = other_command().lower()
#     print(command)
#     # if "play" in command:
#     #     song = command.replace('play', "")
#     #     pywhatkit.playonyt(song)
#     #
#     #     talk("playing" + song)
#     #     # talk("playing " + song)
#     #     print(song)
#     if 'time' in command:
#         time = datetime.datetime.now().strftime('%I: %M %p')
#         talk("i do not know the time, just joking! fetching current time")
#         talk("current time is " + time)
#         print(time)
#
#     elif "what is" in command:
#         # 'wikipedia' in command or "who is" in command or
#         person = command.replace("what is", '')
#         info = wikipedia.summary(person, 1)
#         print(info)
#         talk(info)
#
#
#
#
#
#
#     else:
#         talk("you said " + command + " but sorry, i can't do that right now")
#         run_snow()
#
#
#
#
# # with sr.Microphone() as source:
# #     print("This is Adeyemi's Voice Assistant")
# #     print("listening....")
# #     print("Please speak now!")
# #     voice = listener.listen(source)
# #     command = listener.recognize_google(voice)
# #     command = command.lower()
# #     talk("This is Adeyemi's Voice Assistant called snow")
# #     talk("i do not know the time, just joking! fetching current time")
#
#
#
#
#
#
#
# wake_up_call()
# # run_snow()
# # take_command()
# contract()
#
