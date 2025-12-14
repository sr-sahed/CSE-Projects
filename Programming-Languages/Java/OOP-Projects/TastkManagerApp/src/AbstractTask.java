import java.io.Serializable;
import java.util.Date;

public abstract class AbstractTask implements Serializable {
    private static final long serialVersionUID = 1L;

    private String name;
    private String description;
    private Date dueDate;
    private boolean isCompleted;

    // Constructor
    public AbstractTask(String name, String description, Date dueDate) {
        this.name = name;
        this.description = description;
        this.dueDate = dueDate;
        this.isCompleted = false;
    }

    // Getters and setters for encapsulation
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public Date getDueDate() {
        return dueDate;
    }

    public void setDueDate(Date dueDate) {
        this.dueDate = dueDate;
    }

    public boolean isCompleted() {
        return isCompleted;
    }

    public void setCompleted(boolean completed) {
        isCompleted = completed;
    }

    // Abstract method to be implemented by subclasses
    public abstract void markComplete();

    // Display task details
    public void displayTaskDetails() {
        System.out.println("Task Name: " + name);
        System.out.println("Description: " + description);
        System.out.println("Due Date: " + dueDate);
        System.out.println("Completed: " + (isCompleted ? "Yes" : "No"));
    }
}
