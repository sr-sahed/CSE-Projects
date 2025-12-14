import java.io.*;
import java.util.ArrayList;
import java.util.List;

public class TaskManager {
    private List<AbstractTask> tasks;

    // Constructor
    public TaskManager() {
        tasks = new ArrayList<>();
    }

    // Add a task
    public void addTask(AbstractTask task) {
        tasks.add(task);
        System.out.println("Task added: " + task.getName());
    }

    // Remove a task by name
    public void removeTask(String taskName) throws TaskNotFoundException {
        AbstractTask taskToRemove = findTaskByName(taskName);
        if (taskToRemove != null) {
            tasks.remove(taskToRemove);
            System.out.println("Task removed: " + taskToRemove.getName());
        } else {
            throw new TaskNotFoundException("Task not found: " + taskName);
        }
    }

    // Mark a task as complete
    public void markTaskComplete(String taskName) throws TaskNotFoundException {
        AbstractTask taskToMark = findTaskByName(taskName);
        if (taskToMark != null) {
            taskToMark.markComplete();
        } else {
            throw new TaskNotFoundException("Task not found: " + taskName);
        }
    }

    // Display all tasks
    public void displayAllTasks() {
        if (tasks.isEmpty()) {
            System.out.println("No tasks to display.");
        } else {
            for (AbstractTask task : tasks) {
                task.displayTaskDetails();
                // Add a blank line between tasks
                System.out.println();
            }
        }
    }

    // Find a task by name
    private AbstractTask findTaskByName(String taskName) {
        for (AbstractTask task : tasks) {
            if (task.getName().equalsIgnoreCase(taskName)) {
                return task;
            }
        }
        return null; // Task not found
    }

    // Save tasks to a file
    public void saveTasks() {
        try (ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream("tasks.dat"))) {
            oos.writeObject(tasks);
            System.out.println("Tasks saved to file.");
        } catch (IOException e) {
            System.out.println("Error saving tasks: " + e.getMessage());
        }
    }

    // Load tasks from a file
    @SuppressWarnings("unchecked")
    public void loadTasks() {
        try {
            File file = new File("tasks.dat");
            if (file.exists()) {
                try (ObjectInputStream ois = new ObjectInputStream(new FileInputStream(file))) {
                    // Safely cast to List<AbstractTask>
                    tasks = (List<AbstractTask>) ois.readObject();
                    System.out.println("Tasks loaded from file.");
                }
            } else {
                System.out.println("No saved tasks found, starting fresh.");
            }
        } catch (IOException | ClassNotFoundException e) {
            System.out.println("Error loading tasks: " + e.getMessage());
        }
    }
}
