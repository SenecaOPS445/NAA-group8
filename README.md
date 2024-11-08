# Fall 2024 Assignment 2
System Monitoring Tool
This project is a Python-based system monitoring tool designed to monitor critical system metrics using only Python's standard library. The tool tracks CPU usage, memory utilization, disk space, and network activity. It generates alerts when any metric exceeds a specified threshold and logs data over time for reporting purposes. This project is platform-independent, with adaptations for both Unix/Linux and Windows operating systems.

Project Structure and Requirements
The tool is designed with the following steps:

Metric Collection:

Metrics such as CPU, memory, disk space, and network usage are collected using platform-specific commands executed through Python's subprocess module.
Parsing functions extract relevant data from command output for monitoring.
Alert Mechanism:

Alerts are displayed as console messages whenever a metric exceeds its predefined threshold.
Each metric has a configurable threshold to allow flexibility for different system loads and environments.
Data Logging and Reporting:

Data is logged at regular intervals in either JSON or text format.
A report generation function provides a summary of system health over a specified period by analyzing logged data.
Setup and Usage
Requirements
Python 3.x
Standard Library Modules: subprocess, os, time, json (no third-party libraries are used).
