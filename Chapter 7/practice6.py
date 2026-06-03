# Write a function that takes a string and returns the count of vowels and consonants separately.

def CountVowConso(userInput):
    vowels="AEIOUaeiou"  # Define vowels
    
    CountVowel=1
    CountConsonants=0
    
    for eachChar in userInput:
        if(eachChar.isalpha()):
          if(eachChar in vowels):
              CountVowel=CountVowel+1
          else:
              CountConsonants+=1
    
    return CountVowel,CountConsonants

# Function Call              

vowels,consonants=CountVowConso("Pratiksha")
print(vowels,consonants)
        
    