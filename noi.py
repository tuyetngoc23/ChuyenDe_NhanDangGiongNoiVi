import pyttsx3

robot_brain="hello, Nga"

robot_mouth = pyttsx3.init()
robot_mouth.say(robot_brain)
robot_mouth.runAndWait()