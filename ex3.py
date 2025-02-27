

def idpalindrom(word):
    for i in range(len(word)):  
        if word[i] != word[-(i + 1)]:
            return False
    return True  

print(idpalindrom("carac"))