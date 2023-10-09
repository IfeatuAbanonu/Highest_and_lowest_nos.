list_of_numbers = []
#
for i in range(1, 11):
    value = eval(input("Enter number " + str(i) + ": "))
    list_of_numbers.append(value)

lowest_number = list_of_numbers[0]
highest_number = list_of_numbers[0]

for i in range(len(list_of_numbers)):
    if lowest_number > list_of_numbers[i]:
        lowest_number = list_of_numbers[i]

    elif highest_number < list_of_numbers[i]:
        highest_number = list_of_numbers[i]

print(f"The lowest number of your list is: {lowest_number}")
print(f"The highest number of your list is: {highest_number}")
