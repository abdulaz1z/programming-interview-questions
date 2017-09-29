package sorting;

import java.util.Arrays;

public class SortingQuestions {

    //1. Implement bubble sort
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

    }
}
