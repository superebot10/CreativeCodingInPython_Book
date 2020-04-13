print('Welcome to the Megalon Territory Adventure Game!!!')
print('****************************************************')
print('You are visiting Megalon Mountains, Atlantis.')
playername = input('Enter your username: ')
print('Hello ', playername, '!')
print('You go on an evening hike with one friend.')
#Megalon territory is dangerous, so why not?
print('You and your friend can choose one item each-')
print('map(m), flashlight(f), chocolate(c), rope(r), or stick(s).')
item = input('What do you choose?: ')
item2 = input('What does your friend choose?: ')
print('You hear a humming noise.')
yesorno = input('Do you follow the noise? Enter y for yes or n for no: ')
if yesorno == 'y':
    print('Wow! You are brave.')
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
if python_yeet == 'python':
    print('Yes, Python is my favorate programming thingie. If you have some chocolate, I can help you.')
    if item == 'c' or item2 == 'c':
        print('Luckily, you or your friend had chosen correctly!')
        print('You gave her the chocolate and helps you get home.')
        print('CONGRATS!!! You and your friend got out safely. You won!')
    else:
        print('"Aw man... You do not have chocklate? How pitiful..."' )
        print('The woman drove away.')
        print('You failed to get home safely. YOU LOST')
else:
    print('"SERIOSLY?! You think ', python_yeet, ' is my favorate language?! All I wanted was some chockolate..."')
    print('The woman drove away.')
    print('You failed to get home safely. YOU LOST')