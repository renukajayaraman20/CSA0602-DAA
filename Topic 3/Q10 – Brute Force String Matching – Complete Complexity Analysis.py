text = input("Enter text: ")
pattern = input("Enter pattern: ")

comparisons = 0
positions = []

print("\nShifting Process:")

for i in range(len(text) - len(pattern) + 1):

    print("\nShift", i)
    print("Text portion:", text[i:i + len(pattern)])
    print("Pattern     :", pattern)

    j = 0

    while j < len(pattern):

        comparisons += 1

        print("Comparing", text[i + j], "with", pattern[j])

        if text[i + j] != pattern[j]:
            print("Mismatch")
            break

        print("Match")
        j += 1

    if j == len(pattern):
        print("Pattern matched")
        positions.append(i)

print("\nPattern occurrences:", positions)
#output#
Enter text: TTATAGATCTCGTATTCTTTATAGATCTCCTATTCTT
Enter pattern: TATCTT

Shifting Process:

Shift 0
Text portion: TTATAG
Pattern     : TATCTT
Comparing T with T
Match
Comparing T with A
Mismatch

Shift 1
Text portion: TATAGA
Pattern     : TATCTT
Comparing T with T
Match
Comparing A with A
Match
Comparing T with T
Match
Comparing A with C
Mismatch

Shift 2
Text portion: ATAGAT
Pattern     : TATCTT
Comparing A with T
Mismatch

Shift 3
Text portion: TAGATC
Pattern     : TATCTT
Comparing T with T
Match
Comparing A with A
Match
Comparing G with T
Mismatch

Shift 4
Text portion: AGATCT
Pattern     : TATCTT
Comparing A with T
Mismatch

Shift 5
Text portion: GATCTC
Pattern     : TATCTT
Comparing G with T
Mismatch

Shift 6
Text portion: ATCTCG
Pattern     : TATCTT
Comparing A with T
Mismatch

Shift 7
Text portion: TCTCGT
Pattern     : TATCTT
Comparing T with T
Match
Comparing C with A
Mismatch

Shift 8
Text portion: CTCGTA
Pattern     : TATCTT
Comparing C with T
Mismatch

Shift 9
Text portion: TCGTAT
Pattern     : TATCTT
Comparing T with T
Match
Comparing C with A
Mismatch

Shift 10
Text portion: CGTATT
Pattern     : TATCTT
Comparing C with T
Mismatch

Shift 11
Text portion: GTATTC
Pattern     : TATCTT
Comparing G with T
Mismatch

Shift 12
Text portion: TATTCT
Pattern     : TATCTT
Comparing T with T
Match
Comparing A with A
Match
Comparing T with T
Match
Comparing T with C
Mismatch

Shift 13
Text portion: ATTCTT
Pattern     : TATCTT
Comparing A with T
Mismatch

Shift 14
Text portion: TTCTTT
Pattern     : TATCTT
Comparing T with T
Match
Comparing T with A
Mismatch

Shift 15
Text portion: TCTTTA
Pattern     : TATCTT
Comparing T with T
Match
Comparing C with A
Mismatch

Shift 16
Text portion: CTTTAT
Pattern     : TATCTT
Comparing C with T
Mismatch

Shift 17
Text portion: TTTATA
Pattern     : TATCTT
Comparing T with T
Match
Comparing T with A
Mismatch

Shift 18
Text portion: TTATAG
Pattern     : TATCTT
Comparing T with T
Match
Comparing T with A
Mismatch

Shift 19
Text portion: TATAGA
Pattern     : TATCTT
Comparing T with T
Match
Comparing A with A
Match
Comparing T with T
Match
Comparing A with C
Mismatch

Shift 20
Text portion: ATAGAT
Pattern     : TATCTT
Comparing A with T
Mismatch

Shift 21
Text portion: TAGATC
Pattern     : TATCTT
Comparing T with T
Match
Comparing A with A
Match
Comparing G with T
Mismatch

Shift 22
Text portion: AGATCT
Pattern     : TATCTT
Comparing A with T
Mismatch

Shift 23
Text portion: GATCTC
Pattern     : TATCTT
Comparing G with T
Mismatch

Shift 24
Text portion: ATCTCC
Pattern     : TATCTT
Comparing A with T
Mismatch

Shift 25
Text portion: TCTCCT
Pattern     : TATCTT
Comparing T with T
Match
Comparing C with A
Mismatch

Shift 26
Text portion: CTCCTA
Pattern     : TATCTT
Comparing C with T
Mismatch

Shift 27
Text portion: TCCTAT
Pattern     : TATCTT
Comparing T with T
Match
Comparing C with A
Mismatch

Shift 28
Text portion: CCTATT
Pattern     : TATCTT
Comparing C with T
Mismatch

Shift 29
Text portion: CTATTC
Pattern     : TATCTT
Comparing C with T
Mismatch

Shift 30
Text portion: TATTCT
Pattern     : TATCTT
Comparing T with T
Match
Comparing A with A
Match
Comparing T with T
Match
Comparing T with C
Mismatch

Shift 31
Text portion: ATTCTT
Pattern     : TATCTT
Comparing A with T
Mismatch

Pattern occurrences: []
Total comparisons = 57

Best Case Complexity = O(n)
Worst Case Complexity = O(n * m)
Space Complexity = O(1)

print("Total comparisons =", comparisons)

print("\nBest Case Complexity = O(n)")
print("Worst Case Complexity = O(n * m)")
print("Space Complexity = O(1)")
