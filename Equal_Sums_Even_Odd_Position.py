first_number = int(input())
second_number = int(input())
for current_number in range(first_number, second_number + 1):
    number_to_str = str(current_number)
    even_digits = 0
    odd_digits = 0
    for index, digit in enumerate(number_to_str):
        if index % 2 == 0:
            odd_digits += int(digit)
        else:
            even_digits += int(digit)
    if even_digits == odd_digits:
        print(current_number, end=' ')
