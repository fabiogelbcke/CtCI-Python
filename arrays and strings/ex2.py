from collections import Counter

def check_permutation(str1, str2):
    return (Counter(str1) == Counter(str2))

print check_permutation('fabio schubert gelbcke', 'fabio schubert gelbcke') #true
print check_permutation('fabio', 'oifab') #true
print check_permutation('fabio', 'oiofab') #false
