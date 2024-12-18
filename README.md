# System Monitoring and Alert Program

This Python program monitors the system's **CPU** and **RAM usage** in real time. It provides optional email alerts when usage exceeds predefined thresholds, making it ideal for system administrators and IT professionals to track and respond to high system resource consumption.

---

## 🚀 Features

- **Real-Time Monitoring**:
  - Tracks **CPU usage** and **RAM usage** in real-time.
  - Displays usage percentages in the console every 5 seconds.
  
- **Email Alerts**:
  - Sends email alerts when:
    - **CPU usage** exceeds 80%.
    - **RAM usage** exceeds 80%.
  - Prevents duplicate alerts for the same condition by using alert flags.
  
- **User Interaction**:
  - Asks if email alerts are desired.
  - Allows users to specify the recipient email address.

---

## 📋 Requirements

- Python 3.6 or later
- **os** library for system monitoring
- A Hostinger email account for sending alerts

---

## 🛠 Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/SenecaOPS445/NAA-group8.git
   cd NAA-group8
   python3 ./assignment2.py
