# TODO: Implement the following functions based on the descriptions.

def reverse_list(lst):
    """
    Reverses the given list.
    :param lst: List of integers.
    :return: A list with elements in reverse order.
    """
    reverse_list = []
    list = [20, 40, 60, 80, 100]
    for n in range (len(lst) -1, -1, -1):
        reversed_list.append(lst[n])
        return reversed_list
    reversed_list = reverse_list(list)

    print(reversed_list)

def count_occurrences(lst, element):
    """
    Counts how many times the given element appears in the list.
    :param lst: List of elements.
    :param element: Element to count.
    :return: Integer count of occurrences.
    """
    list = [10, 20, 30, 40, 40, 20, 50]
    count = 0
    for item in lst:
        if item == element:
            count += 1
    return count

def get_keys_with_value(dct, value):
    """
    Returns a list of keys that have the given value in the dictionary.
    :param dct: Dictionary to search.
    :param value: Value to find.
    :return: List of keys.
    """
    keys = []


    return keys

def merge_sorted_lists(lst1, lst2):
    """
    Merges two sorted lists into one sorted list.
    :param lst1: First sorted list.
    :param lst2: Second sorted list.
    :return: Merged sorted list.
    """
    pass  # Implement this

def find_second_largest(numbers):
    """
    Finds the second largest number in a list.
    :param numbers: List of integers.
    :return: The second largest integer.
    """
    numbers = [2, 4, 6, 8, 10, 20]

    if len(numbers) <2:
        raise ValueError ("must have more than one number")
    for num in numbers[2:]:
        if num > largest:
            second_largest = largest
            largest = num

        elif num > second_largest and largest:
            second_largest = num
            return second_largest
        
    print(second_largest)


def is_anagram(str1, str2):
    """
    Checks if two strings are anagrams.
    
    An anagram is a word or phrase formed by rearranging the letters of another,
    using all the original letters exactly once. For example, "listen" and "silent"
    are anagrams because they use the same letters in a different order.
    
    :param str1: First string.
    :param str2: Second string.
    :return: True if the strings are anagrams, False otherwise.
    """
    str1 = "Listen"
    str2 = "Silent"

    if len(str1) != len(str2):
        return False
    
    char_count = {}
    for char in str1:
        char_count[char] = char_count.get(char, 0) + 1

    for char in str2:
        if char not in char_count:
            return False
        char_count[char] -= 1

    else:
        return True


    result = is_anagram(str1, str2)
    print(result)


def flatten_list(nested_list):
    """
    Flattens a nested list into a single list.
    :param nested_list: List of lists.
    :return: A flat list with all elements.
    """
    nested_list = [a, b, c [d, e, f], g, h, [i, j[k,l]]]
    flat_list = []
    for elements in nested_list:
        flat_list.extend(flatten_list(elements))
    else:
        flat_list.append(elements)
    return flat_list


def remove_duplicates(lst):
    """
    Removes duplicates from the list while maintaining order.
    :param lst: List of elements.
    :return: List without duplicates.
    """
    pass  # Implement this

def find_common_elements(lst1, lst2):
    """
    Finds common elements between two lists.
    :param lst1: First list.
    :param lst2: Second list.
    :return: List of common elements.
    """
    pass  # Implement this