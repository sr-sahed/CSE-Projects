class SharedResource {
    synchronized void display(String msg) {
        System.out.print("[" + msg);
        try {
            Thread.sleep(1000);
        } catch (InterruptedException e) {
        }
        System.out.println("]");
    }
}

class MyThread extends Thread {
    SharedResource res;

    MyThread(SharedResource res) {
        this.res = res;
    }

    public void run() {
        res.display("Hello");
    }
}

public class SyncExample {
    public static void main(String[] args) {
        SharedResource res = new SharedResource();
        new MyThread(res).start();
        new MyThread(res).start();
    }
}
