# main.py
from FrequentWords import BetterFrequentWords
from PatternCount import PatternCount

def main():
    # Sample Input
    #Text = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
    #k = 4
    Text = "CGCCTAAATAGCCTCGCGGAGCCTTATGTCATACTCGTCCT"
    k = 3
    
    


    # Output
    print(f"Input Text: {Text}")
    print(f"Value of k: {k}")

    try:
        output = BetterFrequentWords(Text, k)
        if output:
            print(f"Most Frequent {k}-mers: {' '.join(output)}")
        else:
            print("No frequent k-mers found.")
    except Exception as e:
        print(f"Error in main: {e}")


if __name__ == "__main__":
    main()
