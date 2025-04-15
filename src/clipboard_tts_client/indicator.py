#!/usr/bin/python3
import sys
import os
import signal

from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QAction
from PyQt5.QtGui import QIcon

from clipboard_tts_client.lib_funcs import tts_remove_task, tts_play  # Removi o ponto antes do import

last_play_id = None

def play():
    global last_play_id
    app = QApplication.instance()
    if app is None:
        app = QApplication([])

    clipboard = app.clipboard()
    text = clipboard.text()
    last_play_id = tts_play(text)

def remove():
    global last_play_id
    msg = tts_remove_task(last_play_id)
    # print(msg)

def quit_app():
    QApplication.quit()

def main():
    app = QApplication(sys.argv)

    # Criar o ícone da bandeja
    tray_icon = QSystemTrayIcon()
    icon_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'icons', 'logo.png')
    tray_icon.setIcon(QIcon(icon_path))

    # Criar o menu da bandeja
    menu = QMenu()

    play_action = QAction("Play clipboard")
    play_action.triggered.connect(play)
    menu.addAction(play_action)

    remove_action = QAction("Remove last task")
    remove_action.triggered.connect(remove)
    menu.addAction(remove_action)

    quit_action = QAction("Exit")
    quit_action.triggered.connect(quit_app)
    menu.addAction(quit_action)

    tray_icon.setContextMenu(menu)
    tray_icon.show()

    # Capturar Ctrl+C no terminal
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

