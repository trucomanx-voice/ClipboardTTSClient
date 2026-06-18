# clipboard-tts-indicator

This package provides a text-to-speech client program to interact with the server `text-to-speech-program`.

> [!WARNING]
> Tested only on Python 3.10–3.12. Newer versions may break due to audio dependencies (pydub / audioop stack).

## Install from PYPI

The homepage in pipy is https://pypi.org/project/clipboard_tts_client/

```bash
pip install --upgrade clipboard_tts_client
```
or (recommended for desktop applications)

```bash
pipx install clipboard_tts_client
```

> [!IMPORTANT]
> To install with python 3.12 use: `pipx install --python /path/to/venvs/python3.12/bin/python3.12 clipboard_tts_client`

Using:

```bash
clipboard-tts-indicator
```

## Install from source
Installing `clipboard-tts-indicator` program

```bash
git clone https://github.com/trucomanx-voice/ClipboardTTSClient.git
cd ClipboardTTSClient
pip install -r requirements.txt
cd src
python -m build
pip install dist/clipboard_tts_client-*.tar.gz
```
Using:

```bash
clipboard-tts-indicator
```

## Uninstall

```bash
pip uninstall clipboard_tts_client
```
