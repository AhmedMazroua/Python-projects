Here is your **Red Hat System Monitor README** written in the same style and structure as your Suspicious Login Threat Detector README:

---

# 🐧 Red Hat System Monitor

A beginner-friendly Python system monitoring project built for Red Hat Enterprise Linux (RHEL) environments. This lightweight CLI tool monitors CPU, memory, and disk usage in real time. The project follows foundational Linux system administration and DevOps monitoring practices.

The current version runs locally in the terminal. Future versions will include logging, alerting, dashboard visualization, and service-based deployment.

---

## 📌 Overview

The Red Hat System Monitor simulates a basic system monitoring utility used by Linux administrators and DevOps engineers.

It retrieves live system performance metrics and displays them in a clean, readable format directly in the terminal.

This project is ideal for:

* Linux / Red Hat students
* Beginner Python developers
* Aspiring System Administrators
* DevOps beginners
* Resume / portfolio projects

---

## 🚀 Features

* Displays real-time CPU usage
* Shows total and used memory statistics
* Monitors disk usage on root (`/`) partition
* Auto-refreshes every few seconds
* Lightweight and easy to customize
* Runs locally with minimal dependencies

---

## 📂 Project Structure

```
redhat-system-monitor/
│── monitor.py
│── README.md
```

---

## 📊 Example Output

```
===== Red Hat System Monitor =====

CPU Usage: 18%

Memory Usage:
  Total: 15.62 GB
  Used: 6.45 GB
  Percentage: 41%

Disk Usage (/):
  Total: 100 GB
  Used: 47 GB
  Percentage: 47%
```

---

## ▶️ Installation & Usage

### 1️⃣ Clone the Repository

```
git clone https://github.com/yourusername/redhat-system-monitor.git
cd redhat-system-monitor
```

### 2️⃣ Install Dependencies

If Python is not installed:

```
sudo dnf install python3 python3-pip -y
```

Install required library:

```
pip3 install psutil
```

Alternative (RHEL native package):

```
sudo dnf install python3-psutil
```

### 3️⃣ Run the Script

```
python3 monitor.py
```

Press **CTRL + C** to stop the monitor.

---

## 🧠 Monitoring Logic

The Red Hat System Monitor collects system statistics using the `psutil` library and displays:

| Metric       | Source                    |
| ------------ | ------------------------- |
| CPU Usage    | `psutil.cpu_percent()`    |
| Memory Stats | `psutil.virtual_memory()` |
| Disk Usage   | `psutil.disk_usage('/')`  |

The script refreshes every 3 seconds to simulate continuous monitoring.

---

## ⚙️ Configuration

You can modify refresh behavior inside `monitor.py`:

```
time.sleep(3)
```

You may customize:

* Refresh interval timing
* Target disk partitions
* Output formatting
* Threshold-based alerts

---

## 🛠️ Technologies Used

* Python 3
* psutil library
* Red Hat Enterprise Linux (RHEL)
* Linux CLI

---

## 📈 Future Improvements

Potential enhancements:

* Logging system metrics to a file
* Threshold-based alert system (CPU > 80%)
* Email or webhook notifications
* Web dashboard using Flask
* Docker container support
* systemd service integration
* RPM packaging for RHEL deployment
* Database integration for historical tracking

---

## 🎯 Learning Objectives

This project demonstrates:

* Basic Linux system monitoring concepts
* Python scripting for system administration
* CLI-based application development
* Performance metric collection
* DevOps foundational practices

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repository and submit a pull request with improvements.

---

## 📜 License

This project is open-source and free to use for educational purposes.

---

## ⭐ Support

If you found this helpful, consider starring the repository to support the project!
