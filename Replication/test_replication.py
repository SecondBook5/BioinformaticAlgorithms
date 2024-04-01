from replication import FrequencyMap
import unittest
from replication import PatternCount

class TestPatternCount(unittest.TestCase):

    def test_pattern_count_basic(self):
        # Test a basic case
        text = "CGATATATCCATAG"
        pattern = "ATA"
        expected_count = 3
        self.assertEqual(PatternCount(text, pattern), expected_count)

    def test_pattern_count_no_occurrences(self):
        # Test when pattern has no occurrences in text
        text = "CGATATATCCATAG"
        pattern = "GGG"
        expected_count = 0
        self.assertEqual(PatternCount(text, pattern), expected_count)

    def test_pattern_count_empty_inputs(self):
        # Test when text or pattern is empty
        with self.assertRaises(ValueError):
            PatternCount("", "ATA")
        with self.assertRaises(ValueError):
            PatternCount("CGATATATCCATAG", "")

    def test_pattern_count_pattern_longer_than_text(self):
        # Test when pattern length exceeds text length
        with self.assertRaises(ValueError):
            PatternCount("CGAT", "CGATAT")

    def test_case_insensitivity(self):
        # Test if the function correctly counts occurrences regardless of case
        text = "ATGcgtgatGTCgTGCA"
        pattern = "ATG"
        self.assertEqual(PatternCount(text, pattern), 2)

    def test_overlapping_occurrences(self):
        # Test if the function correctly counts overlapping occurrences
        text = "ATATATA"
        pattern = "ATA"
        self.assertEqual(PatternCount(text, pattern), 3)

    def test_single_character_pattern(self):
        # Test if the function correctly counts occurrences of a single character pattern
        text = "AAAAA"
        pattern = "A"
        self.assertEqual(PatternCount(text, pattern), 5)

    def test_pattern_at_start_end(self):
        # Test if the function correctly counts occurrences when pattern occurs at start/end of text
        text = "ATGATGATG"
        pattern = "ATG"
        self.assertEqual(PatternCount(text, pattern), 3)

        text = "ATGATGATGATG"
        pattern = "ATG"
        self.assertEqual(PatternCount(text, pattern), 4)

    def test_pattern_with_special_characters(self):
        # Test if the function correctly handles patterns with special characters
        text = "ATG#ATG$ATG"
        pattern = "#ATG$"
        self.assertEqual(PatternCount(text, pattern), 1)

class TestFrequencyMap(unittest.TestCase):

    def test_frequency_map_basic(self):
        # Test a basic case
        text = "CGATATATCCATAG"
        k = 2
        expected_freq_map = {'CG': 1, 'GA': 1, 'AT': 4, 'TA': 3, 'TC': 1, 'CC': 1, 'CA': 1, 'AG': 1}
        self.assertEqual(FrequencyMap(text, k), expected_freq_map)

    def test_frequency_map_empty_inputs(self):
        # Test when text is empty
        with self.assertRaises(ValueError):
            FrequencyMap("", 2)

    def test_frequency_map_non_positive_k(self):
        # Test when k is non-positive
        with self.assertRaises(ValueError):
            FrequencyMap("CGATATATCCATAG", 0)
        with self.assertRaises(ValueError):
            FrequencyMap("CGATATATCCATAG", -1)

    def test_case_insensitivity(self):
        # Test if the function correctly handles case insensitivity
        text = "ATGcgtgatGTCgTGCA"
        k = 5
        expected_freq_map = {'ATGCG': 1, 'TGCGT': 1, 'GCGTG': 1, 'CGTGA': 1, 'GTGAT': 1, 'TGATG': 1,
                             'GATGT': 1, 'ATGTC': 1, 'TGTCG': 1, 'GTCGT': 1, 'TCGTG': 1, 'CGTGC': 1, 'GTGCA': 1}
        self.assertEqual(FrequencyMap(text, k), expected_freq_map)

    def test_special_characters(self):
        # Test if the function correctly handles special characters
        text = "ATG#TG$G$G#A"
        k = 3
        expected_freq_map = {'ATG': 1, 'TG#': 1, 'G#T': 1, '#TG': 1,
                             'TG$': 1, 'G$G': 2, '$G$': 1, '$G#': 1, 'G#A': 1}
        self.assertEqual(FrequencyMap(text, k), expected_freq_map)

    def test_different_lengths_of_k(self):
        # Test if the function correctly handles different lengths of k
        text = "ATGATGATG"
        k1 = 2
        k2 = 3
        expected_freq_map_k1 = {'AT': 3, 'TG': 3, 'GA': 2}
        expected_freq_map_k2 = {'ATG': 3, 'TGA': 2, 'GAT': 2}
        self.assertEqual(FrequencyMap(text, k1), expected_freq_map_k1)
        self.assertEqual(FrequencyMap(text, k2), expected_freq_map_k2)

    def test_repeated_characters(self):
        # Test if the function correctly handles repeated characters in the text
        text = "AAAAA"
        k = 3
        expected_freq_map = {'AAA': 3}
        self.assertEqual(FrequencyMap(text, k), expected_freq_map)

    def test_text_with_spaces(self):
        # Test if the function correctly handles text with spaces
        text = "ATG ATG ATG"
        k = 3
        expected_freq_map = {'ATG': 3, 'TG ': 2, 'G A': 2, ' AT': 2}
        self.assertEqual(FrequencyMap(text, k), expected_freq_map)


if __name__ == "__main__":
    unittest.main()
