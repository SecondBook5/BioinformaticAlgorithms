//FrequentWordsTest.Java
package edu.yu.bioinfo.test;

import java.util.List;
import org.junit.*;
import static org.junit.Assert.*;

import edu.yu.bioinfo.FrequentWords;


public class FrequentWordsTest {

    @Test
    public void testFrequentWords() {
        String text = "ACGTTTCACGTTTTACGG";
        int k = 3;
        List<String> frequentPatterns = FrequentWords.betterFrequentWords(text, k);
        assertEquals(List.of("ACG", "TTT"), frequentPatterns);
    }

    @Test
    public void testFrequentWordsWithLargeK() {
        String text = "ACGTTTCACGTTTTACGG";
        int k = 4;
        List<String> frequentPatterns = FrequentWords.betterFrequentWords(text, k);
        assertEquals(List.of("ACGT", "CGTT", "GTTT"), frequentPatterns);
    }

    @Test
    public void testFrequentWordsWithSinglePattern() {
        String text = "ACGTACGTACGTACGT";
        int k = 4;
        List<String> frequentPatterns = FrequentWords.betterFrequentWords(text, k);
        assertEquals(List.of("ACGT"), frequentPatterns);
    }

    @Test
    public void testFrequentWordsWithNoPatterns() {
        String text = "ACGT";
        int k = 5; // Set k to a value such that there are no repeating patterns
        List<String> frequentPatterns = FrequentWords.betterFrequentWords(text, k);
        assertEquals(List.of(), frequentPatterns);
    }

    @Test
    public void testFrequentWordsWithEmptyText() {
        String text = "";
        int k = 3;
        List<String> frequentPatterns = FrequentWords.betterFrequentWords(text, k);
        assertEquals(List.of(), frequentPatterns);
    }

    @Test
    public void testFrequentWordsWithEmptyPattern() {
        String text = "ACGTACGTACGTACGT";
        int k = text.length() + 1; // Set k to a value greater than the length of the text
        List<String> frequentPatterns = FrequentWords.betterFrequentWords(text, k);
        assertEquals(List.of(), frequentPatterns);
    }

    @Test
    public void testFrequentWordsWithRepeatedPatterns() {
        String text = "AAAAA";
        int k = 2;
        List<String> frequentPatterns = FrequentWords.betterFrequentWords(text, k);
        assertEquals(List.of("AA"), frequentPatterns);
    }

    @Test
    public void testFrequentWordsWithMixedCaseText() {
        String text = "acgtACGTacgtACGT";
        int k = 3;
        List<String> frequentPatterns = FrequentWords.betterFrequentWords(text, k);
        assertEquals(List.of("cgt", "CGT", "acg", "gtA", "ACG", "tAC"), frequentPatterns);
    }

    @Test
    public void testFrequentWordsWithMixedCasePattern() {
        String text = "ACGTACGTACGTACGTACGT";
        int k = 3; // Change this to the desired value
        List<String> frequentPatterns = FrequentWords.betterFrequentWords(text, k);
        assertEquals(List.of("CGT", "ACG"), frequentPatterns);
    }

    @Test
    public void testFrequentWordsWithSamePatternTwice() {
        String text = "ACGTACGT";
        int k = 4;
        List<String> frequentPatterns = FrequentWords.betterFrequentWords(text, k);
        assertEquals(List.of("ACGT"), frequentPatterns);
    }

    @Test
    public void testFrequentWordsWithMultiplePatterns() {
        String text = "ACGTACGTACGTACGTACGT";
        int k = 4;
        List<String> frequentPatterns = FrequentWords.betterFrequentWords(text, k);
        assertEquals(List.of("ACGT"), frequentPatterns);
    }

    @Test
    public void testFrequentWordsWithLongText() {
        String text = "ACGT" + "ACGTACGTACGTACGT".repeat(100) + "ACGT";
        int k = 4;
        List<String> frequentPatterns = FrequentWords.betterFrequentWords(text, k);
        assertEquals(List.of("ACGT"), frequentPatterns);
    }

    @Test
    public void testFrequentWordsWithMixedCaseTextAndPattern() {
        String text = "ACGTACGTacgtACGT";
        int k = 3; // Change this to the desired value
        List<String> frequentPatterns = FrequentWords.betterFrequentWords(text, k);
        assertEquals(List.of("CGT", "ACG"), frequentPatterns); // Adjust the expected result accordingly
    }

    // Add more test cases as needed
}