# Fall 2024 Assignment 2

## GROUP 8:
## OPS445(NAA)


Group Members:

Mohd Abrar Hossain – 170352215

Mohammad Iqbal – 105830228

Bishwash B C - 184751212



## Ideas:
1.	User reports and management
2.	Systems monitoring and alerts (approved by all)
3.	Diagnostics and health






### Step 1: Project Requirements
1.	Identify the Metrics to Monitor:
o	Decide which system metrics are critical to monitor, such as CPU usage, memory utilization, disk space, and network activity.
o	Set thresholds for each metric. For example, CPU usage above 80% might trigger an alert.
2.	Alert Mechanisms:
o	Determine how alerts will be communicated. Options include console alerts, or email notifications.


### Step 2: Divide Tasks Among Group Members
1.	Metric Collection:
o	Assign a member to focus on gathering data for each metric (e.g., one person for CPU, one for memory, one for disk space etc.).
2.	Alert System Design:
o	Have one or two group members work on designing and implementing the alert mechanism. This includes:
	Writing functions to check if any metric exceeds its threshold.
	Designing notifications (e.g., print statements or emails) to inform when thresholds are breached.


### 3.	Logging and Reporting:
1.	Monitoring Functions:
o	Each group member writes a function for their metric, e.g., monitor_cpu(), monitor_memory(), etc.
o	Test each function independently to make sure it works as expected.
2.	Logging Functions:
o	Decide on the format for logging data (e.g., JSON or text).



### Step 4: Integrate and Test
1.	Combine Functions:
o	Merge the individual functions into a single script.
o	Create a main function that calls each metric monitoring function in a loop (e.g., every 30 seconds).
2.	Testing:
o	Test the script on a real system.
o	Adjust thresholds and logging intervals as necessary.


### Step 5: Finalize and Document
1.	Add Documentation:
o	Include comments and docstrings in the code for clarity.
o	Prepare slides or notes that explain the project setup, how each function works, and the alerting process.
o	Plan a demo to showcase the project in action.
Each group member can present their part, which shows the process from metric collection to alert notifications.

### Notes:
Use the Wall command on matrix to send alerts and pings to the user.
Matrix built-in email could be used as a way to alert the user.

