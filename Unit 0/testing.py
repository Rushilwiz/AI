str = input ("Type a string to do permutation: ")

def permute(str): 
    if len(str) <= 1:
        return str
    
    perm_list = []
    for substr in permute(str[1:]): # Generate all of the permutations of the string excluding the first letter
        for pos in range(len(substr)+1): # Generate all of the positions that first letter can go
            perm_list.append(substr[:pos] + str[0] + substr[pos:]) # Put it in all of those positions
    return perm_list

perms = permute(str)
print (f'22. all permutations {perms}')

# 23. Given the input string from #22, find all the unique permutations of a string.
print (f'23. all unique permutations {set(perms)}')