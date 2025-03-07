class Animal {
    void makeSound() {
        System.out.println("Animal makes a sound.");
    }
}

class Dog extends Animal {
    @Override
    void makeSound() {
        System.out.println("Dog barks.");
    }
}

public class OverridingExample {
    public static void main(String[] args) {
        Animal myDog = new Dog();
        myDog.makeSound(); // Dog's method overrides Animal's method
    }
}
