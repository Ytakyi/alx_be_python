
# Step 1: Prompt user for task details
task = input("Enter your task description: ")
priority = input("Set the task's priority (high/medium/low): ").lower()
time_bound = input("Is the task time-bound? (yes/no): ").lower()

# Step 2: Process the task based on priority
match priority:
    case "high":
        message = f"Task: '{task}' is a HIGH priority task."
    case "medium":
        message = f"Task: '{task}' is a MEDIUM priority task."
    case "low":
        message = f"Task: '{task}' is a LOW priority task."
    case _:
        message = f"Task: '{task}' has an UNKNOWN priority."

# Step 3: Modify message if task is time-bound
if time_bound == "yes":
    message += " It requires immediate attention today!"

# Step 4: Print reminder
print(message)
