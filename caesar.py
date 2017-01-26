from sys import argv, exit
from helpers import rotate_character, up_alpha, low_alpha

def encrypt(text, rot):
    is_text = ''
    for x in text:
        is_text = is_text + rotate_character(x, rot)
    return is_text

def user_input_is_valid(cl_args):
    if len(cl_args) == 2:
        if cl_args[1].isdigit():
            return True
        else:
            return False
    else:
        return False


def main():
    if user_input_is_valid(argv):
        text = "Type a message:"
        rot = int(argv[1])
        encrypt(text, rot)
    else:
        return False

if __name__ == '__main__':
    main()
