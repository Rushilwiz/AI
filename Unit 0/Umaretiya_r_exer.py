# Name: Rushil Umaretiya
# Date: 09/10/2020
# Do not forget to change the file name -> Save as

from PIL import Image
from collections import Counter
from itertools import permutations

''' Tasks '''
# 1. Given an input of a space-separated list of any length of integers, output the sum of them.
# 2. Output the list of those integers (from #1) that are divisible by three.
list = input("list of numbers: ")
print (f"1. sum = {sum([int(x) for x in list.strip().split()])}")
print (f"2. list of multiples of 3: {[int(x) for x in list.strip().split() if int(x) % 3 == 0]}")

# 3. Given an integer input, print the first n Fibonacci numbers. eg. n=6: 1, 1, 2, 3, 5, 8

n = int(input ("Type n for Fibonacci sequence: "))

def fib(n):
    if n <= 0:
        return None
    elif n <= 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
list = []
for i in range(1,n+1): list.append(fib(i))
print (f"3. fibonacci:  ", end='')
print (*list)


# 4. Given an input, output a string composed of every other character. eg. Aardvark -> Arvr

print ('4. every other str: ', ((lambda str: ''.join([str[x*2] for x in range(len(str)//2)]))(input("Type a string: "))))

# 5. Given a positive integer input, check whether the number is prime or not.

n = int(input("Type a number to check prime: "))
isPrime = False
if n != 1:
    for i in range (2, n):
        if n % i == 0:
            break
    else:
        isPrime = True

print (f'5. Is prime? {isPrime}')

# 6. Calculate the area of a triangle given three side lengths.  eg. 13 14 15 -> 84
list = []
for x in input("Type three sides of a triangle: ").strip().split():
    list.append(int(x)) 
p = sum(list)/2
print("6. The area of", *list, "is", (p*(p-list[0])*(p-list[1])*(p-list[2]))**(1/2))

# 7. Given a input of a string, remove all punctuation from the string. 
# eg. "Don't quote me," she said. -> Dontquotemeshesaid)
str = input("Type a sentence: ")
nopunct = ''.join([i for i in str if i not in '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ '])
print (f'7. Punct removed: {nopunct}')

# 8. Check whether the input string (from #7, lower cased, with punctuation removed) is a palindrome.
palindrome = nopunct.lower() == nopunct[::-1].lower()
print (f'8. Is palindrome? {palindrome}')

# 9. Count the number of each vowel in the input string (from #7).

vowels = {
    'a':len([i for i in nopunct if i in 'a']),
    'e':len([i for i in nopunct if i in 'e']),
    'i':len([i for i in nopunct if i in 'i']),
    'o':len([i for i in nopunct if i in 'o']),
    'u':len([i for i in nopunct if i in 'u'])
}

print (f'9. Count each vowel: {vowels}')
# 10. Given two integers as input, print the value of f\left(k\right)=k^2-3k+2 for each integer between the two inputs.  
# eg. 2 5 -> 0, 2, 6, 12
ints = input ("Type two integers (lower bound and upper bound): ")
list = ints.strip().split()
ans = []
for i in range(int(list[0]),int(list[1]) + 1):
    ans.append(int(i)**2-(3*int(i))+2)
print (f'10. Evaluate f(k)=k^2 - 3k + 2 from {list[0]} to {list[1]}:', *ans)

# 11. Given an input of a string, determines a character with the most number of occurrences.
str = input ("Type a string: ")
freq = {}
for char in str.lower():
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1
max_freq = max(freq.values())
max_letters = []
for char in freq.keys():
    if freq[char] == max_freq:
        max_letters.append(char)

print ('11. Most occurred char:', *max_letters)

# 12. With the input string from #11, output a list of all the words that start and end in a vowel.

vowels = []
for word in str.strip().split():
    if len(word) > 0 and word[0] in 'aeiou' and word[len(word)-1] in 'aeiou':
        vowels.append(word)

print (f'12. List of words starting and ending with vowels: {vowels}')

# 13. With the input string from #11, capitalizes the starting letter of every word of the string and print it.
words = [word.capitalize() for word in str.strip().split()]
print ('13. Capitalize starting letter of every word:', *words)

# 14. With the input string from #11, prints out the string with each word in the string reversed.
words = [word[::-1] for word in str.strip().split()]
print ('14. Reverse every word:', *words)

# 15. With the input string from #11, treats the first word of the input as a search string to be found in the rest 
# of the string, treats the second word as a replacement for the first, and treats the rest of the input as the string to be searched.
#   eg.    b Ba baby boy ->  BaaBay Baoy
words = str.strip().split()
search = words[0]
replace = words[1]
for i in range(2, len(words)):
    words[i] = words[i].replace(search, replace)
print ('15. Find the first and replace with the second:', *words[2:])
 
# 16. With an input of a string, removes all duplicate characters from a string.  Eg. detection -> detcion
str = input('Type a string to remove all duplicate chars: ')
letters = []
out = ''
for char in str:
    if char not in letters:
        letters.append(char)
        out += char
print (f'16. Remove all duplicate chars: {out}')

# 17. Given an input of a string, determines whether the string contains only digits.
str = input('Type a string to check if it has only digits or not: ')
print (f'17. Is a number?: {str.isnumeric()}')

# 18. If #17 prints True, determines whether the string contains only 0 and 1 characters, and if so assumes it is a binary string, 
# converts it to a number, and prints out the decimal value.
out = "No"

if str.isnumeric():
    if len([i for i in str if i in '23456789']) == 0:
        out = int(str, 2)
print (f'18. It is a binary number: {out}')

# 19. Write a script that accepts two strings as input and determines whether the two strings are anagrams of each other.
first = input("Type the first string to check anagram: ").strip().replace(' ', '')
second = input("Type the second string to check anagram: ").strip().replace(' ', '')

print(f'19. Are {first} and {second} anagrams?:', len(first) == len(second) and sorted(first) == sorted(second))

# 20. Given an input filename, if the file exists and is an image, find the dimensions of the image.
url = input("Type the image file name: ").strip()
try:
    img = Image.open(url)
    print (f"20. Image dimension: {img.width} by {img.height}")
except:
    print ("20. Image dimension: Image file does not exist or file is not an image")

# 21. Given an input of a string, find the longest palindrome within the string.
str = input ("Type a string to find the longest palindrome: ")
str = ''.join([i for i in str if i not in '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ '])
longest = ''
for i in range(len(str)):
    for j in range(len(str)):
        if str[j:i+j] == str[j:i+j][::-1] and len(str[j:i+j]) > len(longest):
            longest = str[j:i+j]
print (f'21. Longest palindrome within the string: {longest}')
 
# 22. Given an input of a string, find all the permutations of a string.
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
 
# 24. Given an input of a string, find a longest non-decreasing subsequence within the string (according to ascii value).
str = input('Type a string to find the longest non-decreasing sub: ').strip().replace(' ', '')
longest = ''
for i in range(len(str)):
    temp = str[i]
    for j in range(i+1, len(str)):
        if temp[-1] <= str[j]:
            temp += str[j]
        else:
            break

    if len(temp) > len(longest):
        longest = temp
print (f'24. longest non-decreasing sub: {longest}')