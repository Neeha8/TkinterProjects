from gtts import gTTS
import os
from tkinter import filedialog
import time
from tkinter import *

def textToSpeech():
    filename = filedialog.askopenfilename(initialdir='/',title="Select a file to compress")

    with open(filename) as file:
        for line in file:
            output = gTTS(text=line,lang='en',slow=False)
            os.remove('output5.mp3')
            time.sleep(5)
            output.save('output5.mp3')
            time.sleep(5)
            os.system("start output5.mp3")
            time.sleep(10)

root = Tk()
canvas = Canvas(root, width=400, height=300)
canvas.pack()



button = Button(text="Start", command = lambda: textToSpeech())
canvas.create_window(200,230,window=button)



root.mainloop()