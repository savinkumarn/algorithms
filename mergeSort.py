import time
from copy import deepcopy


def merge(l_array,r_array,input_list):
    loop_count_l = 0
    loop_count_r = 0
    main_loop_idx = 0
    left_array_len = len(l_array)
    right_array_len = len(r_array)
    while loop_count_l < left_array_len and loop_count_r < right_array_len:
        if l_array[loop_count_l] <= r_array[loop_count_r]:
            input_list[main_loop_idx] = l_array[loop_count_l]
            loop_count_l += 1
        else :
            input_list[main_loop_idx] = r_array[loop_count_r]
            loop_count_r +=1
        main_loop_idx += 1
    while loop_count_l < left_array_len:
        input_list[main_loop_idx] = l_array[loop_count_l]
        loop_count_l += 1
        main_loop_idx += 1
    while loop_count_r < right_array_len:
        input_list[main_loop_idx] = r_array[loop_count_r]
        loop_count_r += 1
        main_loop_idx += 1


def merge_sort(input_list):
    length = len(input_list)
    if length < 2:
        return
    l_array = input_list[:int(length/2)]
    r_array = input_list[int(length/2):]
    merge_sort(l_array)
    merge_sort(r_array)
    merge(l_array, r_array, input_list)


def merge_sort_main(input_list):
    temp_input_list = deepcopy(input_list)
    start = time.clock()
    merge_sort(input_list)
    time_taken = (time.clock() - start) * 1000
    temp_input_list.sort()
    if input_list == temp_input_list:
        print(f'Time taken for Merge Sort {time_taken:.3g} ms '
              f'for list length {len(input_list)}')
    else:
        print("Merge Sort Failed")
        print(f'Input List Sorted from internal '
              f'sort function \n {temp_input_list}')
        print(f'Input List Sorted From Merge Sort '
              f'function \n {input_list}')
