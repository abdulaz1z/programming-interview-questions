//1. Implement a stack with push and pop functions
//this is going to be a fixed sized generics stack using array
package stack.implementation;

public class StackImpl<T> {
    //this is an array of type T and T will be determined by the user of the stack
    private T[] data;
    private int top = -1;

    public StackImpl(int size){
        data = (T[]) new Object[size];
    }

    //this puts element on top of the stack
    public void push(T element){
        top++;
        data[top] = element;
    }

    //this will return the top element
    public T pop(){
        T temp = data[top];
        top--;
        return temp;
    }

    //this checks if the stack is empty
    public boolean isEmpty(){
        return top == -1;
    }
}
