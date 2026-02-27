# 🔐 Password Strength Checker

A beginner-friendly Python cybersecurity project that evaluates password strength based on common security best practices. The project focuses on enforcing basic password policies often used in authentication systems and security frameworks. The current version is lightweight and runs locally in the terminal. Future versions may include GUI integration, password generation, and breach database checks.

---

## 📌 Overview

The Password Strength Checker simulates a simple password policy enforcement tool used in secure systems. It analyzes user input and determines whether a password meets essential security requirements.

This project is ideal for:

- Cybersecurity students  
- Beginner Python programmers  
- Aspiring SOC / Blue Team analysts  
- Resume / portfolio projects  
- Anyone learning secure authentication basics  

---

## 🚀 Features

- Validates minimum password length (8+ characters)
- Detects uppercase letters
- Detects lowercase letters
- Detects numeric digits
- Detects special characters
- Classifies password strength (Weak, Moderate, Very Strong)
- Provides improvement suggestions
- Lightweight and easy to modify

---

## 📂 Project Structure

password-strength-checker/
│── password_checker.py

---

## ▶️ Installation & Usage

### 1️⃣ Clone the Repository

git clone https://github.com/yourusername/password-strength-checker.git  
cd password-strength-checker  

### 2️⃣ Run the Script

python password_checker.py  

---

## 🧠 Detection Logic

The Password Strength Checker evaluates passwords using the following criteria:

| Rule | Requirement |
|------|-------------|
| Length | ≥ 8 characters |
| Uppercase | At least one A–Z |
| Lowercase | At least one a–z |
| Number | At least one digit (0–9) |
| Special Character | At least one symbol (!@#$%^&* etc.) |

### Strength Rating Logic

- 0–2 criteria met → Weak ❌  
- 3–4 criteria met → Moderate ⚠️  
- 5 criteria met → Very Strong 🔥  

---

## ⚙️ Configuration

You can modify password requirements directly inside `password_checker.py`:

- Change minimum length  
- Adjust required character sets  
- Modify strength scoring logic  

---

## 🛠️ Technologies Used

- Python 3  
- Standard Library (`re` – Regular Expressions)

---

## 📈 Future Improvements

Potential enhancements:

- Password generator feature  
- Graphical interface (Tkinter)  
- Web application version (Flask)  
- Integration with leaked password databases  
- Unit testing  
- Password entropy calculation  
- NIST-based validation rules  

---

## 🎯 Learning Objectives

This project demonstrates:

- Basic password policy enforcement  
- Regular expression usage  
- Conditional logic and scoring systems  
- Secure authentication fundamentals  
- Introductory cybersecurity scripting  

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repository and submit a pull request with improvements.

---

## 📜 License

This project is open-source and free to use for educational purposes.

---

## ⭐ Support

If you found this helpful, consider starring the repository to support the project!
