import sys
sys.path.insert(0,'../PiProject/')
print(sys.path)
import langprocessor
import Server

import input_io


requested_input = input_io.create_instance()

commands = langprocessor.process_sentence(requested_input["transcription"])

if commands.get("error") is not None:
    print("command has error message: " + commands.get("error"))


