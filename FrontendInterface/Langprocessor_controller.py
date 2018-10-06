import Langprocessor
cmd_terms = ["state", "searchterms", "error", "subject"]

def cmd_parser(cmd_dict):
    # Error message if dictionary doesn't follow expected format.
    if not cmd_terms in cmd_dict:
        print("Error. Doesn't follow expected format.")

    if cmd_dict.get("state"):
        print("turn on")
        return 1
    else:
        print("turn off")
        return 0

