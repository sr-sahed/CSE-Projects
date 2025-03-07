import java.lang.reflect.Method;

class MyClass {
    public void showMessage() {
        System.out.println("Hello Reflection!");
    }
}

public class ReflectionExample {
    public static void main(String[] args) {
        try {
            Class<?> obj = MyClass.class;
            Method method = obj.getMethod("showMessage");
            method.invoke(obj.getDeclaredConstructor().newInstance());
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
