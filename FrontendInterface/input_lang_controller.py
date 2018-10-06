import input_controller
import Langprocessor_controller

def commands(response):
    command = Langprocessor_controller.cmd_parser(response)
    print(command)