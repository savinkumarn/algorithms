import time
from copy import deepcopy


def bubble_sort(input_list):
    temp_input_list = deepcopy(input_list)
    start = time.clock()
    length = len(input_list)
    for idx in range(0, length-1):
        flag = False
        for sec_idx in range(0, length-1-idx):
            if input_list[sec_idx] > input_list[sec_idx + 1]:
                tmp_val = input_list[sec_idx + 1]
                input_list[sec_idx + 1] = input_list[sec_idx]
                input_list[sec_idx] = tmp_val
                flag = True
        if not flag:
            break
    time_taken = (time.clock() - start) * 1000
    temp_input_list.sort()
    if input_list == temp_input_list:
        print(f'Time taken for Bubble Sort {time_taken:.3g} ms '
              f'for list length {len(input_list)}')
    else:
        print(" Bubble Sort Failed")
        print(f'Input List Sorted from internal '
              f'sort function \n {temp_input_list}')
        print(f'Input List Sorted From Bubble Sort '
              f'function \n {input_list}')
