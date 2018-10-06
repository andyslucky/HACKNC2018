import sys
sys.path.append('..')
print(sys.path)
import langprocessor
<<<<<<< HEAD
import Server
import userinterface
=======

>>>>>>> 3707a5375a1ca0d9513f1d115f3eb9e5706475f6
import input_io


userinterface.make_ui()
requested_input = input_io.create_instance()

commands = langprocessor.process_sentence(requested_input["transcription"])


if commands.get("error") is not None:
    print("command has error message: " + commands.get("error"))


