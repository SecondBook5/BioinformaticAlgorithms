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
        
    Raises:
        ValueError: If Text or Pattern is empty, or if Pattern length exceeds Text length.
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
    Generates a frequency map of substrings of length 'k' in the given text using a sliding window approach.

    Args:
        Text (str): The text to analyze.
        k (int): The length of substrings.

    Returns:
        dict: A dictionary where keys are substrings of length 'k' and values are their frequencies.
        
    Raises:
        ValueError: If Text is empty or k is non-positive.
    """
    # Check for empty input or invalid value of k
    if not Text:
        raise ValueError("Text must not be empty")
    if k <= 0:
        raise ValueError("k must be a positive integer")

    freq = {}  # Initialize frequency map
    # Initialize the sliding window with the first k characters
    window = Text[:k]
    freq[window] = 1  # Initialize frequency count for the initial window

    # Iterate through the text, updating the sliding window and frequency map
    for i in range(k, len(Text)):
        # Update the sliding window by removing the first character and adding the next character
        window = window[1:] + Text[i]
        # Update the frequency count for the current window
        freq[window] = freq.get(window, 0) + 1

    return freq  # Return the frequency map



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


def ReverseComplement(Pattern):
    """
    Finds the reverse complement of a DNA sequence pattern.

    Args:
        Pattern (str): The DNA sequence pattern.

    Returns:
        str: The reverse complement of the input pattern.

    Raises:
        ValueError: If the input pattern contains invalid nucleotides or is empty.
    """
    # Set of valid nucleotides
    valid_nucleotides = {'A', 'T', 'C', 'G', 'N'}

    # Create a dictionary to store the complement of each nucleotide
    complement_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C', 'N': 'N'}

    # Check if the input pattern is empty
    if not Pattern:
        raise ValueError("Input pattern cannot be empty")

    # Initialize a list to store the reverse complement
    reverse_complement = []

    # Iterate through the input pattern in reverse order
    for base in reversed(Pattern.upper()):
        # Check if the current nucleotide is valid
        if base not in valid_nucleotides:
            raise ValueError("Invalid nucleotide in the input pattern")

        # Find the complement of each nucleotide and append it to the reverse complement list
        reverse_complement.append(complement_dict[base])

    # Join the reverse complement list and return the result
    return ''.join(reverse_complement)
