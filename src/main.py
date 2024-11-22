import threading
from web import WebUI
from circuit import Circuit
from tkui import TKUI

def main():
    terminate = threading.Event()

    ui = TKUI()

    circuit_thread = threading.Thread(target=Circuit.run)
    circuit_thread.start()

    web_ui_thread = threading.Thread(target=WebUI.run, args=(ui,))
    web_ui_thread.start()

    ui.run_ui()

if __name__ == '__main__':
    main()