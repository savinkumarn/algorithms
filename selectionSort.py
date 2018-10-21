import time
from copy import deepcopy


def selection_sort(input_list):
    temp_input_list = deepcopy(input_list)
    start = time.clock()
    length = len(input_list)
    for idx in range(0, length-1):
        for sec_idx in range(idx+1, length):
            if input_list[sec_idx] < input_list[idx]:
                input_list[sec_idx],input_list[idx] = input_list[idx],input_list[sec_idx]
    time_taken = (time.clock() - start) * 1000
    temp_input_list.sort()
    if input_list == temp_input_list:
        print(f'Time taken for Selection Sort {time_taken:.3g} ms '
              f'for list length {len(input_list)}')
    else:
        print(" Selection Sort Failed")
        print(f'Input List Sorted from internal '
              f'sort function \n {temp_input_list}')
        print(f'Input List Sorted From Selection Sort '
              f'function \n {input_list}')
