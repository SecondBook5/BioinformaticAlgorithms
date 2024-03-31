#Replication.py


def PatternCount(Text, Pattern):
    """
    Counts the occurrences of a given pattern in a text string.
    Args:
        Text (str): The text string to search for occurrences of the pattern.
        Pattern (str): The pattern string to search for in the text.
    Returns:
        int: The count of occurrences of the pattern in the text.
    """
    # Initialize the count of occurences to 0
    count = 0
    # Iterate through each possible starting position of a substring of length Pattern in Text
    for i in range(len(Text) - len(Pattern) + 1):
        # Check if the substring from position i to i + len(Pattern) is equal to the given Pattern
        if Text[i:i+len(Pattern)] == Pattern:
            # If equal, increment the count
            count += 1
    # Return the final count of occurrences
    return count


def FrequencyMap(Text, k):
    """
    Generates a frequency map of substrings of length 'k' in the given text.
    Args:
        Text (str): The text to analyze.
        k (int): The length of substrings.
    Returns:
        dict: A dictionary where keys are substrings of length 'k' and values are their frequencies.
    """
    # Initialize an empty dictionary to store frequencies of substrings
    freq = {}
    # Get the length of the text
    n = len(Text)
    # Loop through each possible substring of length 'k' in the text
    for i in range(n - k + 1):
        # Extract the substring of length 'k' starting at index 'i'
        Pattern = Text[i:i + k]
        # Check if the substring is already in the frequency map
        if Pattern in freq:
            # If yes, increment its frequency
            freq[Pattern] += 1
        else:
            # If not, add it to the frequency map with frequency 1
            freq[Pattern] = 1
    # Return the frequency map
    return freq


def FrequentWords(Text, k):
    """
    Finds the most frequent substrings of length 'k' in the given text.
    
    Args:
        Text (str): The text to analyze.
        k (int): The length of substrings.
        
    Returns:
        list: A list of the most frequent substrings of length 'k'.
    """

    # Generate frequency map of substrings of length 'k'
    freq = FrequencyMap(Text, k)

    # Initialize variables to store maximum frequency and corresponding words
    max_freq = 0
    frequent_words = []

    # Iterate through the frequency map to find maximum frequency and corresponding words
    for key, value in freq.items():
        # If current frequency is greater than current maximum frequency
        if value > max_freq:
            max_freq = value  # Update maximum frequency
            frequent_words = [key]  # Start a new list with the current key
        # If current frequency is equal to current maximum frequency
        elif value == max_freq:
            # Add the current key to the list of frequent words
            frequent_words.append(key)

    # Return the list of most frequent substrings
    return frequent_words
