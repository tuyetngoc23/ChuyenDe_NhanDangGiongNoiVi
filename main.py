import os
import playsound
import speech_recognition
import pyttsx3
from datetime import date, datetime
from gtts import gTTS

robot_ear=speech_recognition.Recognizer()
robot_mouth = pyttsx3.init()
language = 'vi'
while True:
    with speech_recognition.Microphone() as mic:
        print("Robot: I'm listening")
        audio = robot_ear.listen(mic)

    print("Robot:...")
    try:
        you = robot_ear.recognize_google(audio, language="vi-VN")
    except:
        you = ""

    print("You: " + you)

    if you == "":
        robot_brain = "I can't hear you, try again"
    elif "chào" in you:
        robot_brain = "Xin chào"
    elif "hello" in you:
        robot_brain = "hello"
    elif "today" in you:
        today = date.today()
        now = datetime.now()
        # Textual month, day and year
        robot_brain = today.strftime("%B %d, %Y") + " " + now.strftime("%H hours %M minutes %S seconds")
    elif "time" in you:
        now = datetime.now()
        robot_brain = now.strftime("%H hours %M minutes %S seconds")
    elif "bye" in you:
        robot_brain = "Goodbye"
        print("Robot: " + robot_brain)
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()

        print("Bot: {}".format(robot_brain))
        tts = gTTS(text=robot_brain, lang=language, slow=False)
        tts.save("sound.mp3")
        playsound.playsound("sound.mp3")
        os.remove("sound.mp3")
        break
    else:
        robot_brain = "I'm fine thank you, and you"

    print("Robot: "+robot_brain)
    robot_mouth.say(robot_brain)
    robot_mouth.runAndWait()

    print("Bot: {}".format(robot_brain))
    tts = gTTS(text=robot_brain, lang=language, slow=False)
    tts.save("sound.mp3")
    playsound.playsound("sound.mp3")
    os.remove("sound.mp3")