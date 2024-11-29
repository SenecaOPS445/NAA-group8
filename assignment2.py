import os
import time
import smtplib
from email.message import EmailMessage


def cpu_usage():
    # Get CPU usage using /proc/stat
    try:
        with open("/proc/stat", "r") as f:
            cpu_line = f.readline()  # Read the first line with CPU stats
            cpu_values = cpu_line.split()[1:]  # Skip the 'cpu' label and get the values
            
            cpu_times = [int(value) for value in cpu_values]
            
            idle_time = cpu_times[3]  # Idle time is the fourth value
            total_time = sum(cpu_times)  # Total time is the sum of all values
            
        return (1 - idle_time / total_time) * 100
    except Exception as e:
        print(f"Error fetching CPU usage: {e}")
        return 0.0

def ram_usage():
    # Get RAM usage using /proc/meminfo
    try:
        with open("/proc/meminfo", "r") as f:
            # Read only the required lines
            mem_total = int(f.readline().split()[1])  # Total memory
            mem_free = int(f.readline().split()[1])  # Free memory
            f.readline()
        
        # Calculate used memory
        mem_used = mem_total - mem_free
        return (mem_used / mem_total) * 100
    except Exception as e:
        print(f"Error fetching RAM usage: {e}")
        return 0.0

def email_alert(recipient_email, subject, body):
    # Send an alert email using Hostinger SMTP
    sender_email = "ops445g8@abrarhossain.com"
    sender_password = "B!ngo123@@"
    smtp_server = "smtp.hostinger.com"
    smtp_port = 465

    # Create the email message
    msg = EmailMessage()
    msg["From"] = sender_email
    msg["To"] = recipient_email
    msg["Subject"] = subject
    msg.set_content(body)

    # Send the email
    try:
        with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
            server.login(sender_email, sender_password)
            server.send_message(msg)
            print(f"Alert email sent to {recipient_email}.")
    except Exception as e:
        print(f"Failed to send email: {e}")

def monitor_system(alert_user, recipient_email=None):
    # Monitor CPU and RAM usage and send alerts if thresholds are breached
    # Flags to track if an alert has already been sent
    cpu_alert_sent = False
    ram_alert_sent = False

    try:
        while True:
            # Get CPU and RAM usage
            cpu = cpu_usage()
            ram = ram_usage()

            print(f"CPU Usage: {cpu:.2f}%")
            print(f"RAM Usage: {ram:.2f}%")

            if alert_user:
                # CPU Usage Alert
                if cpu > 80 and not cpu_alert_sent:
                    subject = "High CPU Usage Alert!"
                    body = (
                        f"Warning! CPU usage is at {cpu:.2f}%, exceeding the threshold of 80%.\n\n"
                        f"Details:\n- CPU Usage: {cpu:.2f}%\n- RAM Usage: {ram:.2f}%"
                    )
                    email_alert(recipient_email, subject, body)
                    cpu_alert_sent = True  # Set the flag to avoid repeated alerts
                elif cpu <= 80:
                    cpu_alert_sent = False  # Reset flag when CPU usage returns to normal

                # RAM Usage Alert
                if ram > 80 and not ram_alert_sent:
                    subject = "High RAM Usage Alert!"
                    body = (
                        f"Warning! RAM usage is at {ram:.2f}%, exceeding the threshold of 80%.\n\n"
                        f"Details:\n- CPU Usage: {cpu:.2f}%\n- RAM Usage: {ram:.2f}%"
                    )
                    email_alert(recipient_email, subject, body)
                    ram_alert_sent = True  # Set the flag to avoid repeated alerts
                elif ram <= 80:
                    ram_alert_sent = False  # Reset flag when RAM usage returns to normal

            time.sleep(5)  # Check every 5 seconds
    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")

def main():
    # Main entry point of the program
    print("Welcome to the System Monitoring Program!")
    alert_choice = input("Do you want to be alerted via email? (yes/no): ").strip().lower()

    if alert_choice == "yes":
        email = input("Enter the email address to receive alerts: ").strip()
        print("Monitoring system with email alerts enabled.")
        monitor_system(alert_user=True, recipient_email=email)
    elif alert_choice == "no":
        print("Monitoring system without email alerts.")
        monitor_system(alert_user=False)
    else:
        print("Invalid input. Exiting program.")

if __name__ == "__main__":
    main()
