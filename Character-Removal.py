
"""

Character Removal
Have the function CharacterRemoval(strArr) read the array of strings stored in strArr, which will contain 2 elements: the first element will be a sequence of characters representing a word, and the second element will be a long string of comma-separated words, in alphabetical order, that represents a dictionary of some arbitrary length. For example: strArr can be: ["worlcde", "apple,bat,cat,goodbye,hello,yellow,why,world"]. Your goal is to determine the minimum number of characters, if any, can be removed from the word so that it matches one of the words from the dictionary. In this case, your program should return 2 because once you remove the characters "c" and "e" you are left with "world" and that exists within the dictionary. If the word cannot be found no matter what characters are removed, return -1.

Examples
Input: ["baseball", "a,all,b,ball,bas,base,cat,code,d,e,quit,z"]
Output: 4

Input: ["apbpleeeef", "a,ab,abc,abcg,b,c,dog,e,efd,zzzz"]
Output: 8

# # #
Calculating runtime...
Above will be the running time of your algorithm expressed in Big-O notation. Big-O notation is used to classify algorithms according to how their run time grows as the input size grows. To learn more here is a video we published on this topic, and here is a guide on how it works.

It may take a few minutes for it to finish calculating.
# # #

"""



from itertools import combinations

def CharacterRemoval(strArr):

  # code goes here
  list_of_chars = list(strArr[0])

  possible_words = [combinations(list_of_chars, length) for length in range(1, len(list_of_chars) +1 )]

  length_max = 0

  for words in possible_words:
    for word in words:
      possible_out_word = "".join(word)
      if possible_out_word in strArr[1].split(","):
        if len(possible_out_word) > length_max:
          length_max = len(possible_out_word)

  if length_max > 0:
    return len(strArr[0]) - length_max

  return -1

# keep this function call here 
print CharacterRemoval(raw_input())
