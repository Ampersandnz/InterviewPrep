__author__ = 'Michael'

# Given two strings, write a method to decide if one is a permutation of the other.

string_1 = "This is a sentence"
string_2 = "snT ecsia h itesne"
string_3 = "A completely different sentence"
string_4 = "Same length but still wrong...."


def main():
    print(is_anagram(string_1, string_2))
    print(is_anagram(string_2, string_3))
    print(is_anagram(string_3, string_4))


def is_anagram(s_1, s_2):
    if len(s_1) != len(s_2):
        return False

    hashmap = {}

    for char in s_1:
        if char in hashmap:
            hashmap[char] += 1
        else:
            hashmap[char] = 1

    # Could throw a check for hashmap[char] = 0 in here but it's more readable to iterate over it again.
    for char in s_2:
        if char in hashmap:
            hashmap[char] -= 1
        else:
            return False

    for value in hashmap.values():
        if value != 0:
            return False

    return True


if __name__ == '__main__':
    main()