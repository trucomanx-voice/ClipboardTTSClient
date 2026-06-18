# clipboard-tts-indicator

This package provides a text-to-speech client program to interact with the server `text-to-speech-program`.

![logo](https://raw.githubusercontent.com/trucomanx-voice/ClipboardTTSClient/main/screenshot.png)

> [!WARNING]
> Tested only on Python 3.10–3.12. Newer versions may break due to audio dependencies (pydub / audioop stack).

## 1. Installing

To install the package from [PyPI](https://pypi.org/project/clipboard_tts_client/), follow the instructions below:

### With pip

```bash
pip install --upgrade clipboard_tts_client
```

Execute `which clipboard-tts-indicator` to see where it was installed, probably in `/home/USERNAME/.local/bin/clipboard-tts-indicator`.

### With pipx (recommended for desktop applications)

```bash
pipx install clipboard_tts_client
```

> [!IMPORTANT]
> To install with python 3.12 use: `pipx install --python /path/to/venvs/python3.12/bin/python3.12 clipboard_tts_client`

If you need to upgrade later: `pipx upgrade clipboard_tts_client`

### Installing and adding the program to the Linux startup session

Installing and adding a bar indicator to Linux startup session (`~/.config/autostart/clipboard-tts-indicator.desktop`)

```bash
pip install --upgrade clipboard_tts_client
clipboard_tts_client --autostart
```

### Using

To start, use the command below:

```bash
clipboard-tts-indicator
```

## 2. More information

If you want more information go to [doc](https://github.com/trucomanx-voice/ClipboardTTSClient/blob/main/doc) directory

## 3. Buy me a coffee

If you find this tool useful and would like to support its development, you can buy me a coffee!  
Your donations help keep the project running and improve future updates.  

[☕ Buy me a coffee](https://ko-fi.com/trucomanx) 

## 4. License

This project is licensed under the GPL license. See the `LICENSE` file for more details.
