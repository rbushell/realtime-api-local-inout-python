# README

From Rick:

virtualenv venv

venv/bin/activate

pip install -r requirements.txt

cp .env.template .env 
vi .env    # Put your openai key in here.  You can ignore the AZURE stuff

python3 voice_chat.py openai

Use headphones; it needs echo cancelation of some sort to use speakers

config.py defines the prompt and a tool `make_me_a_drink`.  Update that method to move the arm around.  





---

## Overview
This code has been modified to enable conversations with a real-time API using your local microphone and speakers, based on [Azure-Samples/aoai-realtime-audio-sdk](https://github.com/Azure-Samples/aoai-realtime-audio-sdk/tree/main/python).  
`voice_chat.py` is created based on [aoai-realtime-audio-sdk/python/samples/low_level_sample.py](https://github.com/Azure-Samples/aoai-realtime-audio-sdk/blob/main/python/samples/low_level_sample.py).  
You can find a detailed explanation of `low_level_sample.py` [here](https://m-sea-bass.blogspot.com/2024/10/welcome-file.html).

Please make sure to read the Code of Conduct and license for [aoai-realtime-audio-sdk](https://github.com/Azure-Samples/aoai-realtime-audio-sdk) before using this code.

## Usage
### Installing Dependencies
Install the necessary dependencies with the following command:
```bash
pip install -r requirements.txt
```

### Setting Environment Variables
Copy `.env.template` to create a `.env` file, and configure the environment variables.

### Setting Constants
The constants defined in `voice_chat.py` configure the sample rate and chunk size for the microphone and speakers.  
Adjust these settings according to your environment if needed:
```python
INPUT_SAMPLE_RATE = 16000  # Input sample rate
INPUT_CHUNK_SIZE = 512  # Input chunk size
OUTPUT_SAMPLE_RATE = 24000  # Output sample rate **Must be set to 24000**
OUTPUT_CHUNK_SIZE = 1024  # Output chunk size
STREAM_FORMAT = pyaudio.paInt16  # Stream format
INPUT_CHANNELS = 1  # Input channels
OUTPUT_CHANNELS = 1  # Output channels
```

### Running the Script
Run the script using the following commands.  
Specify `azure` to use Azure OpenAI, or `openai` to use OpenAI:
```bash
python voice_chat.py azure
# Or 
python voice_chat.py openai
```

The logs are stored in the 'log' directory. The logs contain timestamps for Client Events and Server Events.

## Dialogue
In addition to voice dialogue, `dialogue.py` implements the following features:

- Function execution
- Conversation termination (session reset)

This allows for more versatile conversations, and at the same time, when a conversation ends, it enables the session to restart, which is expected to reduce token costs.

```bash
python dialogue.py azure
# Or 
python dialogue.py openai
```

## Reference Links
- [Azure-Samples/aoai-realtime-audio-sdk](https://github.com/Azure-Samples/aoai-realtime-audio-sdk/tree/main/python)
