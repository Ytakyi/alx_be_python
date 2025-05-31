
 # task_reminder.py

# Step 1: Prompt for user input
task = input("Enter your task description: ")
priority = input("Set the task's priority (high/medium/low): ").lower()
time_bound = input("Is the task time-bound? (yes/no): ").lower()

# Step 2: Process task based on priority using match-case
match priority:
    case "high":
        message = f"Task: '{task}' is a HIGH priority task."
    case "medium":
        message = f"Task: '{task}' is a MEDIUM priority task."
    case "low":
        message = f"Task: '{task}' is a LOW priority task."
    case _:
        message = f"Task: '{task}' has an UNKNOWN priority."

# Step 3: Add extra message if task is time-bound
if time_bound == "yes":
    message += " It requires immediate attention today!"

# Step 4: Print final customized reminder
print(message)

