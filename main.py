import cv2
import easyocr
import matplotlib.pyplot as plt
from gtts import gTTS
import os
from pygame import mixer
import time

mixer.init()

cap = cv2.VideoCapture(0)
while not cap.isOpened():
    print("You messed up man")
    exit()
while True:
    ret, frame = cap.read()

    language = 'en'
    counter = 0

    img_path = "data/test3.png"
    img = frame
    reader = easyocr.Reader([language], gpu=False)

    text = reader.readtext(img) 

    for t in text:
        counter += 1
        bbox, text, score = t

        myObj = gTTS(text=text, lang=language, slow=False)
        myObj.save(f"text{counter}.mp3")
        
        mixer.music.load(f"text{counter}.mp3")
        mixer.music.play()

        while mixer.music.get_busy():  # wait for music to finish playing
            time.sleep(0.3)

        print(text)