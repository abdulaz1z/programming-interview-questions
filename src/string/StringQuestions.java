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

	//recursively
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

	//3. Determine if 2 Strings are anagrams
	//Anagram means a word, phrase, or name formed by rearranging the letters of another, such as cinema, formed from iceman.
	//it will return true for anagram and false otherwise
	//assuming two empty strings are anagram
	public static boolean isAnagram(String a, String b){
		if (a.length() != b.length()) return false;
		//this map will keep count of how many times each char appear in the string
		HashMap<Character, Integer> map = new HashMap<>();

		//this loop is to count how many times char in a appears
		for (int i = 0; i < a.length(); i++) {
			//getting the first char
			char c = a.charAt(i);

			//checking if it already appeared, if it did, incrementing by 1
			if (map.containsKey(c)){
				int value = map.get(c);
				map.put(c, value + 1);
			}
			else {
				//just add it to the map because it's the first time it appeared
				map.put(c, 1);
			}
		}

		//this loop is to see how many times char in b appears
		for (int j = 0; j < b.length(); j++) {
			//getting the first char
			char c = b.charAt(j);

			//checking if it exist in map, if it does, decrementing by 1
			if (map.containsKey(c)){
				int value = map.get(c);
				map.put(c, value - 1);
			}
			else {
				//return false because if the char does not exist in map then it cant be anagram
				//anagram has same char just rearranged
				return false;
			}
		}

		//now check for all char in string a, the value must be 0 for it to be an anagram
		for (int k = 0; k < a.length(); k++) {
			char c = a.charAt(k);
			int val = map.get(c);

			if (val != 0){
				return false;
			}
		}
		return true;
	}


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

		//3t
//		String a = "cinema";
//		String b = "iceman";
//		System.out.println(isAnagram(a, b));
//
//		String c = "cin";
//		String d = "nim";
//		System.out.println(isAnagram(c, d));
//
//		String e = "";
//		String f = "";
//		System.out.println(isAnagram(e, f));

	}
}
