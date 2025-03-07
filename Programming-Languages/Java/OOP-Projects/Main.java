class Car {
    String brand = "Toyota"; // Attribute

    void honk() {
        System.out.println("Beep Beep!");
    }
}

public class Main {
    public static void main(String[] args) {
        Car myCar = new Car(); // Object creation
        System.out.println("Brand: " + myCar.brand);
        myCar.honk();
    }
}
