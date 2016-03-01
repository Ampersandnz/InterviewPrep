__author__ = 'Michael'

# Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?

not_unique = "i am not a unique string"
unique = "but_i.am "


def main():
    print(is_unique(unique))
    print(is_unique(not_unique))

    print(is_unique_no_structs(unique))
    print(is_unique_no_structs(not_unique))


def is_unique(to_check):
    hashmap = {}

    for char in to_check:
        if char in hashmap:
            return False
        hashmap[char] = char
    return True


def is_unique_no_structs(to_check):
    for char in to_check:
        if to_check.count(char) > 1:
            return False
    return True

if __name__ == '__main__':
    main()