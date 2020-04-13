print('Welcome to the Megalon Territory Adventure Game!!!')
print('****************************************************')
print('You are visiting Megalon Mountains, Atlantis.')
playername = input('Enter your username: ')
print('Hello ', playername, '!')
print('You go on an evening hike with one friend.')
#Megalon territory is dangerous, so why not?
print('You and your friend can choose one item each-')
print('map(m), flashlight(f), chocolate(c), rope(r), stick(s), or a medical kit(md).')
item = input('What do you choose?: ')
item2 = input('What does your friend choose?: ')
print('You hear a humming noise.')
yesorno = input('Do you follow the noise? Enter y for yes or n for no: ')
if yesorno == 'y':
    print('Wow! You are brave.')
    print('You start walking toward the noise. The humming noise suddenly stops.')
    print('You realize you are LOST!!!')
    chooseDir = input('Do you go North (n), South (s), East (e), or West (w)?: ')
    if chooseDir.lower() == 'n':
        print('You reach an abandoned cabin.')
        uhoh = input('Do you search the cabin (sc) or stop to make a call (c)?: ')
        while uhoh == 'c':
            print('The call does not go through.')
            uhoh = input('Do you search the abandoned cabin (sc) or try calling again (c)?: ')
        print('You search the cabin. You realize you are in a ghost town called Titanium Town.')
        print('If you have a map, you could find your way home from here.')
        if item.lower() == 'm' or item2.lower() == 'm':
            print('Luckily, you or your friend chose correctly!')
            print('You use the map to get home.')
            print('CONGRATS! You and your friend got home safely. You won!')
        else:
            print('Uh-oh. Looks like you didn\'t bring a map.')
            print('You failed to get home safely. YOU LOST')
    elif chooseDir.lower() == 'w':
        print('You walk for hours.')
        print('You trip on a fallen log and hurt your leg.')
        print('If you have a medical kit, you can heal yourself.')
        if item.lower() == 'md' or item2.lower() == 'md':
            print('Luckily, you or your friend has chosen correctly.') 
            print('You use the medical kit to heal yourself.')
            print('You realize you are in Hideaway Hollow, thanks to all the little burrows.')
            print('If you or your friend has a map, you could find your way home from here.')
            if item2.lower() == 'm' or item.lower() == 'm':
                print('You use the map to get home from here.')
                print('CONGRATS!!! You and your friend got home safely. You won!')
            else: 
                print('Unfortunately, you did not think to get a map.')
                print('You failed to get home safely. YOU LOST')
        else:
            print('You sit and wait for help to come. This could take awhile...')
            print('You failed to get home safely. YOU LOST.')
    elif chooseDir.lower() == 's':
        print('You come across a broken bridge.')
        print('If you have a stick or rope, you could fix the bridge.')
        if item.lower() == 'r' or item.lower() == 's' or item2.lower() == 'r' or item2.lower() == 's':
            print('Luckily, you or your friend has chosen correctly.')
            print('With the help of your friend, you fix the bridge and cross.')
            print('By the time you are done, it is very dark.')
            if item.lower() == 'f' or item2.lower() == 'f':
                print('Luckily, you brought along a flashlight.')
                print('You can see camp from here!')
                print('"Why, hello ', playername, '! Good to see you!" Your sister says.')
                print('You say hi back and head inside.')
                print('CONGRATS!!! You got home safely. You won!')
            else:
                go = input('Do you keep wandering (w) or stay put (p)?: ')
                if go == 'w':
                    print('You decide to walk around for a bit.')
                    print('Eventually, you come across a steep hill.')
                    up = input('Do you climb the hill (c) or stay put (p)?: ')
                    if go == 'c':
                        print('You climb up the hill.')
                        print('You can see the cabin from here!')
                        print('CONGRATS!!! You got home safely. You won!')
                    else:
                        print('Good idea. You decided to stay put.')
                        print('This could be a long night...')
                        print('You failed to get home safely. YOU LOST')
                else:
                    print('Good idea. You decide to stay put.')
                    print('This could be a long night...')
                    print('You failed to get home safely. YOU LOST')
        else:
            print('Unfortunately, you don\'t have the supplies.')
            print('You failed to get home safely. YOU LOST')
    else:
        print('You reach the highway.')
        print('It is very dark.')
        if item.lower() == 'f' or item2.lower() == 'f':
            print('Luckily, you happened to bring a flashlight.')
            print('You signal for help. A car picks you up.')
            print('The driver asks, "Do you have a map?"')
            if item.lower() == 'm' or item2 == 'm':
                print('"Great! I\'ll be glad to bring you home!"')
                print('The man drives you back to the cabin.')
                print('CONGRATS!!! You got home safely. You won!')
            else:
                print('"Sorry, buddy. I can\'t help you without a map."')
                print('You failed to get home safely. YOU LOST')
        else:
            print('Unfortunately, it is too dark for anyone to see you.')
            print('You failed to get home safely. YOU LOST')
else:
    print('Good idea. You are not taking risks.')
    print('You walk back toward the starting point. You realize you are LOST!!!')
    print('The sound is getting louder. You panic!')
    run_or_lose = input('Do you start running (r) or stop to make a call? (c): ')
    while (run_or_lose == 'c'):
        print('The call does not go through.')
        run_or_lose = input('Do you want to run (r) or try calling again?: ')
    print('You are running fast. The sound gets really loud.')
    print('A woman on an electric scooter comes up behind you.')
    python_yeet = input('She asks, "Name my favorate computer programming language: ')
    if python_yeet.lower() == 'python':
        print('Yes, Python is my favorate programming language. If you have some chocolate, I can help you.')
        if item == 'c' or item2 == 'c':
            print('Luckily, you or your friend had chosen correctly!')
            print('You gave her the chocolate and helps you get home.')
            print('CONGRATS!!! You and your friend got out safely. You won!')
        else:
            print('"Aw man... You do not have chocolate? How pitiful..."' )
            print('The woman drove away.')
            print('You failed to get home safely. YOU LOST')
    else:
        print('"SERIOUSLY?! You think ', python_yeet, ' is my favorate programming language?! All I wanted was some chocolate..."')
        print('The woman drove away.')
        print('You failed to get home safely. YOU LOST')