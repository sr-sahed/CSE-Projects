import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Scanner;

public class TaskManagerApp {
    private static TaskManager taskManager = new TaskManager(); // TaskManager instance
    private static Scanner scanner = new Scanner(System.in); // Scanner for user input

    public static void main(String[] args) {
        // Load tasks from file
        taskManager.loadTasks();

        while (true) {
            // Display menu options
            System.out.println("\nTask Manager Menu:");
            System.out.println("1. Add Task");
            System.out.println("2. Add Urgent Task");
            System.out.println("3. Mark Task Complete");
            System.out.println("4. Remove Task");
            System.out.println("5. Display All Tasks");
            System.out.println("6. Save Tasks to File");
            System.out.println("7. Exit");
            System.out.print("Choose an option: ");

            int choice = scanner.nextInt();
            scanner.nextLine();

            switch (choice) {
                case 1:
                    addTask();
                    break;
                case 2:
                    addUrgentTask();
                    break;
                case 3:
                    markTaskComplete();
                    break;
                case 4:
                    removeTask();
                    break;
                case 5:
                    displayAllTasks();
                    break;
                case 6:
                    saveTasks();
                    break;
                case 7:
                    System.out.println("Exiting program...");
                    System.exit(0);
                    break;
                default:
                    System.out.println("Invalid choice! Please try again.");
            }
        }
    }

    // Method to add a new task
    private static void addTask() {
        System.out.print("Enter task name: ");
        String name = scanner.nextLine();
        System.out.print("Enter task description: ");
        String description = scanner.nextLine();
        System.out.print("Enter due date (YYYY-MM-DD): ");
        String dueDateStr = scanner.nextLine();

        try {
            // Define a date format and parse the user input
            SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd");
            // Parse the date using the specified format
            Date dueDate = sdf.parse(dueDateStr);
            Task task = new Task(name, description, dueDate);
            taskManager.addTask(task);
        } catch (Exception e) {
            System.out.println("Invalid date format! Please try again.");
        }
    }

    // Method to add a new urgent task
    private static void addUrgentTask() {
        System.out.print("Enter task name: ");
        String name = scanner.nextLine();
        System.out.print("Enter task description: ");
        String description = scanner.nextLine();
        System.out.print("Enter due date (YYYY-MM-DD): ");
        String dueDateStr = scanner.nextLine();
        System.out.print("Enter priority level (1 to 5): ");
        int priorityLevel = scanner.nextInt();
        scanner.nextLine();

        try {
            // Parse date with a defined format
            SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd");
            Date dueDate = sdf.parse(dueDateStr);
            UrgentTask urgentTask = new UrgentTask(name, description, dueDate, priorityLevel);
            taskManager.addTask(urgentTask);
        } catch (Exception e) {
            System.out.println("Invalid date format or priority level! Please try again.");
        }
    }

    // Method to mark a task as complete
    private static void markTaskComplete() {
        System.out.print("Enter the task name to mark as complete: ");
        String taskName = scanner.nextLine();

        // Create a TaskThread to mark the task complete in the background
        TaskThread taskThread = new TaskThread(taskManager, taskName, "complete");
        taskThread.start();
        // Start the thread to complete the task
    }

    // Method to remove a task
    private static void removeTask() {
        System.out.print("Enter the task name to remove: ");
        String taskName = scanner.nextLine();

        // Create a TaskThread to remove the task
        TaskThread taskThread = new TaskThread(taskManager, taskName, "remove");
        taskThread.start();
        // Start the thread to remove the task
    }

    // Method to display all tasks
    private static void displayAllTasks() {
        taskManager.displayAllTasks();
    }

    // Method to save tasks to a file
    private static void saveTasks() {
        taskManager.saveTasks();
    }
}
