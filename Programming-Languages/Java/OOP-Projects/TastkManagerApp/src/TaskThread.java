public class TaskThread implements Runnable {
    private TaskManager taskManager;
    private String taskName;
    private String action; // Action to be performed: "complete" or "remove"

    // Constructor
    public TaskThread(TaskManager taskManager, String taskName, String action) {
        this.taskManager = taskManager;
        this.taskName = taskName;
        this.action = action;
    }

    // The run() method will execute the task
    @Override
    public void run() {
        try {
            // Perform action based on the 'action' value
            if ("complete".equalsIgnoreCase(action)) {
                taskManager.markTaskComplete(taskName);
            } else if ("remove".equalsIgnoreCase(action)) {
                taskManager.removeTask(taskName);
            } else {
                System.out.println("Unknown action: " + action);
            }
        } catch (TaskNotFoundException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }

    // Start the thread to perform the task
    public void start() {
        Thread thread = new Thread(this);
        thread.start();
    }
}
