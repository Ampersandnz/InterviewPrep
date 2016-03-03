__author__ = 'Michael'

# Implement a method to perform basic string compression using the counts of repeated characters.
# For example, the string aabcccccaaa would become a2blc5a3.
# If the "compressed" string would not become smaller than the original string,
# your method should return the original string.

string_1 = "aaaaabbbcdddda"
string_2 = "abccbc"


def main():
    print(compress(string_1))
    print(compress(string_2))


def compress(long_string):
    temp = []
    for char in long_string:
        if len(temp) > 0 and temp[len(temp) - 2] == char:
            temp[len(temp) - 1] += 1
        else:
            temp.append(char)
            temp.append(1)

    if len(temp) < len(long_string):
        return "" . join(str(e) for e in temp)
    else:
        return long_string


if __name__ == '__main__':
    main()