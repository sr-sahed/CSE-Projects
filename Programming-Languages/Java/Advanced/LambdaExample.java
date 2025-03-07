interface MyInterface {
    void sayHello();
}

public class LambdaExample {
    public static void main(String[] args) {
        MyInterface obj = () -> System.out.println("Hello, Lambda!");
        obj.sayHello();
    }
}
