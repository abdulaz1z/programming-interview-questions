package string;

import java.util.HashMap;

public class StringQuestions {
	
	//1. Find the first non-repeated character in a String
	public static char firstNonRepeatedChar(String str) {
		//each char from the string will be stored as the key and number of time they appear as value.
		//this object will how many times a char occur
		HashMap<Character, Integer> map = new HashMap();

		for (int i = 0; i < str.length(); i++){
			//first char from string
			char c = str.charAt(i);

			//check if it exist in the map
			if (map.containsKey(c)){
				//get the value
				Integer currOccurrence = map.get(c);

				// now update and put it back in the map using the same key
				map.put(c, currOccurrence + 1);
			}
			else {
				//add it to the map
				map.put(c, 1);
			}
		}

		//now return the first key (char) that has a value == 1
		char firstNonRepeated = '\u0000';

		for (int j = 0; j < str.length(); j++){
			//first char from string
			char c = str.charAt(j);

			//get the value using that char
			Integer totalOccurrence = map.get(c);

			//check if totalOccurrence == 1
			if (totalOccurrence == 1){
				firstNonRepeated = c;
			}
		}
		
		
		return firstNonRepeated;
	}

	//2. Reverse a String iteratively and recursively

	//iteratively
	public static String reverseIteratively(String str){
		if (str.length() == 0) return "";
		String reverse = "";

		//looping backwards from last item to first and concatenating to reverse
		for (int i = str.length() - 1; i >= 0; i--){
			reverse += str.charAt(i);
		}
		return reverse;
	}

	//iteratively
	public static String reverseRecursively(String str){
		int length = str.length();
		//base cases
		if (length == 0) return "";	//reverse of empty string is empty
		else if (length == 1) return str;	//reverse of one char is the same char

		//recursive case
		else{
			//get the last char then call the method again from first char to second to last char
			return str.charAt(length - 1) + reverseRecursively(str.substring(0, length - 1));
		}
	}


	
	//Reverse a String iteratively and recursively
	public static void main(String[] args) {

		//1t
//		String str = "abcdefghabcdefghi";
//		System.out.println(firstNonRepeatedChar(str));
//
//		String str1 = "aaaaaaaaaaa";
//		System.out.println(firstNonRepeatedChar(str1));

		//2t
//		String str = "java";
//		System.out.println("Iteratively : " + reverseIteratively(str));
//		System.out.println("Recursively : " + reverseRecursively(str));
//		System.out.println("Iteratively : " + reverseIteratively(""));
//		System.out.println("Recursively : " + reverseRecursively(""));
	}
}
