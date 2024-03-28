def CountWithPseudocounts(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    count = {}  # output variable
    for symbol in "ACGT":
        count[symbol] = [1] * k  # Initialize counts with pseudocounts
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1
    return count


def ProfileWithPseudocounts(Motifs):
    """
    Form a profile matrix with pseudocounts from a collection of motifs.

    Parameters:
    - motifs (list): Collection of motifs.

    Returns:
    - list: Profile matrix with pseudocounts.
    """
    t = len(Motifs)
    k = len(Motifs[0])
    profile = {}
    count_matrix = CountWithPseudocounts(Motifs)
    for symbol in "ACGT":
        # Pseudocounts added
        profile[symbol] = [count / (t + 4) for count in count_matrix[symbol]]
    return profile
