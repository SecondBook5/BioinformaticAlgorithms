def FrequencyMap(Text, k):
    """
    Generates a frequency map of k-mers in the given text using a sliding window approach.

    Args:
        Text (str): The text to analyze.
        k (int): The length of k-mers.

    Returns:
        dict: A dictionary where keys are k-mers and values are their frequencies.
        
    Raises:
        ValueError: If Text is empty or k is non-positive.
    """
    if not Text:
        raise ValueError("Text must not be empty")
    if k <= 0:
        raise ValueError("k must be a positive integer")
    
     # Remove whitespace from the text
    Text = ''.join(Text.split())

    # Initialize a dictionary to store the frequencies of k-mers
    freq = {}
    n = len(Text)

  #Iterate over the text with a sliding window approach
    for i in range(n - k + 1):
        # Extract the substring of length 'k' starting at index 'i' and convert it to uppercase to make the function case-insensitive
        pattern = Text[i:i + k].upper() 
        # Increment the frequency count of the current pattern by 1
        freq[pattern] = freq.get(pattern, 0) + 1

    return freq


def MaxMap(freqMap):
    """
    Finds the maximum value in a map and returns the value, kmers with that value, and their length.

    Args:
    - freqMap (dict): A map (dictionary) with keys as strings and values as integers.

    Returns:
    - tuple: A tuple containing the maximum value, kmers with that value, and their length.
    """
    max_value = max(
        freqMap.values())  # Find the maximum value in the dictionary
    # Find kmers with maximum value
    max_kmers = [kmer for kmer, count in freqMap.items() if count == max_value]
    kmer_length = len(max_kmers[0])  # Get the length of the kmers
    print(f"The maximum value is: {max_value}")
    print(f"The kmers with the maximum value are: {max_kmers}")
    print(f"The length of the kmers is: {kmer_length}")
    # Return the maximum value, kmers, and their length as a tuple
    return max_value, max_kmers, kmer_length


