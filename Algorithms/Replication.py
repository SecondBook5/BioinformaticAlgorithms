#Replication.py
from collections import Counter


def PatternCount(Text, Pattern):
    """
    Counts the occurrences of a given pattern in a text string.
    Args:
        Text (str): The text string to search for occurrences of the pattern.
        Pattern (str): The pattern string to search for in the text.
    Returns:
        int: The count of occurrences of the pattern in the text.
    """
    # Check for empty inputs
    if not Text:
        raise ValueError("Text must not be empty")
    if not Pattern:
        raise ValueError("Pattern must not be empty")
    # If the pattern is longer than the text, it cannot occur
    if len(Pattern) > len(Text):
        raise ValueError("Pattern length cannot be greater than Text length")
    # Initialize the count of occurrences to 0
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
    # Check for empty input or invalid value of k
    if not Text:
        raise ValueError("Text must not be empty")
    if k <= 0:
        raise ValueError("k must be a positive integer")
    # Use Counter to count occurrences of substrings of length 'k'
    substrings = [Text[i:i+k] for i in range(len(Text) - k + 1)]
    freq = Counter(substrings)
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
    # Check for empty input
    if not Text:
        return []
    # Generate frequency map of substrings of length 'k'
    # Convert text to lowercase for case-insensitive comparison
    freq = FrequencyMap(Text.lower(), k)
    # Find maximum frequency
    # Get the maximum frequency value, or 0 if the map is empty
    max_freq = max(freq.values(), default=0)
    # Use list comprehension to filter frequent words
    frequent_words = [key for key, value in freq.items() if value == max_freq]
    # Return the list of most frequent substrings
    return frequent_words
