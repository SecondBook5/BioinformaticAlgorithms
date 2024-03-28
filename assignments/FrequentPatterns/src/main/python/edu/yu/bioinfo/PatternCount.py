# PatternCount.py

def PatternCount(Text, Pattern):
    """
    Counts the occurrences of a pattern in a given text.

    Args:
    - Text (str): The input text.
    - Pattern (str): The pattern to count.

    Returns:
    - int: The count of occurrences of the pattern in the text.

     Raises:
    - ValueError: If Text or Pattern is empty, or if Pattern is longer than Text.
    - TypeError: If Text or Pattern is not a string.
    """

   # Validate input strings
    if not isinstance(Text, str) or not isinstance(Pattern, str):
        raise TypeError("Text and Pattern must be strings")

    # Check if Text and Pattern are non-empty strings
    if not Text or not Pattern:
        raise ValueError("Text and Pattern cannot be empty")
    
    # Check if Pattern is not longer than Text
    if len(Pattern) > len(Text):
        raise ValueError("Pattern length cannot be greater than Text length")
    
    # Initialize the count of occurences
    count = 0

    try:
        # Iterate through each possible starting position of a substring of length Pattern in Text
        for i in range(len(Text) - len(Pattern) + 1):
            # Check if the substring from position i to i + len(Pattern) is equal to the given Pattern
            if Text[i:i+len(Pattern)] == Pattern:
                # If equal, increment the count
                count += 1
    except Exception as e:
        # Raise an exception with a descriptive error message
        raise ValueError(f"Error counting pattern occurrences: {e}")

    # Return the final count of occurrences
    return count

'''
This code defines a function PatternCount that counts the occurrences of a given pattern (Pattern) in a given text (Text). 
The function uses a sliding window approach to iterate through the text and check for matches with the pattern. 
If a match is found, the count is incremented. Any exceptions during the process are caught and an error message is printed. 
The final count is returned.
'''

