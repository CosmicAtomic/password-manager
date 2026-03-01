# 🔐 Password Manager GUI

A lightweight, secure desktop application built with Python and Tkinter that generates strong passwords, saves them locally, and retrieves them on demand. 

## 🚀 Overview

Managing passwords across dozens of websites can be a hassle. This application solves that by providing a simple, user-friendly Graphical User Interface (GUI) to handle credential management. 

Instead of relying on third-party cloud services, this app stores your credentials locally and securely in a structured JSON format, ensuring you retain full control over your data.

## ✨ Key Features

* **Strong Password Generation:** Automatically generates highly secure passwords mixing letters, numbers, and symbols with a single click.
* **Auto-Clipboard:** Generated passwords are automatically copied to your clipboard (via `pyperclip`) for immediate pasting.
* **Data Serialization:** Saves and updates credentials cleanly using Python's `json` module.
* **Smart Search:** Easily retrieve forgotten passwords by searching for the website name.
* **Error Handling:** Built-in safeguards (via `messagebox`) prevent saving empty fields or searching for data that doesn't exist yet.

## 🛠️ Tech Stack

* **Language:** Python 3.x
* **GUI Framework:** Tkinter
* **Data Handling:** JSON (JavaScript Object Notation)
* **Libraries:** `pyperclip`, `random`, `json`

## 💻 Running the Application

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/yourusername/password-manager.git](https://github.com/yourusername/password-manager.git)
   cd password-manager
