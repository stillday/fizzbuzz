print "Willkommen zu FizzBuzz, dem neuen Spiele Spass!"

while True:
    try:
        number = int(raw_input("Waehle eine Zahl zwischen 1 und 100: "))

        for x in range(1,number+1):

            if x % 3 == 0 and x % 5 == 0:
                print "fizzbuzz"

            elif x % 3 == 0:
                print "fizz"

            elif x % 5 == 0:
                print "buzz"
            else:
                print x
        print "Neue runde, neues Glueck :)"
    except ValueError:
        print "Bitte nur Zahlen eingeben"