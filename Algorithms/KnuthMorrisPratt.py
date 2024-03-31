def compute_prefix(pattern):
    """
    Computes the prefix table for the Knuth-Morris-Pratt algorithm.
    
    The Knuth-Morris-Pratt algorithm (KMP) is an efficient pattern matching algorithm used to search for occurrences of a 
    pattern within a text. The prefix table, also known as the failure function or transition function, is a key component 
    of the KMP algorithm. It stores information about the longest proper prefix of a substring that is also a suffix of 
    the substring. This information is used to efficiently skip unnecessary comparisons during the pattern matching process.

    Args:
        pattern (list): The pattern to be analyzed (an array of characters).

    Returns:
        list: The prefix table to be filled (an array of integers).
    """
    if not pattern:
        raise ValueError("Pattern cannot be empty")

    # Initialize the table with -1
    prefix_table = [-1] * (len(pattern) + 1)
    position = 1  # The current position we are computing in the table
    candidate = 0  # The zero-based index in the pattern of the next character of the current candidate substring

    # Iterate to fill the prefix table
    while position < len(pattern):
        if pattern[position] == pattern[candidate]:
            # If characters match, copy value from the previous position
            prefix_table[position] = prefix_table[candidate]
        else:
            # If characters don't match, update table and backtrack
            prefix_table[position] = candidate
            candidate = prefix_table[candidate]
            while candidate >= 0 and pattern[position] != pattern[candidate]:
                candidate = prefix_table[candidate]
        position += 1
        candidate += 1

    # Only needed when all occurrences are searched
    prefix_table[position] = candidate

    return prefix_table


def kmp_pattern_search(text, pattern):
    """
    Searches for occurrences of a pattern in a text using the Knuth-Morris-Pratt algorithm.
    
    The Knuth-Morris-Pratt algorithm (KMP) is an efficient pattern matching algorithm used to search for occurrences of a 
    pattern within a text. It utilizes the prefix table generated from the pattern to efficiently skip unnecessary 
    comparisons during the search process. This improves the overall performance of the pattern matching operation.

    Args:
        text (list): The text to be searched (an array of characters).
        pattern (list): The pattern sought (an array of characters).

    Returns:
        tuple: A tuple containing an array of integers positions (positions in the text at which the pattern is found) and
               an integer count (number of occurrences).
    """
    if not text:
        raise ValueError("Text cannot be empty")
    if not pattern:
        raise ValueError("Pattern cannot be empty")
    if len(pattern) > len(text):
        return [], 0

    prefix_table = compute_prefix(pattern)  # Generate the prefix table

    text_index = 0  # Position of the current character in the text
    pattern_index = 0  # Position of the current character in the pattern
    count = 0  # Number of occurrences
    positions = []  # Positions in the text at which the pattern is found

    # Iterate over the text
    while text_index < len(text):
        if pattern[pattern_index] == text[text_index]:
            # Characters match, move to the next characters
            text_index += 1
            pattern_index += 1
            if pattern_index == len(pattern):
                # If the whole pattern is matched, add the position to the list
                positions.append(text_index - pattern_index)
                count += 1
                pattern_index = prefix_table[pattern_index]
        else:
            # Characters don't match, update position using the prefix table
            pattern_index = prefix_table[pattern_index]
            if pattern_index < 0:
                # If pattern index is negative, move to the next character in the text
                text_index += 1
                pattern_index += 1

    return positions, count
