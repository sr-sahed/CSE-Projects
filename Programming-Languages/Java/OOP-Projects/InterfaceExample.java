interface Animal {
    void makeSound();
}

class Cat implements Animal {
    public void makeSound() {
        System.out.println("Meow Meow!");
    }
}

public class InterfaceExample {
    public static void main(String[] args) {
        Animal myCat = new Cat();
        myCat.makeSound();
    }
}
