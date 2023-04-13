import tkinter as tk
import pyttsx3

root = tk.Tk()
root.resizable(False, False)
root.configure(bg='blue')
root.title("Text to Speech Converter")

# Load the image file
img = tk.PhotoImage(file="C:/Users/saadg/Desktop/text-to-speech-converter/imge.png")
# Create a label with the image as the background
labelImage = tk.Label(root, image=img)
labelImage.place(x=0,y=0,relwidth=1,relheight=1)

def openConsoleInCentre():
    # Get the screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calculate the coordinates for the top-left corner of the window
    x = (screen_width / 2) - (600 / 2)  # Reuuplace 400 with the width of your window
    y = (screen_height / 2) - (300 / 2)  # Replace 300 with the height of your window

    root.geometry("600x300+{}+{}".format(int(x), int(y)))


def button_clicked(textbox):
    sentence = textbox.get("1.0", tk.END)
    obj = pyttsx3.init()
    if not sentence or sentence.isspace():
        voice = obj.say("OOPS! You forgot to enter a text...")
        obj.runAndWait()
        return voice
    else:
        voice = obj.say(sentence)
        obj.runAndWait()
    return voice


def main():
    openConsoleInCentre()
    top_label = tk.Label(root, text="TEXT TO SPEECH CONVERTER!", bg='yellow')
    label = tk.Label(root, text="Enter Your Sentence: ", bg= 'yellow')
    textbox = tk.Text(root, height=0.5, width=50)
    button = tk.Button(height=1, width=25, text="CONVERT", command=lambda: button_clicked(textbox))

    # bind Return key to button click
    textbox.bind("<Return>", lambda event: button.invoke())
    top_label.pack(pady=20)
    label.pack(padx=(0, 10), side=tk.LEFT, anchor=tk.N, pady=10)
    textbox.pack(pady=10)
    button.pack(padx=(5,90), pady=20)

    root.mainloop()


if __name__ == "__main__":
    main()
