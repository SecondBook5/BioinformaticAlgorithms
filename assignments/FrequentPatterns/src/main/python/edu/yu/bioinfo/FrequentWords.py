# FrequentWords.py
from PatternCount import PatternCount


def FrequentWords(Text, k):
    """
    Finds the most frequent k-mers in a given text.

    Args:
    - Text (str): The input text.
    - k (int): The length of k-mers.

    Returns:
    - list: List of most frequent k-mers.
    """
    # Initialize an empty set to store most frequent k-mers
    FrequentPatterns = set()

    # Initialize an array to store counts for each k-mer in the text
    count = [0] * (len(Text) - k + 1)

    try:
        # Iterate through each possible starting position of a k-mer in the text
        for i in range(len(Text) - k + 1):
            pattern = Text[i:i+k]
            # Count the occurrences of the current k-mer using PatternCount function
            count[i] = PatternCount(Text, pattern)

        # Find the maximum count in the count array
        maxCount = max(count)

        # Iterate through each k-mer again and add it to the set if its count is equal to maxCount
        for i in range(len(Text) - k + 1):
            if count[i] == maxCount:
                FrequentPatterns.add(Text[i:i+k])

    except Exception as e:
        # Handle any exceptions and print an error message
        print(f"Error in FrequentWords: {e}")

    # Convert the set to a list and return the result
    return list(FrequentPatterns)


def FrequencyTable(Text, k):
    """
    Builds a frequency table for k-mers in a given text.

    Args:
    - Text (str): The input text.
    - k (int): The length of k-mers.

    Returns:
    - dict: A frequency table (dictionary) of k-mers.
    """
    # Initialize an empty dictionary to store frequencies of k-mers
    freqMap = {}
    n = len(Text)

    try:
        # Iterate through each possible starting position of a k-mer in the text
        for i in range(n - k + 1):
            # Extract the current k-mer
            Pattern = Text[i:i+k]
            # Update the frequency in the dictionary
            if Pattern not in freqMap:
                freqMap[Pattern] = 1
            else:
                freqMap[Pattern] += 1
    except Exception as e:
        # Handle any exceptions and print an error message
        print(f"Error in FrequencyTable: {e}")

    # Return the final frequency table
    return freqMap


def MaxMap(freqMap):
    """
    Finds the maximum value in a map.

    Args:
    - freqMap (dict): A map (dictionary) with keys as strings and values as integers.

    Returns:
    - int: The maximum value in the map.
    """
    try:
        # Return the maximum value in the dictionary
        return max(freqMap.values())
    except Exception as e:
        # Handle any exceptions and print an error message
        print(f"Error in MaxMap: {e}")
        return 0  # Return 0 if there's an error.


def BetterFrequentWords(Text, k):
    """
    Finds all most frequent k-mers in a given text.

    Args:
    - Text (str): The input text.
    - k (int): The length of k-mers.

    Returns:
    - list: List of most frequent k-mers.
    """
    # Initialize an empty list to store most frequent k-mers
    FrequentPatterns = []
    # Build the frequency table using the FrequencyTable function
    freqMap = FrequencyTable(Text, k)
    # Find the maximum count in the frequency table using the MaxMap function
    maxCount = MaxMap(freqMap)

    try:
        # Iterate through each k-mer in the frequency table
        for pattern in freqMap:
            # Add the k-mer to the list if its count is equal to maxCount
            if freqMap[pattern] == maxCount:
                FrequentPatterns.append(pattern)
    except Exception as e:
        # Handle any exceptions and print an error message
        print(f"Error in BetterFrequentWords: {e}")

    # Return the final list of most frequent k-mers
    return FrequentPatterns
