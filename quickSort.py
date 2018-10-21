import time
from copy import deepcopy


def partition(input_list, start, end):
    partition_idx = start
    pivot = input_list[end]
    for i in range (start, end):
        if input_list[i] <= pivot:
            input_list[partition_idx], input_list[i] = input_list[i], input_list[partition_idx]
            partition_idx += 1
    input_list[partition_idx], input_list[end] = input_list[end], input_list[partition_idx]
    return partition_idx


def quick_sort(input_list, start, end):
    if start < end:
        partition_idx = partition(input_list, start,end)
        quick_sort(input_list, start, partition_idx-1)
        quick_sort(input_list, partition_idx+1, end)


def quick_sort_main(input_list):
    temp_input_list = deepcopy(input_list)
    start = time.clock()
    length = len(input_list)
    quick_sort(input_list, 0, length-1)
    time_taken = (time.clock() - start) * 1000
    temp_input_list.sort()
    if input_list == temp_input_list:
        print(f'Time taken for Quick Sort {time_taken:.3g} ms '
              f'for list length {len(input_list)}')
    else:
        print("Quick Sort Failed")
        print(f'Input List Sorted from internal '
              f'sort function \n {temp_input_list}')
        print(f'Input List Sorted From Merge Sort '
              f'function \n {input_list}')
