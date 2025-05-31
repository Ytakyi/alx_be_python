
# Step 1: Prompt user for task details

Task = input("Enter your task description: ")
priority = input("Enter task priority level (high/medium/low): ")
Time_bound = input("Is the task time-bound? (yes/no): ")

# Step 2: Process the task based on priority

match priority:
    case 'high':
        if Time_bound == "yes"
            message = f"Task: '{Task}' is a HIGH priority task and needs attention today."
        else:
            message = f"Task: '{Task}' is a HIGH priority task"
    case 'medium':
        if Time_bound == "yes":
            message = " It requires immediate attention today!"
        else:
            message = f"Task: '{Task}' is a MEDIUM priority task."
    case 'low':
        message = f"Task: '{Task}' is a LOW priority task."
    case _:
        message = f"Task: '{Task}' has an UNKNOWN priority."


# Step 4: Print reminder
print(message)
