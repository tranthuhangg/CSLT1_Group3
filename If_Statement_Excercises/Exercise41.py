note = input("Enter the note name: ")

# Separate the note name into letter and octave number
letter = note[0]
octave = int(note[1])

# Compute the frequency of the note in the fourth octave
if letter == "C":
    frequency = 261.63
elif letter == "D":
    frequency = 293.66
elif letter == "E":
    frequency = 329.63
elif letter == "F":
    frequency = 349.23
elif letter == "G":
    frequency = 392.00
elif letter == "A":
    frequency = 440.00
elif letter == "B":
    frequency = 493.88
else:
    print("Invalid note name.")

# Adjust the frequency based on the octave number
x = 2 ** (4 - octave)
frequency = frequency/x

print("The frequency of", note, "is", frequency, "Hz.")