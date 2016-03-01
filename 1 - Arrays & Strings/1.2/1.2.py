__author__ = 'Michael'

# Implement a function void reverse(char* str) in C or C++ which reverses a null terminated string.
# NOTE: Too out of practice to want to do it in C/C++. May come back and do it again in the correct language later.

to_be_reversed = "I have been reversed!"


def main():
    # I'm aware that 'reversed(to_be_reversed)' would be easier but it's cheating.
    print(reverse(to_be_reversed))


def reverse(to_reverse):
    to_return = ''

    for char in to_reverse[::-1]:
        to_return += char

    return to_return


if __name__ == '__main__':
    main()