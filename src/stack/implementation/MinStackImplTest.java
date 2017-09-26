package stack.implementation;

public class MinStackImplTest {
    public static void main(String[] args) {
        MinStackImpl stack = new MinStackImpl();
        stack.push(2);
        stack.push(3);
        stack.push(4);
        stack.push(12);
        stack.push(7);
        stack.push(1);

        System.out.println("Current Min: " + stack.getMin());
        System.out.println("Current Top: " + stack.peek());

        System.out.println("Removing 1 to see the next minimum value");
        stack.pop();

        System.out.println("Current Min: " + stack.getMin());
        System.out.println("Current Top: " + stack.peek());
    }
}
