midday = []
midnight = []

for i in range(0, 5):

    while True:
        temp_midday = input('Enter Midday temperature: \n')
        try:
            float(temp_midday)
        except ValueError:
            print ("This is not a number.\n")
            continue
        temp_midday_float = float(temp_midday)
        if temp_midday_float < -50 or temp_midday_float > 60:
            print ("Sorry, your temperature is either too high or too low.")
        else:
            midday.append(temp_midday)
            print ("Your temperature is recorded.\n")
            break

    while True:
        temp_midnight = input("Enter the temperature for midnight.\n")
        try:
            float(temp_midnight)
        except ValueError:
            print ("This is not a number.\n")
            continue
        temp_midnight_float = float(temp_midnight)
        if temp_midnight_float < -50 or temp_midnight_float > 60:
            print ("Sorry, your temperature is either too high or too low.")
        else:
            midnight.append(temp_midnight)
            print ("Your temperature is recorded.\n")
            break

print (midday, midnight)