# 🔐 Suspicious Login Threat Detector

A beginner-friendly **Python cybersecurity project** that analyzes server log files and detects suspicious activity such as brute-force login attempts, blacklisted IP access, and sensitive endpoint requests. The project is geared towards common basic basic practices found in "Blue Team" CyOps. The projects current state is light weight and ran locally. Future renditions of the project will include more practical impliminations of databases and 
API generated sample tests.

---

## 📌 Overview

The **Suspicious Login Threat Detector** simulates a basic intrusion detection system used by security analysts and SOC teams. It parses log entries and flags behaviors commonly associated with attacks.

This project is ideal for:

* Cybersecurity students
* Beginner Python programmers
* Aspiring SOC analysts
* Resume / portfolio projects

---

## 🚀 Features

* Detects repeated failed login attempts (brute force attacks)
* Flags access from blacklisted IP addresses
* Identifies successful access to sensitive endpoints
* Generates a readable alert report
* Lightweight and easy to modify

---

## 📂 Project Structure

```
suspicious_login/
│── detect_threat.py
│── sample_log.txt
```

---

## 📄 Sample Log Format

```
IP_ADDRESS - STATUS PATH
```

Example:

```
192.168.1.11 - FAILED /login
10.0.0.5 - SUCCESS /admin
```

---

## ▶️ Installation & Usage

### 1️⃣ Clone the Repository

```
git clone https://github.com/AhmedMazroua/Python-projects/tree/main/suspicious_login
cd suspicious-login
```

### 2️⃣ Run the Script

```
python detect_threat.py
```

---

## 🧠 Detection Logic

The **Suspicious Login Threat Detector** checks logs for:

| Threat Type      | Detection Rule                            |
| ---------------- | ----------------------------------------- |
| Brute Force      | ≥ 3 failed login attempts from same IP    |
| Blacklisted IP   | IP appears in blacklist list              |
| Sensitive Access | Successful access to `/admin` or `/login` |

---

## ⚙️ Configuration

You can modify detection settings directly in `detect_threat.py`:

```
FAILED_LIMIT = 3
SENSITIVE_PATHS = ["/admin", "/login"]
BLACKLIST = ["45.33.32.1"]
```

---

## 🛠️ Technologies Used

* Python 3
* Standard Library (`collections`)

---

## 📈 Future Improvements

Potential enhancements:

* Real-time log monitoring
* GeoIP location lookup
* Email or webhook alerts
* CSV or JSON report export
* GUI dashboard
* Machine learning anomaly detection

---

## 🎯 Learning Objectives

This project demonstrates:

* Log analysis fundamentals
* Basic threat detection logic
* Python scripting for cybersecurity
* Security automation concepts

---

## 🤝 Contributing

Contributions are welcome!
Feel free to fork the repo and submit a pull request with improvements.

---

## 📜 License

This project is open-source and free to use for educational purposes.

---

## ⭐ Support

If you found this helpful, consider starring the repository to support the project!

---
