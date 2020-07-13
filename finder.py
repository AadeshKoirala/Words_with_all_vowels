file_to_read = "wordlist.txt"
sort_by_length = True

with open(file_to_read, "r") as f:
    lines = f.readlines()

# ___FIND THE WORDS 
words = []
for line in lines:
    if "a" in line:
        if "e" in line:
            if "i" in line:
                if "o" in line:
                    if "u" in line:
                        words.append(line)

#____SORT BY LINE LENGTH
# ___MERGE SORT
def comparator(val_a, val_b, comparator_type="LENGTH_OF_ELEMENT"):
    if comparator_type == "LENGTH_OF_ELEMENT":
        if len(val_a) < len(val_b):
            return val_a
        elif len(val_a) > len(val_b):
            return val_b
        else:
            return comparator(val_a, val_b, "ALPHABETICALLY")
    
    if comparator_type == "ALPHABETICALLY":
        unequal_condition = False
        a = val_a.lower()
        b = val_b.lower()
        while a and b:
            if ord(a[0]) < ord(b[0]):
                return val_a
            elif ord(b[0]) < ord(a[0]):
                return val_b
            else:
                if a:
                    a = a[1:]
                if b:
                    b = b[1:]
        if len(a) < len(b):
            return val_a
        else:
            return val_b
        

def merge_merged_lists(list1, list2, comparator_type):
    return_list = []
    while list1 and list2:
        if comparator(list1[0], list2[0], comparator_type) == list1[0]:
            return_list.append(list1[0])
            del list1[0]
        else:
            return_list.append(list2[0])
            del list2[0]
    if list1:
        return_list += list1
    if list2:
        return_list += list2
    return return_list

def merge(list, comparator_type):
    if len(list) == 1:
        return list
    
    list_a = list[ : len(list) // 2]
    list_b = list[len(list) // 2 : ]
    
    list_a = merge(list_a, comparator_type)
    list_b = merge(list_b, comparator_type)
    
    merged_list = merge_merged_lists(list_a, list_b, comparator_type)
    return merged_list
    
words = merge(words, "LENGTH_OF_ELEMENT")


# ___SAVE THE LIST
with open("words_with_vowels.txt", "w") as f:
    for word in words:
        f.write(word)