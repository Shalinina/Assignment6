def uneven(number_list):
    number_list.sort()
    uneven_numbers = [num for num in number_list if num % 2 != 0]
    return uneven_numbers

number_list = []
number = input("Enter the List Elements: ")
for _ in range(1, 50):
    if number != "":
        number_list.append(int(number))
        number = input("Enter the next number or quit by pressing Enter: ")
    else:
        break

print("Original list:", number_list)
uneven_list = uneven(number_list)
print("List of uneven numbers:", uneven_list)