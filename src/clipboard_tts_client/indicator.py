#!/usr/bin/python3
import sys
import os
import signal

from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QAction
from PyQt5.QtGui import QIcon

from clipboard_tts_client.lib_funcs import tts_remove_task, tts_play  # Ajuste se estiver num pacote

class ClipboardTtsClientApp(QApplication):
    def __init__(self, sys_argv):
        super().__init__(sys_argv)
        self.last_play_id = None
        self.menu = None
        self.init_tray()

    def init_tray(self):
        # Ícone
        icon_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'icons', 'logo.png')
        self.tray_icon = QSystemTrayIcon(QIcon(icon_path), self)

        # Menu
        self.menu = QMenu()

        self.play_action = QAction("Play clipboard")
        self.play_action.triggered.connect(self.play_clipboard)
        self.menu.addAction(self.play_action)

        self.remove_action = QAction("Remove last task")
        self.remove_action.triggered.connect(self.remove_last_task)
        self.menu.addAction(self.remove_action)

        self.quit_action = QAction("Exit")
        self.quit_action.triggered.connect(self.quit)
        self.menu.addAction(self.quit_action)

        self.tray_icon.setContextMenu(self.menu)
        self.tray_icon.show()

    def play_clipboard(self):
        clipboard = self.clipboard()
        text = clipboard.text()
        self.last_play_id = tts_play(text)

    def remove_last_task(self):
        if self.last_play_id is not None:
            tts_remove_task(self.last_play_id)

    def quit(self):
        self.exit()

def main():
    # Captura de sinal Ctrl+C no terminal
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    app = ClipboardTtsClientApp(sys.argv)
    app.setApplicationName("clipboard_tts_client") # xprop WM_CLASS # *.desktop -> StartupWMClass  
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

