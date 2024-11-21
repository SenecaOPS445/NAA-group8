import psutil
import smtplib
from email.message import EmailMessage
import time

def send_email_alert(recipient_email, subject, body):
    # Email configuration
    sender_email = "ops445g8@abrarhossain.com"  # Hostinger email account
    sender_password = "#####" # Hostinger email's password
    smtp_server = "smtp.hostinger.com"
    smtp_port = 465

    # Create the email message
    msg = EmailMessage()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
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
    # Flags to track if an alert has already been sent
    cpu_alert_sent = False
    ram_alert_sent = False

    try:
        while True:
            cpu_usage = psutil.cpu_percent(interval=1)
            ram_usage = psutil.virtual_memory().percent

            print(f"CPU Usage: {cpu_usage}%")
            print(f"RAM Usage: {ram_usage}%")

            if alert_user:
                # CPU Usage Alert
                if cpu_usage > 80 and not cpu_alert_sent:
                    subject = "High CPU Usage Alert!"
                    body = f"Warning! CPU usage is at {cpu_usage}%, exceeding the threshold of 80%.\n\nDetails:\n- CPU Usage: {cpu_usage}%\n- RAM Usage: {ram_usage}%"
                    send_email_alert(recipient_email, subject, body)
                    cpu_alert_sent = True  # Set the flag to avoid repeated alerts
                elif cpu_usage <= 80:
                    cpu_alert_sent = False  # Reset flag when CPU usage returns to normal

                # RAM Usage Alert
                if ram_usage > 80 and not ram_alert_sent:
                    subject = "High RAM Usage Alert!"
                    body = f"Warning! RAM usage is at {ram_usage}%, exceeding the threshold of 80%.\n\nDetails:\n- CPU Usage: {cpu_usage}%\n- RAM Usage: {ram_usage}%"
                    send_email_alert(recipient_email, subject, body)
                    ram_alert_sent = True  # Set the flag to avoid repeated alerts
                elif ram_usage <= 80:
                    ram_alert_sent = False  # Reset flag when RAM usage returns to normal

            time.sleep(5)  # Check every 5 seconds
    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")

def main():
    print("Welcome to the System Monitoring Program!")
    alert_choice = input("Do you want to be alerted via email? (yes/no): ").strip().lower()

    if alert_choice == 'yes':
        email = input("Enter the email address to receive alerts: ").strip()
        print("Monitoring system with email alerts enabled.")
        monitor_system(alert_user=True, recipient_email=email)
    elif alert_choice == 'no':
        print("Monitoring system without email alerts.")
        monitor_system(alert_user=False)
    else:
        print("Invalid input. Exiting program.")

if __name__ == "__main__":
    main()
