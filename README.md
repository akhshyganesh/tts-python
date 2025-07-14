# Text-to-Speech Python Script

This project provides a simple Python interface for converting text to speech using the [Coqui TTS](https://github.com/coqui-ai/TTS) library. It supports direct audio playback without saving to disk, making it fast and efficient for desktop use.

## Features
- Text-to-speech conversion using neural models
- Direct audio playback (no intermediate file required)
- Easy to use and extend

## Requirements

### Python Version
- Python 3.8 or higher
- Python 3.10 or lower

### Python Libraries
- TTS (Coqui TTS)
- sounddevice
- os (standard library)

### System-level Dependencies
- On macOS: [PortAudio](http://www.portaudio.com/) (required for `sounddevice`)
  - Install via Homebrew:
    ```sh
    brew install portaudio
    ```
- On Linux: PortAudio (install via your package manager)
- On Windows: No extra system library required for basic usage

## Installation

1. Clone this repository:
    ```sh
    git clone <repo-url>
    cd text-to-speech
    ```
2. Install Python dependencies:
    ```sh
    pip install -r requirements.txt
    ```
3. (macOS/Linux only) Install PortAudio:
    ```sh
    # macOS
    brew install portaudio
    # Linux (Debian/Ubuntu)
    sudo apt-get install portaudio19-dev
    ```

## Usage

Run the script:
```sh
python main.py
```

Edit `main.py` to change the text or model as needed.

## License
MIT
