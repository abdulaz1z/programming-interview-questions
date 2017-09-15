package general;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;

import javafx.util.Pair;

public class GeneralQuestions {
	
	//1. Find the most frequent integer in an array
    //what if multiple items occurs same many times?
    public static int findMostFrequentInteger(int[] arr){
        //this map will keep the int element as key and how many times the appear as value
        HashMap<Integer, Integer> map = new HashMap<>();

        for (Integer element : arr) {
            if (map.containsKey(element)){
                int curVal = map.get(element);
                map.put(element, curVal + 1);
            }
            else {
                map.put(element, 1);
            }
        }

        //getting the most frequent integer from the map value
        int currentMostFrequent = arr[0];
        int maxOccurred = 0;
        for (Integer item : arr) {
            int itemOccurred = map.get(item);
            if (itemOccurred > maxOccurred){
                currentMostFrequent = item;
                maxOccurred = itemOccurred;
            }
        }

        return currentMostFrequent;
    }

    //2. Find pairs in an integer array whose sum is equal to 10 (bonus: do it in linear time)
    public static List<Pair> pairsWhoseSumEqualsToTen(int[] arr) {
        //list to hold all the pair whose sums is equal to 10
        List<Pair> pairList = new ArrayList<>();

        //add it to HashSet for constant lookup
        HashSet<Integer> valueSet = new HashSet<>();
        for (Integer item : arr) {
            valueSet.add(item);
        }

        //check which pairs equals to 10
        for (Integer item : arr) {
            if (valueSet.contains(10 - item)){
                pairList.add(new Pair(item, 10 - item));
                //System.out.println("(" + item + ", " + (10 - item) + ")");
            }
        }
        return pairList;
    }

	public static void main(String[] args) {
      //1t
      int[] arr = {5,6,7,8,1,2,1,2,3};
      System.out.println(findMostFrequentInteger(arr));

      //2t
      int[] arr2 = {1,2,3,4,6};
      System.out.println(pairsWhoseSumEqualsToTen(arr2));

	}

}
