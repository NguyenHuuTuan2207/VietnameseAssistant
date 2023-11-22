import tkinter as tk
from PIL import Image, ImageTk

class VoiceAssistant:
    def __init__(self, root):
        self.root = root
        self.root.title("Voice Assistant")
        self.create_widgets()

    def create_widgets(self):
        # # Load the microphone image file
        # mic_img = Image.open("D:\ANguyen Huu Tuan 21GIT\Term1-year3\doancs4\image\Assistant.png")
        # mic_img = mic_img.resize((50, 50), Image.LANCZOS)  # Resize the image
        # self.microphone_img = ImageTk.PhotoImage(mic_img)

        # Load the assistant image file
        assistant_img = Image.open("D:\ANguyen Huu Tuan 21GIT\Term1-year3\doancs4\image\Assistant.png")
        assistant_img = assistant_img.resize((100, 100), Image.LANCZOS)  # Resize the image
        self.assistant_img = ImageTk.PhotoImage(assistant_img)

        # Create main frame
        main_frame = tk.Frame(self.root)
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # # Create label with microphone image
        # mic_img_label = tk.Label(main_frame, image=self.microphone_img)
        # mic_img_label.grid(row=0, column=0, padx=10, pady=10)

        # Create label with assistant image
        assistant_img_label = tk.Label(main_frame, image=self.assistant_img)
        assistant_img_label.grid(row=0, column=0, padx=10, pady=10)

        # Create text widget for assistant's responses
        self.assistant_text = tk.Text(main_frame, width=50, height=15)
        self.assistant_text.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=10, pady=10)

        send_img = Image.open("D:\ANguyen Huu Tuan 21GIT\Term1-year3\doancs4\image\microphone.png")
        send_img = send_img.resize((50, 50), Image.LANCZOS)  # Resize the image
        self.send_img = ImageTk.PhotoImage(send_img)

       # Create 'Send' button to send user's commands
        send_button = tk.Button(main_frame, image=self.send_img, command=self.send_command)
        send_button.grid(row=2, column=0, padx=10, pady=10)
    def send_command(self):
        # Get user's command
        user_command = self.user_entry.get()

        # TODO: Process user's command with your voice assistant here

        # Show assistant's response (for now, just echo user's command)
        self.assistant_text.insert(tk.END, "User: " + user_command + "\n")
        self.assistant_text.insert(tk.END, "Assistant: " + user_command + "\n")

        # Clear user's command
        self.user_entry.delete(0, tk.END)

root = tk.Tk()
app = VoiceAssistant(root)
root.mainloop()
