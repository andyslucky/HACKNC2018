import langprocessor
from ..PiProject.Server import Server

#import input_io

#requested_input = input_io.create_instance()

#langprocessor.process_sentence(requested_input["transcription"])

cmds = langprocessor.process_sentence("turn on off on off lights")

if cmds.get("error") is not None:
    print("command has error message: " + cmds.get("error"))


