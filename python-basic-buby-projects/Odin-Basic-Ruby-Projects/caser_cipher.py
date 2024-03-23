import string

alphabet_upper = list(string.ascii_uppercase)
alphabet_lower = list(string.ascii_lowercase)

def caesar_cipher(phrase, index_shift):
    encryted_phrase = ""
    
    for letters in phrase:
        if letters in alphabet_upper:
                encryted_phrase =  encryted_phrase + alphabet_upper[(alphabet_upper.index(letters) + index_shift) - len(alphabet_upper)]
        elif letters in alphabet_lower:   
            encryted_phrase =  encryted_phrase + alphabet_lower[(alphabet_lower.index(letters) + index_shift) - len(alphabet_lower)] 
        else:
            encryted_phrase = encryted_phrase + letters
            
    print(encryted_phrase)
        

        
caesar_cipher("What a string!", 5)
