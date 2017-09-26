//2. Find the minimum element in a stack in O(1) time
//in this case i will design a Integer stack that keeps track of minimum
//value at any given time after stack has been created
package stack.implementation;

import java.util.Stack;

public class MinStackImpl {
    //this stack will keep our elements. Note: this will not keep the actual element for the minimum element
    private Stack<Integer> stack;
    //this will keep track of the current minimum element in the stack
    private int min;

    public MinStackImpl(){
        stack = new Stack<>();
    }

    public void push(int x){
        //if the stack is empty, push x and make it current minimum
        if(stack.isEmpty()){
            stack.push(x);
            min = x;
        }
        else{
            //case 1: x is greater or equal to current minimum
            if (x >= min){
                stack.push(x);
            }
            //case 2: x is less than current minimum
            else{
                //instead of pushing the actual x, we are pushing (2x - current minimum) so that we can track back to the
                //next previous using (2min - current top element)
                stack.push((2 * x) - min);
                min = x;
            }
        }
    }

    public void pop(){
        int currentTop = stack.peek();

        //if the current top element is greater than or equal to the current minimum value, then simply pop off the top
        if(currentTop >= min){
            stack.pop();
        }
        else{
            //now we track back to the previous minimum value from the stack using (2min - current top element)
            //then remove the top
            min = (2 * min) - currentTop;
            stack.pop();
        }
    }

    public int getMin(){
        //returns the minimum in stack in O(1)
        return min;
    }

    public int peek(){
        int currentTop = stack.peek();

        //if the current top is less than or equal the current minimum then return the current minimum because
        //the current top is not an actual value. Remember for every minimum value we pushed (2x - current minimum) instead of x (line 31)
        if (currentTop <= min){
            return min;
        }
        //if the current top is greater than or equal to the minimum value then just return the current top.
        //because this is the actual value that was pushed
        else{
            return currentTop;
        }
    }

    public boolean isEmpty(){
        return stack.isEmpty();
    }
}
