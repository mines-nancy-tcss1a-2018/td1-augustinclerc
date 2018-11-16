## Problem 16

def digitsum(n):
    l=str(n)
    somme=0
    for i in range(len(l)):
        somme+=int(l[i])
    return somme


# print(digitsum(2**1000))



## Probelm 22

alphabet=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

def str_to_num(lettre):
    for i in range(len(alphabet)):
        if lettre==alphabet[i]:
            return (i+1)

# print(str_to_num('D'))

def score_prenom(prenom):
    score=0
    for i in range(len(prenom)):
        score += str_to_num(prenom[i])
    return score 

# print(score_prenom("COLIN"))

def names_score (liste_noms):
    liste_noms.sort()
    score_total=0
    for i in range(len(liste_noms)):
        score_total += (i+1) * score_prenom(liste_noms[i])
    return score_total

L = ["MARY","PATRICIA","LINDA","BARBARA","ELIZABETH","JENNIFER"]
# print (names_score(L))



## Problem 55

def test_palindrome(n):
    l=str(n)
    i=0
    j=len(l)-1
    bool=True
    while (i<j and bool) :
        if l[i] != l[j] :
            bool=False
        i+=1
        j-=1
    return bool

#print(test_palindrome(15851))

def reverse(n):
    l1=str(n)
    l2=""
    for i in range(len(l1)-1,-1,-1):
        l2+=l1[i]
    return int(l2)

# print (reverse(1984))


def test_lychrel(n,num_iteration):
    N=n+reverse(n)
    #print(N)
    if test_palindrome(N):
        return False
    elif num_iteration>50 :
        return True
    else:
        return test_lychrel(N,num_iteration+1)

# print(test_lychrel(349,1))


def compte_lych(n):
    somme=0
    for i in range(n):
        if test_lychrel(i,1):
            somme+=1
    return somme

# print(compte_lych(10000))


























