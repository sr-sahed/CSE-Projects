import java.io.Serializable;
import java.util.Date;

@SuppressWarnings("unused")
public class Task extends AbstractTask implements Serializable {
    private static final long serialVersionUID = 1L;

    public Task(String name, String description, Date dueDate) {
        super(name, description, dueDate);
    }

    // Override markComplete method for Task
    @Override
    public void markComplete() {
        setCompleted(true);
        System.out.println("Task \"" + getName() + "\" has been marked as complete.");
    }
}
