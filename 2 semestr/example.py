strings = ["C", "T", "A", "C"]
i = 0
new_strings = []
    
str_string = ""
for string in strings:
    str_string += string
    for string in str_string[i]:
        new_string = string.replace("C", "G")
        new_strings.append(new_string)

        new_string = string.replace("G", "C")
        new_strings.append(new_string)
        i += 1



print(new_strings)



