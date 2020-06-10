'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    compare = []
    other_compare = []

    for i in arr:
        

        if i not in compare:
            compare.append(i)
        else:
            other_compare.append(i)

    single_number = 0

    for i in compare:
        if i not in other_compare:
            single_number = i

    return single_number


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")