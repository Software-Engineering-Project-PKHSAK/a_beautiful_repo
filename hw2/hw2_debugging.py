
"""
Module to sort the given array by merge sort
"""
import rand


def merge_sort(arr_input):
    """Recursive function to split array in half, then combine the two sorted halves"""

    if len(arr_input) < 2:  # handles the input array having size 0 and 1
        return arr_input

    half = len(arr_input)//2

    return recombine(merge_sort(arr_input[:half]), merge_sort(arr_input[half:]))


def recombine(left_arr, right_arr):
    """Function to combine the two  arrays in one"""
    left_index = 0
    right_index = 0
    k = 0  # to keep track of current index in final combined array
    merge_arr = [None] * (len(left_arr) + len(right_arr))

    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            # merge_arr[left_index + right_index] = left_arr[left_index]

            merge_arr[k] = left_arr[left_index]
            left_index += 1
            k += 1
        else:
            merge_arr[k] = right_arr[right_index]

            # merge_arr[left_index + right_index] = right_arr[right_index]
            right_index += 1
            k += 1

    for i in range(right_index, len(right_arr)):
        merge_arr[k] = right_arr[i]
        k += 1

    for i in range(left_index, len(left_arr)):
        merge_arr[k] = left_arr[i]
        k += 1

    return merge_arr


arr = rand.random_array([None] * 20)
arr_out = merge_sort(arr)

print(arr_out)
