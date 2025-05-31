
# Step 1: Prompt user for task details
Task = input("Enter your task description: ")
Priority = input("Set the task's priority (high/medium/low): ").lower()
Time_bound = input("Is the task time-bound? (yes/no): ").lower()

# Step 2: Process the task based on priority
match priority:
    case "high":
        if Time_bound == "yes"
            message = f"Task: '{task}' is a HIGH priority task and needs attention today."
        else:
            message = f"Task: '{task}' is a HIGH priority task"
    case "medium":
        if time_bound == "yes":
            message = " It requires immediate attention today!"
        else:
            message = f"Task: '{task}' is a MEDIUM priority task."
    case "low":
        message = f"Task: '{task}' is a LOW priority task."
    case _:
        message = f"Task: '{task}' has an UNKNOWN priority."


# Step 4: Print reminder
print(message)
