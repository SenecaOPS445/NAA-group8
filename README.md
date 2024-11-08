# System Monitoring Tool

This project is a Python-based system monitoring tool designed to monitor critical system metrics using only Python's standard library. The tool tracks CPU usage, memory utilization, disk space, and network activity. It generates alerts when any metric exceeds a specified threshold and logs data over time for reporting purposes. This project is platform-independent, with adaptations for both Unix/Linux and Windows operating systems.

## Project Structure and Requirements

The tool is designed with the following steps:

1. **Metric Collection**: 
   - Metrics such as CPU, memory, disk space, and network usage are collected using platform-specific commands executed through Python's `subprocess` module.
   - Parsing functions extract relevant data from command output for monitoring.

2. **Alert Mechanism**: 
   - Alerts are displayed as console messages whenever a metric exceeds its predefined threshold.
   - Each metric has a configurable threshold to allow flexibility for different system loads and environments.

3. **Data Logging and Reporting**:
   - Data is logged at regular intervals in either JSON or text format.
   - A report generation function provides a summary of system health over a specified period by analyzing logged data.

## How the Program Works

1. **Gathering Required Input**
   - The tool gathers input by executing platform-specific commands:
     - **CPU and Memory**: Uses `top`, `free`, or `vmstat` on Unix/Linux systems, and `systeminfo` or `tasklist` on Windows.
     - **Disk Space**: Uses `os.statvfs()` for Unix systems, and `dir` or `wmic` for Windows.
     - **Network Activity**: Uses `netstat` across both Unix/Linux and Windows.

2. **Accomplishing Requirements**
   - Each metric is collected, parsed, and checked against the set threshold. Alerts are triggered if any threshold is breached.
   - Logging functions store data at regular intervals, and a reporting function analyzes this data for system health trends.

3. **Output Presentation**
   - Alerts are printed to the console in real-time.
   - Logged data is saved in JSON or text format based on user preference.
   - Summary reports are generated from logged data, providing an overview of system health over time.

4. **Arguments and Options**
   - Thresholds, logging intervals, and output formats can be customized via command-line arguments to suit different monitoring needs.

5. **Challenges**
   - Parsing platform-specific command outputs accurately is challenging, as each operating system has unique formats.
   - Ensuring compatibility across Unix/Linux and Windows adds complexity to the codebase.
   - Configuring alerts and logging functions to handle edge cases, such as command failures or unexpected output, requires thorough testing.
