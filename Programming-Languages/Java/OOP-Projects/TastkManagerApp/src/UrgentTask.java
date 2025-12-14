import java.util.Date;

public class UrgentTask extends Task {
    private static final long serialVersionUID = 1L;

    private int priorityLevel;

    public UrgentTask(String name, String description, Date dueDate, int priorityLevel) {
        super(name, description, dueDate);
        this.priorityLevel = priorityLevel;
    }

    // Getter and Setter for priority level
    public int getPriorityLevel() {
        return priorityLevel;
    }

    public void setPriorityLevel(int priorityLevel) {
        this.priorityLevel = priorityLevel;
    }

    @Override
    public void displayTaskDetails() {
        super.displayTaskDetails(); // Show common task details
        System.out.println("Priority Level: " + priorityLevel);
    }

    @Override
    public void markComplete() {
        super.markComplete();
        System.out.println("Urgent task \"" + getName() + "\" has been completed!");
    }
}
