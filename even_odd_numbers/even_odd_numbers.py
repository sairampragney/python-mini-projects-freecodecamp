even_numbers = []

odd_numbers = []

for num in range(100):
    if num % 2 == 0:
        even_numbers.append(num)

    elif num % 2 == 1:
        odd_numbers.append(num)

print("EVEN NUMBER:", even_numbers)

print("ODD NUMBER:", odd_numbers)
