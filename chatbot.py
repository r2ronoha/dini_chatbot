#!/usr/bin/python3

# my chatbot

# welcome user
print('Hello I am DIDI53! I hope you enjoy my company! ')

# ask user for their name
username = input('what is your name? Please write it in that grey rectangle.')
username_camel = "{}{}".format(username[0].upper(), username.lower()[1:])
print('nice to meet you, ' + username_camel + '!')

# checking username for a match
if username.lower() in ['arturo', 'daddy', 'papa']:
    print ("this is my creators father's name")

elif username.lower() in ['alida', 'bob', 'mumma']:
    print('Hi ' + username_camel + ', I know you dance very well you are the best mum in the world to didi!')

elif username.lower() in ["nieves", "idaisa"]:
    print("hello and goodbye")

else:
    great_day = input('Are you having a great day?')

    great_day = great_day.split(' ')
    good_list = ['Yes', 'yes', 'good', 'great', 'awesome']
    bad_list = ['No', 'no', 'not', 'bad', 'terrible']

    for word in great_day:
        if word in good_list:
            print("That's good. I'm happy for you")
            break
        elif word in bad_list:
            print("That's not good.")

        break

naughty = input("do you want to tell me anything?")
print(naughty)
naughty2 = input("anything more?")
print("{0}. {1}".format(naughty2, "goodbye"))
