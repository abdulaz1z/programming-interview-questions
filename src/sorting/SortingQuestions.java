package sorting;

import java.util.Arrays;

public class SortingQuestions {

    //1. Implement bubble sort O(n^2)
    public static int[] bubbleSort(int[] arr){
        int length = arr.length;    //size of the array

        //looping through all elements in the array arr and for each iteration
        //it loops through again from first element to the last element and for each iteration
        //it checks if the adjacent elements are in wrong order and if they are then swapping them to correct the order
        for (int i = 0; i< length; i++){
            for (int j = 0; j< length - i - 1; j++){
                if (arr[j] > arr[j + 1]){
                    //swapping the elements here
                    int temp = arr[j + 1];
                    arr[j + 1] = arr[j];
                    arr[j] = temp;
                }
            }
        }

        return arr;
    }

    //2. Implement selection sort O(n^2)
    /*
    This sorting algorithm is an in-place comparison-based algorithm in which the list is divided into two parts,
    the sorted part at the left end and the unsorted part at the right end. Initially, the sorted part is empty
    and the unsorted part is the entire list.
     */
    public static int[] selectionSort(int[] arr){
        int length = arr.length;    //size of the array
        int indexOfMinElement;
        int temp;

        for (int i = 0; i < length; i++){
            indexOfMinElement = i;  //assuming the ith element to be the smallest at start of the inner loop
            for (int j = i + 1; j < length; j++){
                if (arr[j] < arr[indexOfMinElement]){
                    //updating with the next minimum value index
                    indexOfMinElement = j;
                }
            }
            //swapping the current minimum to be in the sorted portion of the array
            temp = arr[i];
            arr[i] = arr[indexOfMinElement];
            arr[indexOfMinElement] = temp;
        }
        return arr;
    }

    public static void main(String[] args) {
        //1t
//        int[] a = {4,3,6,9,1,6,0};
//        int[] result = bubbleSort(a);
//        System.out.println(Arrays.toString(result));
//
//        int[] b = {4};
//        int[] result2 = bubbleSort(b);
//        System.out.println(Arrays.toString(result2));
//
//        int[] c = {};
//        int[] result3 = bubbleSort(c);
//        System.out.println(Arrays.toString(result3));

        //2t
//        int[] arr = {4,3,6,9,1,6,0};
//        int[] result = selectionSort(arr);
//        System.out.println(Arrays.toString(result));
//
//        int[] arr2 = {1,2,3,4,5,6,7};
//        int[] result2 = selectionSort(arr2);
//        System.out.println(Arrays.toString(result2));
//
//        int[] arr3 = {};
//        int[] result3 = selectionSort(arr3);
//        System.out.println(Arrays.toString(result3));
    }
}
