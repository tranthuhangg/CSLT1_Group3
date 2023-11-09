frequency = float(input("Enter the frequency (in Hz): "))

# Check if the frequency matches any note in the table
if abs(frequency - 261.63) <= 1:
    print("The frequency corresponds to the note: C4")
elif abs(frequency - 293.66) <= 1:
    print("The frequency corresponds to the note: D4")
elif abs(frequency - 329.63) <= 1:
    print("The frequency corresponds to the note: E4")
elif abs(frequency - 349.23) <= 1:
    print("The frequency corresponds to the note: F4")
elif abs(frequency - 392.00) <= 1:
    print("The frequency corresponds to the note: G4")
elif abs(frequency - 440.00) <= 1:
    print("The frequency corresponds to the note: A4")
elif abs(frequency - 493.88) <= 1:
    print("The frequency corresponds to the note: B4")
else:
    print("The frequency does not correspond to a known note.")
    