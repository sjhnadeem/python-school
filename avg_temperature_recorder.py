midday = []
midnight = []
number_day = 1
number_night = 1

for i in range(0, 3):

    while True:
        temp_midday = input(f'Enter Day {number_day} Midday temperature: ')
        try:
            float(temp_midday)
        except ValueError:
            print ("This is not a number.\n")
            continue
        temp_midday_float = float(temp_midday)
        if temp_midday_float < -50:
            print ("Sorry, your temperature is too low.")
        elif temp_midday_float > 60:
            print("Sorry, your temperature is too high")
        else:
            midday.append(temp_midday)
            number_day += 1
            print ("Your temperature is recorded.\n")

            break

    while True:
        temp_midnight = input(f"Enter Day {number_night} midnight temperature: ")
        try:
            float(temp_midnight)
        except ValueError:
            print ("This is not a number.\n")
            continue
        temp_midnight_float = float(temp_midnight)
        if temp_midnight_float < -50:
            print ("Sorry, your temperature is too low.")
        elif temp_midnight_float > 60:
            print("Sorry, your temperature is too high")
        else:
            midnight.append(temp_midnight)
            number_night += 1
            print ("Your temperature is recorded.\n")
            break

    print(f'midday:{midday}')
    #print("Midnight:" + (midnight))

#finding the average temperature of the whole month in both miday and midnight:
total_midday = 0
total_midnight = 0

for day in range(0, len(midday)):
    total_midday = total_midday + float(midday[day])
avg_midday = total_midday / len(midday)


print (f'The average midnight temperature in the whole month is: {avg_midday}')