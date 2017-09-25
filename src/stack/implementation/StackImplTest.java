package stack.implementation;

public class StackImplTest {
    public static void main(String[] args) {
        //Stack of Integer
        StackImpl<Integer> stack = new StackImpl<>(10);
        stack.push(2);
        stack.push(3);
        stack.push(4);

        while (!stack.isEmpty()){
            System.out.println(stack.pop());
        }

        //Stack of String
        StackImpl<String> stringStack = new StackImpl<>(10);
        stringStack.push("Abdul");
        stringStack.push("Alex");
        stringStack.push("Felix");

        while (!stringStack.isEmpty()){
            System.out.println(stringStack.pop());
        }
    }
}
