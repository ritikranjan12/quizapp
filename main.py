import time
import speech_recognition as sr
import pyttsx3
import json
from urllib.request import urlopen
from colored import fg


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
for voice in voices:
    engine.setProperty("rate",170)
    engine.setProperty("voice",voices[1].id,)

def speak(text):
        engine.say(text)
        engine.runAndWait()

def audio():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)

            try:
                statement = r.recognize_google(audio, language='en-in')  # en at hi for english

            except Exception:
                return "None"

            return statement

color = fg('red')
color1 = fg('white')
color2 = fg('blue')
color3 = fg('green')
color4 = fg('yellow')
print()
print(color +"Game of knowledge ")
speak("Please Give your name to proceed")
pname = audio().lower()
print()
print(color1+"Rules of the Game are as follows: ")
print(color4+" 1. For every correct question you get 10 points ")
print(color4+" 2. For every wrong answer you get -10 points")
print(color4+" 3. if the answer given in option 1 is correct then type the answer as option1 and so on ")
print(color4+" 4. if you get 100 points you are the winner ")
print()
print(color3+"Game is starting...")
time.sleep(8)


def game(n=0,name=pname,score=0):

        print()

        if score<0:
            print(color+"Game over " + name + " Your Score is " + str(score))
            speak("Game over " + name + " Your Score is " + str(score))
            exit()
        if score>=100:
            print(color3+"You are the Ultimate Winner " + name)
            speak("Congratulation " + name + " you won this game in a heroic way")
            exit()
        elif score>=10:
            print(color+"Your Score is "+str(score))
            print()
            if score == 30:
                speak("you are now 2 steps from becoming winner !")
                print(color3 + "you are now 2 steps from becoming winner !")
                print()
            if score == 60:
                speak("you are now 1 steps from becoming winner !")
                print(color3 + "you are now 1 steps from becoming winner !")
                print()

            if score == 90:
                speak("you are just 1 question away from becoming winner !")
                print(color3 + "you are just 1 question away from becoming winner !")
                print()

        url = 'http://127.0.0.1:8000/questionapi/?format=json'
        response = urlopen(url)
        data = json.load(response)
        quizq = data[n]
        question = quizq['question']
        option1 = quizq['option1']
        option2 = quizq['option2']
        option3 = quizq['option3']
        option4 = quizq['option4']
        answer = quizq['answer']

        print(color1+"Question " + str(n+1) +"  : "+ question)
        speak("Question " + str(n+1) +"  ,"+ question)
        print()
        print(color2+"Option 1 :  " + option1)
        speak("Option1 is " + option1)
        print(color2+"Option 2 :  " +option2)
        speak("Option2 is " + option2)
        print(color2+"Option 3 :  " +option3)
        speak("Option 3 is " + option3)
        print(color2+"Option 4 :  " +option4)
        speak("Option 4 is " + option4)

        speak("Enter your answer")
        print()
        ans = input(color3+"Enter your Answer: ")
        if ans == answer:
            speak("This is correct answer !!")
            score+=10
            game(n+1,pname,score)

        else:
            speak("This is an incorrect answer")
            score -= 10
            game(n + 1, pname, score)

if __name__=='__main__':
    game(0)