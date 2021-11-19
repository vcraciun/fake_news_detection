from gtts import gTTS
import os

tx = open("result.txt", "r", encoding = "utf-8")
textul = tx.read().replace("\n", " ")

limba = "ro"

output = gTTS(text=textul, lang=limba, slow=False)


output.save("audio.mp3")
tx.close()

os.system("start audio.mp3")
