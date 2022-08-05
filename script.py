# Importing libraries
from hashlib import sha256
def letters_counters(file_path, alphabet):
    # Open the file
    file = open(file_path, "r")
    # Converting the file in readable way
    string = file.read()
   
    # Create an empty dictionary
    dict_count = {}
    
    for i in string.lower():
        # Check if it is in the alphabet (skipping special characters)
        if i in alphabet:
            # Updating the key of the dictionary
            if i in dict_count.keys():
                dict_count[i] += 1
            else:
                # Adding the new key
                dict_count.update({i:1})   

    # Sorting the dictionary in descending order by values
    dict_count = {k: v for k, v in sorted(dict_count.items(), reverse = True, key = lambda item: item[1])}
    return(dict_count, string)

def substitution_letters(plain_text, cipher_dict, corpus_dict,alphabet):
     
    # A sorted list with the frequency letters in the cipher text
    start_list = list(cipher_dict.keys())
    # A sorted list with the frequency letters in the plain text
    converted_list = list(corpus_dict.keys())

    # Substition of all the letters in the cipher text
    for k,v in zip(start_list, converted_list):
        plain_text = plain_text.replace(k.upper(), v)
       
    return plain_text

def bigram_count(text, alphabet):
    # Create an empty dictionary
    dict_bigram = {}
    
    for i in range(len(text)):
        
        # first letter of the bigram
        first = text[i-1]
        # second letter of the bigram
        second = text[i]
        
        # if the bigram contains any non alphabetic character  
        if first in alphabet and second in alphabet:
            # Merge the letters
            bigram = first + second
            
            # Updating the key of the dictionary
            if bigram in dict_bigram.keys():
                dict_bigram[bigram] += 1
            else:
                # Adding the new key
                dict_bigram.update({bigram:1})
    # Sorting the dictionary by values            
    dict_bigram = {k: v for k, v in sorted(dict_bigram.items(), reverse = True, key = lambda item: item[1])}
    return dict_bigram

def bigram_score(D):
    # Minimum value
    total_values = 0
    # New empty dictionary
    dict_score = {}
    # Summing all the frequencies of bigrams
    total_values = sum(list(D.values()))

    for k,v in D.items():
        # Calculating probability
        freq = v/total_values
        # Adding the value to the dictionary
        dict_score.update({ k : freq })

    return dict_score

def compute_score(dict_bigram_plain, dict_score_corpus):
    score = 0
    # Get the number of times of a bigram in the cipher text
    for k_c,v_c in dict_bigram_plain.items():

        try:
            # Get the score of the bigram corpus
            value = dict_score_corpus[k_c]
            # Multiply the score obtained the row above, with the number of times of 
            # the bigram in the cipher text
            score += (v_c*value)
        # If the bigram does not exist, skip to the next one
        except:
            continue
    return score

def swap_letter(first, second, string):
    # New swaped word
    swaped_word = ""
    # Storing the index of the first letter
    left_val_idx = []
    # Storing the index of the second letter
    right_val_idx = []
    
    for i in string:
        if i == first:
            left_val_idx.append(string.index(first))
        elif i == second:
            right_val_idx.append(string.index(second))

    for i in string:
        # if the index is equal to the index of first letter
        if string.index(i) in left_val_idx:
            # Adding the second letter the variable
            swaped_word += second
        # if the index is equal to the index of second letter
        elif string.index(i) in right_val_idx:
            # Adding the first letter the variable
            swaped_word += first
        # if the index does not correspond to any index previously stored
        else:
            # add the letter to the variable 
            swaped_word += i

    return swaped_word

def plain_score(plain_text, dict_score_corpus, alphabet):
    # Counting the numbers of bigrams in the plain text
    dict_plain_numbers = bigram_count(plain_text, alphabet)

    # Computing the plain text score 
    plain_text_score = compute_score(dict_plain_numbers, dict_score_corpus)
    
    return plain_text_score

def check_hash(plain_text, cipher_text, hash_text, alphabet):
    # Storing the key
    key = ""
    # Upper case of the cipher text
    test = cipher_text.upper()
    
    # Storing the key
    for i in alphabet:
        # Looking for the index of the letter in the plain text
        index = plain_text.index(i)
        # Adding the cripted letter to the key
        key += cipher_text[index]
    
    # Decrypting the cipher text using the key
    for i,j in zip(key, alphabet):
        test = test.replace(i.upper(),j)
    
    # Hashing the plain text
    digest = sha256(test.encode('utf-8')).hexdigest()
    
    # Open the hash file
    hash_digest = open(hash_text, "r")
    hash_digest = hash_digest.read()
    
    # Checking if the hashes are equal
    if digest == hash_digest:
        return True, test
    else:
        return False, test

def decrypt(corpus_file, cipher_file, hash_text):
    print("Loading...")
    # Creating the alphabet variable
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    # Doing the frequency analysis for the corpus
    corpus_dict, corpus_text = letters_counters(corpus_file, alphabet)
    # Doing the frequency analysis for the cipher text
    cipher_dict, cipher_text = letters_counters(cipher_file, alphabet)

    # Picking a small portion of the cipher text
    plain_text = cipher_text.upper()[:5000]

    # Substitute letters using values of frequency analysis 
    plain_text = substitution_letters(plain_text, cipher_dict, corpus_dict, alphabet)
    
    # Couting bigram in the corpus text 
    dict_bigram_count = bigram_count(corpus_text, alphabet)
    # Assigning a score in each bigram
    dict_score_corpus = bigram_score(dict_bigram_count)
    
    outcome, final_text = check_hash(plain_text, cipher_text, hash_text, alphabet)
    print(".")
    if outcome == True:
        return "***Message Decrypted with success!***", final_text
    else:
        for key_letter in alphabet:
            print(".")
            # Storing the score of the new permutations
            dict_score = {}

            for i in range (len(alphabet)):

                new_letter = alphabet[i]
                # Swapping two letters in the plain text
                result = swap_letter(key_letter, new_letter, plain_text)
                # Computing the score for the new plain text
                score = plain_score(result, dict_score_corpus, alphabet)
                # Storing the swapped letter and the relative score
                dict_score.update({new_letter : score})
                # Getting the key of the highest score
                best_match = max(dict_score, key = dict_score.get)

            # Searching the index of the letter in the alphabet
            plain_text = swap_letter(key_letter, best_match, plain_text)
            
            # Checking if the algorithm has found a best combination
            if best_match != key_letter :
                outcome, final_text = check_hash(plain_text, cipher_text, hash_text, alphabet)
                if outcome == True:
                    return "***Message Decrypted with success!***" , final_text

        return "Sorry, The message has not been decrypted", final_text


corpus_file_path = "data/corpus.txt"
cipher_file_path = "data/ciphertext.txt"
hash_file_path = "data/SHA256SUM.txt"
print(decrypt(corpus_file_path, cipher_file_path, hash_file_path))






