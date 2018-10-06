import sys
sys.path.append('..')
print(sys.path)
import langprocessor

import input_io


requested_input = input_io.create_instance()

commands = langprocessor.process_sentence(requested_input["transcription"])


if commands.get("error") is not None:
    print("command has error message: " + commands.get("error"))


