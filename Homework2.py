__author__ = 'sreekala'
__author__ = 'sreekala'
import pyttsx
engine = pyttsx.init()
engine.setProperty('rate', 100)

engine.say("Hello, state your name?")
engine.runAndWait()
name = raw_input("Hi there, what's your name?")
mnNames = {'Sawyer': 'Mark', 'Bhatia':'Ravi','Bhuiyan':'Ether', 'Bazille': 'Frantz','Almanzor':'AJ','Tropeano':'Steven','Stone':'Jameson', 'Tung':'Downey'}
wmNames = {'Vichare': 'Radhika', 'Kapoor':'Shruti', 'Zaveri':'Vai', 'Shah':'Hezal','Shaikh':'Kristina','Torres':'Maris',
           'Matos':'Maggie','Wang':'Yuxiang', 'Selvaraj':'Chitra', 'Anjum':'Uzmina', 'Kutty':'Sree'}
fsName = ''
lsName = ''
itrMn =0
itrWn = 0
for i in mnNames:
    if mnNames[i] == name:
        fsName = mnNames[i]
        lsName = i
        print ('Welcome ' + fsName + ' ' + lsName + '!' + "\nHello dude, how's it going?")
        engine.say('Welcome ' + fsName + ' ' + lsName + '!' + "\nHello dude, how's it going?")
        engine.runAndWait()
        itrMn = 1
for i in wmNames:
    if wmNames[i] == name:
        fsName = wmNames[i]
        lsName = i
        print ('Welcome ' + fsName + ' ' + lsName +'!' +'\nHey girl, whassup?')
        engine.say('Welcome ' + fsName + ' ' + lsName +'!' +'\nHey girl, whassup?')
        engine.runAndWait()
        itrWn = 1

if itrMn==0 and itrWn == 0:
    print ('Hello, stranger! Welcome to TE!')
    engine.say('Hello, stranger! Welcome to TE!')
    engine.runAndWait()
engine.say("Which team do you belong to?")
engine.runAndWait()
team = raw_input("\nWhich team do you belong to?")
print ('GOOOO.. ' + team + ' team!' )
engine.setProperty("volume", 10)
engine.say('GO ' + team + ' team')
engine.say("Which conference room are you in?")
engine.runAndWait()
room = raw_input("\nWhich conference room are you in?")
rooms = ['thunderdome', 'pitfall']

if room.lower() == rooms[1]:
    print "It's always freezing in there.\n"
    engine.say("It's always freezing in there.")
    engine.runAndWait()
elif room.lower() == rooms[0]:
    print "That's one huge conference room."
    engine.say("That's one huge conference room.")
    engine.runAndWait()
else:
    print "Hmm - Sorry, I'm not setup for that conference room."
    engine.say("Hmm - Sorry, I'm not setup for that conference room.")
    engine.runAndWait()