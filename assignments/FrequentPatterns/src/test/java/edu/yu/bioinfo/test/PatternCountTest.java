// PatternCountTest.java
package edu.yu.bioinfo.test;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.MethodSource;

import static org.junit.jupiter.api.Assertions.assertEquals;

import java.util.stream.Stream;

import edu.yu.bioinfo.PatternCount;

public class PatternCountTest {

    @ParameterizedTest
    @MethodSource("patternCountTestData")
    public void testPatternCount(String text, String pattern, int expectedCount) {
        int actualCount = PatternCount.patternCount(text, pattern);
        assertEquals(expectedCount, actualCount);
    }

    private static Stream<Object[]> patternCountTestData() {
        return Stream.of(
                new Object[] { "AGCTAGCTAGCTAGCT", "GCT", 4 },
                new Object[] { "AAATTTGGGCCCAAATTT", "A", 6 },
                new Object[] { "ATGC", "ATGCGC", 0 },
                new Object[] { "ACGT" + "ACGTACGTACGTACGT".repeat(1000) + "ACGT", "ACGT", 4002 });
    }

    @Test
    public void testPatternCountWithNoMatch() {
        String text = "ACGTTTCACGTTTTACGG";
        String pattern = "AAAA";
        int expectedCount = 0;
        int actualCount = PatternCount.patternCount(text, pattern);
        assertEquals(expectedCount, actualCount);
    }

    @Test
    public void testPatternCountWithEmptyText() {
        String text = "";
        String pattern = "ACGT";
        int expectedCount = 0;
        int actualCount = PatternCount.patternCount(text, pattern);
        assertEquals(expectedCount, actualCount);
    }
    
    @Test
    public void testPatternCountWithEmptyPattern() {
        String text = "ACGTTTCACGTTTTACGG";
        String pattern = "";
        int expectedCount = 0;
        int actualCount = PatternCount.patternCount(text, pattern);
        assertEquals(expectedCount, actualCount);
    }

    @Test
    public void testPatternCountWithPatternEqualToText() {
        String text = "ACGTACGTACGT";
        String pattern = "ACGTACGTACGT";
        int expectedCount = 1;
        int actualCount = PatternCount.patternCount(text, pattern);
        assertEquals(expectedCount, actualCount);
    }

    @Test
    public void testPatternCountWithPatternAsSubstring() {
        String text = "ACGTACGTACGT";
        String pattern = "ACGT";
        int expectedCount = 3;
        int actualCount = PatternCount.patternCount(text, pattern);
        assertEquals(expectedCount, actualCount);
    }

    @Test
    public void testPatternCountWithMixedCaseTextAndPattern() {
        String text = "acgtACGTacgtACGT";
        String pattern = "ACGT";
        int expectedCount = 4; // Case-insensitive matching should count all occurrences
        int actualCount = PatternCount.patternCount(text, pattern);
        assertEquals(expectedCount, actualCount);
    }

    @Test
    public void testPatternCountWithSpecialCharacters() {
        String text = "ACGT$%#ACGT!@acgt";
        String pattern = "ACGT";
        int expectedCount = 3; // Special characters should not affect matching
        int actualCount = PatternCount.patternCount(text, pattern);
        assertEquals(expectedCount, actualCount);
    }

    @Test
    public void testPatternCountWithRandomTextAndPattern() {
        String text = "AGCTAGCTAGCTAGCT";
        String pattern = "GCT";
        int count = PatternCount.patternCount(text, pattern);
        assertEquals(4, count);
    }

    @Test
    public void testPatternCountWithSingleCharacterPattern() {
        String text = "AAATTTGGGCCCAAATTT";
        String pattern = "A";
        int count = PatternCount.patternCount(text, pattern);
        assertEquals(6, count);
    }

    @Test
    public void testPatternCountWithPatternLongerThanText() {
        String text = "ATGC";
        String pattern = "ATGCGC";
        int count = PatternCount.patternCount(text, pattern);
        assertEquals(0, count);
    }

    @Test
    public void testPatternCountWithLargeTextAndPattern() {
        String text = "ACGT" + "ACGTACGTACGTACGT".repeat(1000) + "ACGT";
        String pattern = "ACGT";
        int count = PatternCount.patternCount(text, pattern);
        assertEquals(4002, count);
    }
    
    @Test
    public void testPatternCountWithValidInput() {
        // Test case with valid input
        String text = "ACGTTTCACGTTTTACGG";
        String pattern = "ACGT";
        int expectedCount = 2; // The pattern "ACGT" appears three times in the text
        int actualCount = PatternCount.patternCount(text, pattern);
        assertEquals(expectedCount, actualCount);
    }
}
