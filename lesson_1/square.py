def square(num):

    # Check if list length is valid
    if type(num) is not int:
        raise TypeError("Length value must be Integer")
    if num < 0:
        raise ValueError("Length value must be > 0")
    if num == 0:
        return []

    square_list = []
    for i in range(0, num):
        square_list.append(i**2)
    return square_list


if __name__ == "__main__":
    print(square(10))
