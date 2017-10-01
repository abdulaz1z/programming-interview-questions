package stack;

import java.util.Stack;

public class StackQuestions {
    //4. Reverse a stack recursively
    //i will use a helper method called getBottomElement to get the bottom element of the stack
    public static void reverseStack(Stack<Integer> stack){
        //base case
        if (stack.isEmpty()){
            //return to the previous function call
            return;
        }
        //recursive case
        else{
            //get the bottom element using this method getBottomElement.
            //don't worry about how it returns the bottom element of the stack. look it that method separately
            int bottomElement = getBottomElement(stack);

            //call the reverseStack without the bottom element now
            reverseStack(stack);

            //when reverseStack function returns from the base case push bottom element on the stack
            stack.push(bottomElement);
        }
    }
    //helper method that return bottom element recursively
    private static int getBottomElement(Stack<Integer> stack) {
        //get the current top
        int top = stack.pop();

        if (stack.isEmpty()){   //if the stack is empty which means the top is the bottom element
            return top;
        }
        else{
            //this execute when the top was not the bottom element so we call the same method again
            int bottom = getBottomElement(stack);

            //push back all the top that was not the bottom element
            stack.push(top);

            //finally return the bottom
            return bottom;
        }

    }


    public static void main(String[] args) {
        //4t
//        Stack<Integer> stack = new Stack<>();
//        stack.push(2);
//        stack.push(3);
//        stack.push(4);
//        stack.push(5);
//
//        System.out.println("Original Stack:");
//        while (!stack.isEmpty()){
//            System.out.println(stack.pop());
//        }
//
//        stack.push(2);
//        stack.push(3);
//        stack.push(4);
//        stack.push(5);
//
//        reverseStack(stack);
//        System.out.println("Reversed Stack:");
//        while (!stack.isEmpty()){
//            System.out.println(stack.pop());
//        }

    }
}
