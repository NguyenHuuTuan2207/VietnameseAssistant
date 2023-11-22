import speech_recognition as sr
# initialize the recognizer
r = sr.Recognizer()
with sr.Microphone() as source:
    # read the audio data from the default microphone
    audio_data = r.record(source, duration=5)
    print("Recognizing...")
    # convert speech to text
    try:
        text = r.recognize_google(audio_data, language="vi")
    except:
        text = " Xin lỗi , mình không hiểu bạn nói gì "
    print(text)