# -*- coding: utf-8 -*-
print "Willkommen zu FizzBuzz, dem neuen Spiele Spaß!"

while True:
    try:
        number = int(raw_input("Wähle eine Zahl zwischen 1 und 100: "))

        while number < 1 or number > 100:

            number= int(raw_input("Die Zahl muss zwischen 1 und 100 liegen: "))

        for x in range(1,number+1):

            if x % 3 == 0 and x % 5 == 0:
                print "FizzBuzz"

            elif x % 3 == 0:
                print "Fizz"

            elif x % 5 == 0:
                print "Buzz"
            else:
                print x
        print "Neues Spiel, neues Glück :)"
    except ValueError:
        print "Bitte nur Zahlen eingeben"