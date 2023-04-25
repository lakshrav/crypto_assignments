def printString(S, N):
     
    # Stores 5 possible PT after frequency analysis
    plaintext = [None] * 5
     
    # Stores frequency of all CT
    freq = [0] * 26
    freqSorted = [None] * 26
     
    # Store which alphabet is used already
    used = [0] * 26
     
    for i in range(N):
        if S[i] != ' ':
            freq[ord(S[i]) - 65] += 1
             
    for i in range(26):
        freqSorted[i] = freq[i]
         
    # High frequency letters in English stored in T  
    T = "ETAOINSHRDLCUMWFGYPBVKJXQZ"
     
    # Sort the array in descending order -> so high frequency letter of CT is first
    freqSorted.sort(reverse = True)
     
    for i in range(5):
        ch = -1
         
        for j in range(26):
            if freqSorted[i] == freq[j] and used[j] == 0:
                used[j] = 1
                ch = j
                break
             
        if ch == -1:
            break
         
        # Store the numerical equivalent of letter
        # at ith index of array letter_frequency
        x = ord(T[i]) - 65
         
        # Calculate a possible shift
        x = x - ch
         
        # Temporary string to store answer
        curr = ""
         
        # Generate ith most probable PT
        for k in range(N):
             
            if S[k] == ' ':
                curr += " "
                continue
             
            y = ord(S[k]) - 65
            y += x # adding key
             
            if y < 0:
                y += 26
            if y > 25: # mod
                y -= 26
             
            # Add letter    
            curr += chr(y + 65)
             
        plaintext[i] = curr
     
    # Print final   
    for i in range(5):
        print(plaintext[i])
 
# Driver 
S=input("Enter cipher text: ") 
N = len(S)
printString(S, N)
