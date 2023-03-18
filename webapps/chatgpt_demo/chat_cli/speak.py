from gtts import gTTS
import os

# https://pypi.org/project/gTTS/
def speakText(text, filename):
    language = 'en'
    speakobj = gTTS(text=text, lang=language, slow=False)
    speakobj.save(filename + ".mp3")

def speakFile(fpath, name):
    f = open(fpath, "r")
    text = f.read()
    speakText(text, name)

speakFile("search_results/chelsea_fc.txt", "chelsea")