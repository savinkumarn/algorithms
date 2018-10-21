import time
from copy import deepcopy


def insertion_sort(input_list):
    temp_input_list = deepcopy(input_list)
    start = time.clock()
    length = len(input_list)
    for idx in range(1, length):
        value = input_list[idx]
        blank_idx = idx
        while value < input_list[blank_idx - 1] and blank_idx > 0:
            input_list[blank_idx] = input_list[blank_idx -1]
            blank_idx -= 1
        input_list[blank_idx] = value
    time_taken = (time.clock() - start) * 1000
    temp_input_list.sort()
    if input_list == temp_input_list:
        print(f'Time taken for Insertion Sort {time_taken:.3g} ms '
              f'for list length {len(input_list)}')
    else:
        print("Insertion Sort Failed")
        print(f'Input List Sorted from internal '
              f'sort function \n {temp_input_list}')
        print(f'Input List Sorted From Insertion Sort '
              f'function \n {input_list}')
