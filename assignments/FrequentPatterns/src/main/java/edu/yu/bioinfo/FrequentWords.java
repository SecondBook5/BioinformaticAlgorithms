// FrequentWords.java

package edu.yu.bioinfo;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;

public class FrequentWords {

    /**
     * Finds the most frequent k-mers in a given text.
     *
     * @param text The input text.
     * @param k    The length of k-mers.
     * @return List of most frequent k-mers.
     */
    public static List<String> frequentWords(String text, int k) {
        // A set to store unique most frequent k-mers
        Set<String> frequentPatterns = new HashSet<>();
        // An array to store the count of each k-mer
        int[] count = new int[text.length() - k + 1];

        try {
            // Iterate through the text to build counts for each k-mer
            for (int i = 0; i <= text.length() - k; i++) {
                // Extract the current k-mer from the text
                String pattern = text.substring(i, i + k);
                // Count occurrences of the current k-mer in the text
                count[i] = patternCount(text, pattern);
            }

            // Find the maximum count among all k-mers
            int maxCount = Arrays.stream(count).max().orElse(0);

            // Collect k-mers with counts equal to the maximum count
            for (int i = 0; i <= text.length() - k; i++) {
                if (count[i] == maxCount) {
                    frequentPatterns.add(text.substring(i, i + k));
                }
            }
        } catch (Exception e) {
            // Handle exceptions
            System.err.println("Error in frequentWords: " + e.getMessage());
        }

        // Convert the set to a list and return the result
        return new ArrayList<>(frequentPatterns);
    }

    /**
     * Counts the occurrences of a pattern in a given text.
     *
     * @param text    The input text.
     * @param pattern The pattern to count.
     * @return The count of occurrences of the pattern in the text.
     */
    private static int patternCount(String text, String pattern) {
        int count = 0;
        // Iterate through the text to find occurrences of the pattern
        for (int i = 0; i <= text.length() - pattern.length(); i++) {
            // Check if the substring of the text matches the pattern
            if (text.substring(i, i + pattern.length()).equals(pattern)) {
                count++;
            }
        }
        // Return the count of occurrences
        return count;
    }

    /**
     * Builds a frequency table for k-mers in a given text.
     *
     * @param text The input text.
     * @param k    The length of k-mers.
     * @return A frequency table (Map) of k-mers.
     */
    private static Map<String, Integer> frequencyTable(String text, int k) {
        // A map to store the frequency count for each k-mer
        Map<String, Integer> freqMap = new HashMap<>();
        try {
            // Iterate through the text to build the frequency table
            for (int i = 0; i <= text.length() - k; i++) {
                // Extract the current k-mer from the text
                String pattern = text.substring(i, i + k);
                // Update the count for the current k-mer in the map
                freqMap.put(pattern, freqMap.getOrDefault(pattern, 0) + 1);
            }
        } catch (Exception e) {
            // Handle exceptions
            System.err.println("Error in frequencyTable: " + e.getMessage());
        }
        // Return the frequency table
        return freqMap;
    }

    /**
     * Finds the maximum value in a map.
     *
     * @param freqMap A map (dictionary) with keys as strings and values as
     *                integers.
     * @return The maximum value in the map.
     */
    private static int maxMap(Map<String, Integer> freqMap) {
        try {
            // Find the maximum value using Collections.max
            return Collections.max(freqMap.values());
        } catch (Exception e) {
            // Handle exceptions
            System.err.println("Error in maxMap: " + e.getMessage());
            return 0; // Return 0 if there's an error.
        }
    }

    /**
     * Finds all most frequent k-mers in a given text.
     *
     * @param text             The input text.
     * @param mixedCasePattern The length of k-mers.
     * @return List of all most frequent k-mers.
     */
    public static List<String> betterFrequentWords(String text, int mixedCasePattern) {
        // A set to store unique most frequent k-mers
        Set<String> frequentPatterns = new HashSet<>();
        // Build the frequency table for k-mers
        Map<String, Integer> freqMap = frequencyTable(text, mixedCasePattern);
        // Find the maximum count among all k-mers in the frequency table
        int maxCount = maxMap(freqMap);

        try {
            // Collect k-mers with counts equal to the maximum count
            for (Map.Entry<String, Integer> entry : freqMap.entrySet()) {
                if (entry.getValue() == maxCount) {
                    frequentPatterns.add(entry.getKey());
                }
            }
        } catch (Exception e) {
            // Handle exceptions
            System.err.println("Error in betterFrequentWords: " + e.getMessage());
        }

        // Convert the set to a list and return the result
        return new ArrayList<>(frequentPatterns);
    }

    /**
     * Reads input from a text file, runs betterFrequentWords, and prints the
     * result.
     *
     * @param args Command-line arguments (not used in this example).
     */
    public static void main(String[] args) {
        // Read input from a text file
        String fileName = "data/rosalind_ba1b.txt"; // Provide the actual file name
        String text = "";
        int k = 0;

        try {
            Scanner scanner = new Scanner(new File(fileName));

            // Assuming the first line is the text and the second line is the value of k
            if (scanner.hasNextLine()) {
                text = scanner.nextLine();
            }
            if (scanner.hasNextLine()) {
                k = Integer.parseInt(scanner.nextLine());
            }

            scanner.close();
        } catch (FileNotFoundException e) {
            // Handle file not found exception
            System.err.println("File not found: " + e.getMessage());
            return;
        }

        // Output the result of betterFrequentWords
        List<String> frequentPatterns = betterFrequentWords(text, k);
        System.out.println("Most frequent " + k + "-mers in the text: " + frequentPatterns);
    }
}
