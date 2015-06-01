__author__ = 'sreekala'
name = str(raw_input("Hello, What's your name: "))
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
        print ('Welcome ' + fsName + ' ' + lsName + '!')
        print ("Hello dude, how's it going?")
        itrMn = 1
for i in wmNames:
    if wmNames[i] == name:
        fsName = wmNames[i]
        lsName = i
        print ('Welcome ' + fsName + ' ' + lsName +'!')
        print ("Hey girl, whassup?")
        itrWn = 1

if itrMn==0 and itrWn == 0:
    print ('Hello, stranger! Welcome to TE!')

team = raw_input("\nWhich team do you belong to?")
print ('GOOOO.. ' + team + ' team!' )

room = raw_input("\nWhich conference room are you in?")
rooms = ['thunderdome', 'pitfall']

if room.lower() == rooms[1]:
    print "It's always freezing in there.\n"
elif room.lower() == rooms[0]:
    print "That's one huge conference room."
else:
    print "Hmm - Sorry, I'm not setup for that conference room."