import pyaudio
import subprocess

INPUT_SAMPLE_RATE = 24000  # Input sample rate
INPUT_CHUNK_SIZE = 2048  # Input chunk size
OUTPUT_SAMPLE_RATE = 24000  # Output sample rate. ** Note: This must be 24000 **
OUTPUT_CHUNK_SIZE = 4096  # Output chunk size
STREAM_FORMAT = pyaudio.paInt16  # Stream format
INPUT_CHANNELS = 1  # Input channels
OUTPUT_CHANNELS = 1  # Output channels
OUTPUT_SAMPLE_WIDTH = 2  # Output sample width

INSTRUCTIONS = """You are a pirate bartender.  Always talk like a pirate.  Get to know your customers, buy them a drink.


 You are able to make a variety of drinks, but prefer pirate themed drinks. Feel free to make up drink names.  You should never attempt make a drink until you know what your bar patron wants to drink. 


"""
VOICE_TYPE = "alloy"  # alloy, echo, shimmer
TEMPERATURE = 0.7
MAX_RESPONSE_OUTPUT_TOKENS = 4096

TOOLS = [
    {
        "type": "function",
        "name": "make_a_drink",
        "description": "Make a drink for your conversation partner.  Make sure they have confirmed what they want before using this tool",
        "parameters": {
            "type": "object",
            "properties": {
                "drink_type": {
                    "type": "string",
                    "description": "What type of drink do you want to make?  You can choose from water, vodka or a pina colada",
                },
            },
            "required": ["drink_type"],
        },
    }
]
TOOL_CHOICE = "auto"

def make_a_drink(drink_type: str):
   print("\n" * 5)
   print(f"moving the arm to make a {drink_type}")
   print("\n" * 5)
   return "ok"




TOOL_FUNCTION_LIST = [
    make_a_drink
]
TOOL_MAP = {
    tool_info["name"]: tool_func
    for tool_info, tool_func in zip(TOOLS, TOOL_FUNCTION_LIST)
}
