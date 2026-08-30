text = input("Enter text: ")
pattern1 = input("Enter successful search pattern: ")
pattern2 = input("Enter unsuccessful search pattern: ")


def brute_force(text, pattern):

    comparisons = 0

    for i in range(len(text) - len(pattern) + 1):

        for j in range(len(pattern)):
            comparisons += 1

            if text[i + j] != pattern[j]:
                break

        else:
            return comparisons

    return comparisons


c1 = brute_force(text, pattern1)
c2 = brute_force(text, pattern2)

print("Successful search comparisons =", c1)
print("Unsuccessful search comparisons =", c2)
