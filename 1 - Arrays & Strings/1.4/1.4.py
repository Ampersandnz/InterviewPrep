__author__ = 'Michael'

# Write a method to replace all spaces in a string with'%20'. You may assume that
# the string has sufficient space at the end of the string to hold the additional
# characters, and that you are given the "true" length of the string.

the_string = "i am a sentence with a bunch of spaces"


def main():
    print(urlify_whitespace(the_string))


def urlify_whitespace(to_change):
    temp = to_change.replace(" ", "%20")
    return temp


if __name__ == '__main__':
    main()