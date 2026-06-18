#!/usr/bin/python3
import sys
import os
import signal
import subprocess

from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QAction
from PyQt5.QtGui import QIcon, QDesktopServices
from PyQt5.QtCore import QUrl

from clipboard_tts_client.lib_funcs import tts_remove_task, tts_play  # Ajuste se estiver num pacote
import clipboard_tts_client.about as about

from clipboard_tts_client.desktop import create_desktop_file, create_desktop_directory, create_desktop_menu
from clipboard_tts_client.modules.wabout    import show_about_window
from clipboard_tts_client.modules.resources import resource_path

class ClipboardTtsClientApp(QApplication):
    def __init__(self, sys_argv):
        super().__init__(sys_argv)
        
        self.setQuitOnLastWindowClosed(False)
        
        self.last_play_id = None
        self.menu = None
        self.icon_path = None
        self.init_tray()

    def init_tray(self):
        # Ícone
        self.icon_path = resource_path('icons', 'logo.png')
        self.tray_icon = QSystemTrayIcon(QIcon(self.icon_path), self)
        self.setWindowIcon(QIcon(self.icon_path)) 
        
        # Menu
        self.menu = QMenu()

        self.play_action = QAction("Play clipboard")
        self.play_action.setIcon(QIcon(resource_path('icons', 'play-button.png')))
        self.play_action.triggered.connect(self.play_clipboard)
        self.menu.addAction(self.play_action)

        self.remove_action = QAction("Remove last task")
        self.remove_action.setIcon(QIcon(resource_path('icons', 'dialog-error.png')))
        self.remove_action.triggered.connect(self.remove_last_task)
        self.menu.addAction(self.remove_action)

        self.menu.addSeparator()

        # restart server linux
        self.restart_linux_action = QAction("Restart server in linux", self.menu)
        self.restart_linux_action.setIcon(QIcon(resource_path('icons', 'arrow-cw.png')))
        self.restart_linux_action.triggered.connect(self.restart_linux_service)
        self.menu.addAction(self.restart_linux_action)        
        
        # Coffee
        self.coffee_action = QAction("☕ Buy me a coffee", self.menu)
        self.coffee_action.setIcon(QIcon(resource_path('icons', 'emote-love.png')))
        self.coffee_action.triggered.connect(self.open_coffee_link)
        self.menu.addAction(self.coffee_action)
        
        # About
        self.about_action = QAction("🌟 About", self.menu)
        self.about_action.setIcon(QIcon(resource_path('icons', 'status_help.png')))
        self.about_action.triggered.connect(self.show_about)
        self.menu.addAction(self.about_action)
                
        
        self.menu.addSeparator()

        self.quit_action = QAction("❌ Exit")
        self.quit_action.setIcon(QIcon(resource_path('icons', 'application-exit.png')))
        self.quit_action.triggered.connect(self.quit)
        self.menu.addAction(self.quit_action)

        self.tray_icon.setContextMenu(self.menu)
        self.tray_icon.show()



    def restart_linux_service(self):
        subprocess.run([
            "pkexec", "systemctl", "restart", "tts-program-server"
        ])

    def open_coffee_link(self):
        QDesktopServices.openUrl(QUrl("https://ko-fi.com/trucomanx"))

    def show_about(self):
        data = {
            "version": about.__version__,
            "package": about.__package__,
            "program_name": about.__program_name__,
            "author": about.__author__,
            "email": about.__email__,
            "description": about.__description__,
            "url_source": about.__url_source__,
            "url_doc": about.__url_doc__,
            "url_funding": about.__url_funding__,
            "url_bugs": about.__url_bugs__
        }
        
        show_about_window(data, self.icon_path)
        
        
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
    
    create_desktop_directory()    
    create_desktop_menu()
    create_desktop_file(os.path.join("~",".local","share","applications"))
    
    for n in range(len(sys.argv)):
        if sys.argv[n] == "--autostart":
            create_desktop_directory(overwrite = True)
            create_desktop_menu(overwrite = True)
            create_desktop_file(os.path.join("~",".config","autostart"), overwrite=True)
            return
        if sys.argv[n] == "--applications":
            create_desktop_directory(overwrite = True)
            create_desktop_menu(overwrite = True)
            create_desktop_file(os.path.join("~",".local","share","applications"), overwrite=True)
            return

    app = ClipboardTtsClientApp(sys.argv)
    app.setApplicationName(about.__package__) # xprop WM_CLASS # *.desktop -> StartupWMClass  
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

