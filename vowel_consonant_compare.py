def vowel_consonant_compare(s):
    vowels = "aeiou"
    vowel_count = 0
    consonant_count = 0
    
    for char in s:
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1
    
    if vowel_count > consonant_count:
        return "Yes"
    elif vowel_count < consonant_count:
        return "No"
    else:
        return "Same"

print(vowel_consonant_compare("thequickbrownfoxjumpsoverthelazydog"))  # No
print(vowel_consonant_compare("aaaaaa"))   # Yes
print(vowel_consonant_compare("abab"))     # Same
