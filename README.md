# Password Strenth Checker Project 1
## Project Title
Password Strength Checker

## Description
The Password Strength Checker is a Python program that checks how strong a password is based on common password security rules.  

The program analyzes the password and checks if it:
- Has at least 8 characters
- Contains an uppercase letter
- Contains a number
- Contains a special symbol

After the checks, the program displays:
- PASS or FAIL for each requirement
- A score out of 4
- The overall password strength rating

This project is useful for beginners learning Python and basic cybersecurity concepts.

---

## How It Runs

1. The user runs the Python file.
2. The program asks the user to enter a password.
3. The password is checked character by character.
4. The program evaluates the password using different security conditions.
5. A final strength score and rating are displayed.

---

## How to Run the Project

### Step 1: Install Python
Make sure Python 3 is installed on your computer.

### Step 2: Save the File
Save the program as:

```bash
password_checker.py
```

### Step 3: Run the Program
Open the terminal or command prompt and run:

```bash
python password_checker.py
```

---

## Example Output

```text
Enter a password: MyPassword123!

--- Password Strength Checker ---
Length (8+):          PASS
Contains Uppercase:   PASS
Contains Digit:       PASS
Contains Symbol:      PASS

Your Score: 4 out of 4
Password Strength: STRONG
---------------------------------------
```

---

## Language Used
- Python 3

---


# Basic Encryption & Decryption Project 2

## Project Title
Basic Encryption & Decryption Using Caesar Cipher

---

## 📖 Description
This project is a beginner-friendly cybersecurity program developed in Python that demonstrates how encryption and decryption work using the Caesar Cipher technique.

The program accepts a message from the user, encrypts the text by shifting letters forward in the alphabet, and then decrypts it back to the original message.

This project helps beginners understand:
- Encryption concepts
- Decryption logic
- Data confidentiality
- Python programming fundamentals
- Basic cybersecurity principles

---

## Features
- Encrypts user text
- Decrypts encrypted text
- Uses Caesar Cipher logic
- Handles uppercase and lowercase letters
- Keeps spaces and symbols unchanged
- Simple and beginner-friendly

---

## Technologies Used
- Python 3

---

##  How the Program Works

### Encryption
The program:
1. Takes input from the user
2. Converts letters into numerical values
3. Shifts each letter forward by a specific value
4. Converts the values back into letters
5. Displays the encrypted text

### Decryption
The program:
1. Reads the encrypted text
2. Shifts each letter backward using the same shift value
3. Restores the original message

---

##  How to Run the Project

### Step 1: Install Python
Download and install Python from the official website:

https://www.python.org

---

### Step 2: Save the File
Save the code in a file named:

```bash
encryption.py
```

---

### Step 3: Open Terminal or Command Prompt
Navigate to the folder containing the file.

Example:

```bash
cd Desktop
```

---

### Step 4: Run the Program

```bash
python encryption.py
```

or

```bash
python3 encryption.py
```

---

## 💻 Example Output

=== Basic Encryption & Decryption ===

Enter your message: hello

Encrypted Text: khoor
Decrypted Text: hello

---

##  Learning Outcomes
By completing this project, you will learn:
- Basic encryption and decryption techniques
- Caesar Cipher implementation
- Python loops and conditions
- String manipulation
- ASCII conversion using `ord()` and `chr()`
- Fundamentals of cybersecurity

---

##  Conclusion
This project serves as a simple introduction to cybersecurity and cryptography. It demonstrates how information can be protected using basic encryption techniques and provides a strong foundation for more advanced cybersecurity concepts in the future

## Phishing Awareness Analysis System Project 3
# Project Title
Phishing Awareness Analysis System

## Project Overview
The Phishing Awareness Analysis System is a Python-based cybersecurity project designed to detect and analyze phishing messages. The program examines suspicious emails and SMS messages to identify common phishing indicators such as suspicious links, urgent language, fake domains, and untrusted sender addresses.

This project helps users understand how phishing attacks work and how to recognize dangerous messages before becoming victims of cybercrime.

---

# Objectives
The main objectives of this project are:

- Detect phishing attempts in emails and messages
- Identify suspicious keywords and unsafe links
- Analyze phishing indicators and red flags
- Improve cybersecurity awareness
- Demonstrate basic threat analysis using Python

---

# Features

## The system can:
- Analyze multiple phishing messages
- Detect suspicious keywords
- Identify unsafe HTTP links
- Detect suspicious domains
- Detect fake sender email addresses
- Display phishing analysis results
- Show warning messages for unsafe content

---

# Technologies Used

- Python 3
- String Handling
- Conditional Statements
- Loops
- Functions
---

# How the Program Works

1. The program stores sample phishing messages.
2. It scans each message for suspicious keywords.
3. It checks for suspicious domains and unsafe links.
4. It identifies phishing red flags.
5. The final result is displayed to the user.

---

# Installation and Usage

## Step 1: Install Python
Download and install Python from:
https://www.python.org/

---

## Step 2: Run the Program

Open terminal or command prompt and run:

```bash
python phishing_analysis.py
```

---

# Skills Demonstrated

This project demonstrates:

- Cybersecurity awareness
- Threat analysis
- Phishing detection
- Python programming
- Problem-solving skills
- Security thinking

---

# Future Improvements

Possible future upgrades include:

- GUI interface using Tkinter
- Real-time email scanning
- Machine learning phishing detection
- URL reputation checking
- Database logging system
- AI-powered threat detection

---

# Conclusion

Phishing attacks are one of the most common cyber threats today. This project demonstrates how Python can be used to analyze suspicious messages and identify phishing attempts through simple threat detection techniques.

By understanding phishing indicators and practicing safe browsing habits, users can better protect themselves from cyber attacks and online scams.

---

# Author

Jeffery Donkoh Ata
Computer Science (Cyber Security) Student
