class Person {
    String name;

    // Default Constructor
    Person() {
        name = "Unknown";
    }

    // Parameterized Constructor
    Person(String newName) {
        name = newName;
    }
}

public class ConstructorExample {
    public static void main(String[] args) {
        Person p1 = new Person(); // Default constructor
        Person p2 = new Person("Alice"); // Parameterized constructor

        System.out.println("Person 1: " + p1.name);
        System.out.println("Person 2: " + p2.name);
    }
}
