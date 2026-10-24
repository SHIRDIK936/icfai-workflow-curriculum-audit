def find_max(numbers):
    largest = numbers[0]
    for num in numbers[1:]:
        if num > largest:
            largest = num
    return largest


assert find_max([1, 5, 3]) == 5
assert find_max([-8, -2, -10]) == -2
assert find_max([7]) == 7
assert find_max([4, 4, 4]) == 4

print("PASS: Computer Programming - 4/4 tests")