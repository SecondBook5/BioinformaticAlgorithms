//PatternCount.java
package edu.yu.bioinfo;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class PatternCount {

    /**
     * Counts the occurrences of a pattern in a given text.
     *
     * @param text    The input text.
     * @param pattern The pattern to count.
     * @return The count of occurrences of the pattern in the text.
     * @throws IllegalArgumentException If the pattern is empty or longer than the
     *                                  text.
     */
    public static int patternCount(String text, String pattern) {
        // Validate input
        if (pattern.isEmpty()) {
            return 0; // If the pattern is empty, it cannot have occurrences
        }

        // Check if Pattern is longer than text, if it is that is an illegal argument
        if (pattern.length() > text.length()) {
            throw new IllegalArgumentException("Pattern cannot be longer than Text");
        }
        
        int count = 0;
        // Iterate through the text to find occurrences of the pattern
        for (int i = 0; i <= text.length() - pattern.length(); i++) {
            // Check if the substring of the text matches the pattern
            if (text.substring(i, i + pattern.length()).equals(pattern)) {
                count++;
            }
        }
        return count;
    }
    /**
     * Reads input from a text file, runs patternCount, and prints the result.
     *
     * @param args Command-line arguments (not used in this example).
     */
    public static void main(String[] args) {
        // Read input from a text file
        String fileName = "data/Vibrio_cholerae.txt"; // Provide the actual file name
        String text = "";
        String pattern = "TGATCA";

        try {
            Scanner scanner = new Scanner(new File(fileName));

            // Assuming the first line is the text and the second line is the pattern
            if (scanner.hasNextLine()) {
                text = scanner.nextLine();
            }
            //if (scanner.hasNextLine()) {
                //pattern = scanner.nextLine();
            //}

            scanner.close();
        } catch (FileNotFoundException e) {
            // Handle file not found exception
            System.err.println("File not found: " + e.getMessage());
            return;
        }

        // Output the result of patternCount
        int count = patternCount(text, pattern);
        System.out.println("Occurrences of pattern '" + pattern + "' in the text: " + count);
    }
}
