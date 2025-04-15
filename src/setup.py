#!/usr/bin/python3
from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / "README.md").read_text(encoding="utf-8");

setup(
    name="clipboard_tts_client",
    version="0.1.0",
    description="Program that collects text from clipboard and converts it to speech using tts-program-server",
    author="Fernando Pujaico Rivera",
    author_email="fernando.pujaico.rivera@gmail.com",
    maintainer='Fernando Pujaico Rivera',
    maintainer_email='fernando.pujaico.rivera@gmail.com',
    url="https://github.com/trucomanx/ClipboardTTSClient",
    keywords="tts, server",  # Optional
    long_description=long_description,  # Optional
    long_description_content_type="text/markdown",  # Optional (see note above)
    packages=find_packages(),
    install_requires=[
        "PyQt5",
        'text-to-speech-program',
        'langdetect'
    ],
    entry_points={
        'console_scripts': [
            'clipboard-tts-indicator=clipboard_tts_client.indicator:main'
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    package_data={
        'clipboard_tts_client': ['icons/logo.png'],
    },
    include_package_data=True, 
    project_urls={  # Optional
        "Bug Reports": "https://github.com/trucomanx/ClipboardTTSClient/issues",
        "Funding": "https://trucomanx.github.io/en/funding.html",
        "Source": "https://github.com/trucomanx/ClipboardTTSClient/",
    },
)
