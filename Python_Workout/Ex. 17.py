
def how_many_different_numbers(numbers_input):
    repeated = []
    different_numbers = 0
    for number in numbers_input:
        if number not in repeated:
            repeated.append(number)
            different_numbers += 1
    return different_numbers

def how_many_different_numbers_book(numbers_input):
    return len(set(numbers_input))


numbers_list = list(input("Write the list of numbers: "))
print("1", how_many_different_numbers(numbers_list))
print("2", how_many_different_numbers_book(numbers_list))