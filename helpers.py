up_alpha = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
low_alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def alphabet_position(letter):
    # check to see if letter is in alphabet
    if letter.isalpha():
        # check if letter is upper or lower case
        if letter in up_alpha:
            return up_alpha.index(letter)
        else:
            return low_alpha.index(letter)
    else:
        return letter

def rotate_character(char, rot):
    # check to see if letter is in alphabet
    if char.isalpha():
        # find position of char and rotate
        og_let = alphabet_position(char)
        new_let = rot + og_let
        new_let = new_let % 26
        # check if char is upper or lower case
        if char in up_alpha:
            return up_alpha[new_let]
        else:
            return low_alpha[new_let]
    else:
        return char
