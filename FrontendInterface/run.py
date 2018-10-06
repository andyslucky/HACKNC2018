import langprocessor
import input_io

requested_input = input_io.create_instance()

langprocessor.process_sentence(requested_input["transcription"])