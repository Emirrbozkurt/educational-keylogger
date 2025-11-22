# Educational Keylogger (Python)

A basic keystroke logging application developed using Python and the `pynput` library. 

This project was created to demonstrate **system programming concepts**, specifically analyzing how keyboard events are intercepted using **hooking mechanisms**, managing **background threads**, and handling **file I/O operations** safely.

> ⚠️ **LEGAL DISCLAIMER**
>
> This software is developed for **educational and academic research purposes only**.
> Using this tool on any system without the explicit permission of the system owner is **illegal** and may constitute a violation of privacy laws.
>
> The developer assumes **no liability** and is not responsible for any misuse or damage caused by this program.

## 🚀 Features

* **Real-time Event Listening:** Intercepts keyboard inputs using the `pynput` library.
* **Local Logging:** securely saves keystrokes to a local `key_log.txt` file with timestamps.
* **Special Key Handling:** Differentiates between standard characters and special keys (e.g., `Space`, `Enter`, `Shift`).
* **Graceful Exit:** Uses a specific trigger (`ESC` key) to stop the listener thread and close the file resources properly.

## 🛠️ Installation & Usage

### Prerequisites
* Python 3.x
* `pip` package manager

### 1. Clone the Repository
```bash
git clone [https://github.com/Emirrbozkurt/educational-keylogger.git]
cd educational-keylogger

2. Install Dependencies
Bash

pip install -r requirements.txt
3. Run the Application
Bash

python main.py
📝 Note for macOS Users: Since you are interacting with input devices, macOS requires explicit permission. If the script does not log anything or throws an error:

Go to System Settings > Privacy & Security > Input Monitoring.

Enable the switch for your Terminal application (or VS Code).

Restart the terminal and run the script again.

4. Stop the Session
Press the ESC key to stop the logging process safely.

📂 Project Structure
Plaintext

├── main.py             # The main script containing the hooking logic
├── requirements.txt    # List of dependencies (pynput)
├── key_log.txt         # Output file (Generated automatically, ignored in git)
├── .gitignore          # Git ignore file to protect logs
└── README.md           # Project documentation
🧠 Technical Concepts Covered
Python Threading: Managing non-blocking listeners in the background.

Input Hooking: Interfacing with OS-level input streams.

File Handling: Appending data streams to text files efficiently.

Developed by Emir Bozkurt | Computer Engineering Student
