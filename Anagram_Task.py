# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(words, sword):
    # [assignment] Add your code here
   if (sorted(words) == sorted(sword)):
        print(sorted(words), sorted(sword))
        return True
   return False

find_anagram('words', 'sword')
    
    
