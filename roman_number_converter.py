# Create Roman Numerals
tallie = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
    # add more numerals if necessary
}


def RomanNumeralToDecimal(roman_Numeral):
    sum = 0
    for i in range(len(roman_Numeral) - 1):
        left = roman_Numeral[i]
        right = roman_Numeral[i + 1]
        if tallie[left] < tallie[right]:
            sum -= tallie[left]
        else:
            sum += tallie[left]
    sum += tallie[roman_Numeral[-1]]
    return sum


# Get user input
roman_numeral = input("Enter a Roman numeral: ")

# Convert to decimal
decimal_numeral = RomanNumeralToDecimal(roman_numeral)

# Print the result
print("Decimal equivalent:", decimal_numeral)
