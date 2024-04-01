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
        # Check if the substring from position i to i + len(Pattern) (converted to lowercase) is equal to the given Pattern (converted to lowercase)
        if Text[i:i+len(Pattern)].lower() == Pattern.lower():
            # If equal, increment the count
            count += 1
    # Return the final count of occurrences
    return count
