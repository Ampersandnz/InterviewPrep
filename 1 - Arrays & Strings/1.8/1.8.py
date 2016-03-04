__author__ = 'Michael'

# Assume you have a method isSubstring which checks if one word is a substring of another.
# Given two strings, si and s2, write code to check if s2 is a rotation of si using only one call to isSubstring
# (e.g.,"waterbottle"is a rotation of "erbottlewat")

string_1 = "waterbottle"
string_2 = "erbottlewat"
string_3 = "asdfdgdfg"


def main():
    print(is_rotation(string_1, string_2))
    print(is_rotation(string_2, string_3))


def is_rotation(a, b):
    temp = a + a
    return temp.find(b) != -1

if __name__ == '__main__':
    main()