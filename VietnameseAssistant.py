import speech_recognition as sr
from gtts import gTTS
import os
import playsound
from datetime import datetime
import wikipedia
now=datetime.now()
# initialize the recognizer
r = sr.Recognizer()
def speak(text):
    tts = gTTS(text=text, lang='vi')
    filename = './voice.mp3'
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

while True :
        # read the audio data from the default microphone
    with sr.Microphone() as source:
        audio_data = r.record(source, duration=5)
        print("Recognizing...")
        # convert speech to text
        try:
            text = r.recognize_google(audio_data, language="vi")
        except:
            text = " Xin lỗi , mình không hiểu bạn nói gì "
        print(text)
        if text== " " :
            robot_brain="Bạn muốn nói gì với tôi vậy "
            speak(robot_brain)
        elif text=="xin chào" or text=="chào bạn" or text=="Xin chào" :
            robot_brain="Xin chào , Bạn có khỏe hem"
            speak(robot_brain)
        elif text=="Hôm nay là ngày bao nhiêu" or text=="thời gian hiện tại" :
            robot_brain="Hiện tại là ngày" + now.strftime("%d/%m/%Y")
            speak(robot_brain)
        elif text=="Bây giờ là mấy giờ" :
            robot_brain="Hiện tại là" + now.strftime("%H:%M:%S")
            speak(robot_brain)
        elif text=="tạm biệt" or text=="Tạm biệt bạn" :
            robot_brain="Tạm biệt , chúc bạn một ngày tốt lành"
            speak(robot_brain)
            break
        elif text :
            wikipedia.set_lang("vi")
            robot_brain = wikipedia.summary(text, sentences=1)
            speak(robot_brain)
        else :
            robot_brain = " Xin lỗi , mình không hiểu bạn nói gì "
            speak(robot_brain)




