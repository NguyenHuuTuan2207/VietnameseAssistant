import tkinter as tk
from PIL import Image, ImageTk
import speech_recognition as sr
from gtts import gTTS
import os
import playsound
from datetime import datetime
import wikipedia

class VoiceAssistant:
    def __init__(self, root):
        self.root = root
        self.root.title("Voice Assistant")
        self.create_widgets()
        self.initialize_voice()

    def create_widgets(self):
        assistant_img = Image.open("D:\ANguyen Huu Tuan 21GIT\Term1-year3\doancs4\image\Assistant.png")
        assistant_img = assistant_img.resize((100, 100), Image.LANCZOS)
        self.assistant_img = ImageTk.PhotoImage(assistant_img)

        main_frame = tk.Frame(self.root)
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        assistant_img_label = tk.Label(main_frame, image=self.assistant_img)
        assistant_img_label.grid(row=0, column=0, padx=10, pady=10)

        self.assistant_text = tk.Text(main_frame, width=50, height=15)
        self.assistant_text.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=10, pady=10)

        send_img = Image.open("D:\ANguyen Huu Tuan 21GIT\Term1-year3\doancs4\image\microphone.png")
        send_img = send_img.resize((50, 50), Image.LANCZOS)
        self.send_img = ImageTk.PhotoImage(send_img)

        send_button = tk.Button(main_frame, image=self.send_img, command=self.send_command)
        send_button.grid(row=2, column=0, padx=10, pady=10)

    def initialize_voice(self):
        self.r = sr.Recognizer()

    def send_command(self):
        with sr.Microphone() as source:
            audio_data = self.r.listen(source, timeout=5)
            print("Recognizing...")
            try:
                text = self.r.recognize_google(audio_data, language="vi")
            except sr.UnknownValueError:
                text = " Xin lỗi , mình không nghe rõ. Bạn nói lại được không?"

            print(text)
            self.assistant_text.insert(tk.END, "User: " + text + "\n")

            if text == " ":
                robot_brain = "Bạn muốn nói gì với tôi vậy "
                self.speak(robot_brain)
            elif text == "xin chào" or text == "chào bạn" or text == "Xin chào":
                robot_brain = "Xin chào , Bạn có khỏe không"
                self.speak(robot_brain)
            elif text == "Hôm nay là ngày bao nhiêu" or text == "thời gian hiện tại":
                robot_brain = "Hiện tại là ngày" + datetime.now().strftime("%d/%m/%Y")
                self.speak(robot_brain)
            elif text == "Bây giờ là mấy giờ":
                robot_brain = "Hiện tại là" + datetime.now().strftime("%H:%M:%S")
                self.speak(robot_brain)
            elif text == "tạm biệt" or text == "Tạm biệt bạn":
                robot_brain = "Tạm biệt , chúc bạn một ngày tốt lành"
                self.speak(robot_brain)
            elif text:
                wikipedia.set_lang("vi")
                robot_brain = wikipedia.summary(text, sentences=1)
                self.speak(robot_brain)
            else:
                robot_brain = " Xin lỗi , mình không hiểu bạn nói gì "
                self.speak(robot_brain)

    def speak(self, text):
        self.assistant_text.insert(tk.END, "Assistant: " + text + "\n")
        tts = gTTS(text=text, lang='vi')
        filename = './voice.mp3'
        tts.save(filename)
        playsound.playsound(filename)
        os.remove(filename)

root = tk.Tk()
app = VoiceAssistant(root)
root.mainloop()
