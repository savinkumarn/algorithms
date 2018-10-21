# This is the main program to invoke the algorithm sripts
from selectionSort import selection_sort
from bubbleSort import bubble_sort
from listGenerator import get_list_for_testing
from insertionSort import insertion_sort
from mergeSort import merge_sort_main
from copy import copy


def main():
    list_lengths = [10, 100, 99, 999, 1000]
    #list_lengths = [10]
    for list_len in list_lengths:
        input_list = get_list_for_testing(list_len)
        #input_list = [7, 4, 5, 1, 3, 2, 6, 8]
        selection_sort(copy(input_list))
        bubble_sort(copy(input_list))
        insertion_sort(copy(input_list))
        merge_sort_main(copy(input_list))


if __name__ == '__main__':
    main()
