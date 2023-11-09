sound_level = int(input("Enter a sound level in decibels: "))

if sound_level >= 130:
    message = "Jackhammer"
elif sound_level >= 106:
    message = "Gas lawnmower"
elif sound_level >= 70:
    message = "Alarm clock"
elif sound_level >= 40:
    message = "Quiet room"
else:
    message = "Sound level is below the quietest noise in the table"

print("The sound level corresponds to:", message)