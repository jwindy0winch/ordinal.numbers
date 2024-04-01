ordinal_numbers = list(range(1,10))

for ordinal_number in ordinal_numbers:
    if ordinal_number % 10 == 1:
        ordinal = "st"
    elif ordinal_number % 10 == 2:
        ordinal = "nd"
    elif ordinal_number % 10 == 3:
        ordinal = "rd"
    else:
        ordinal = "th"
    print(f"{ordinal_number}{ordinal}")