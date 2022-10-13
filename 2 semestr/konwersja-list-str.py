def listToString(DNA):

    i = 0
    rev2_DNA = []

    if not(len(DNA) == 0):
            for i in DNA:
                rev_DNA = DNA[::-1]                                         #odczytanie tablicy DNA od tylu
                for i in range(len(rev_DNA)):
                    if rev_DNA[i] == "A":
                        rev2_DNA = rev_DNA[0+i] + "T" + rev_DNA[(2+i):]
                        i += 1    
    return rev2_DNA

DNA = ['A', 'A', 'T', 'C', 'G', 'G', 'C', 'A', 'T', 'G', 'C', 'C', 'A', 'T', 'G', 'G', 'C', 'C', 'T', 'T', 'G', 'C', 'G', 'C', 'T', 'A']
listToString(DNA)
print(listToString(DNA))

"""
                        if rev_DNA[w] == "T":
                            rev2_DNA[w] = w.replace("T", "A") 
                        if rev_DNA[w] == "C":
                            rev2_DNA[w] = w.replace("C", "G")
                        if rev_DNA[w] == "G":
                            rev2_DNA[w] = w.replace("G", "C")
"""