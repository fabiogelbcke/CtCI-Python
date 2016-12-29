def one_away(str1, str2):
    if abs(len(str1) - len(str2)) > 1:
        return False
    for i in range(len(str1)):
        if i >= len(str2) or str1[i] != str2[i]: # if a difference between the two is found
            insert = str2[i+1:] == str1[i:] # if something was inserted on str2 and that was the only change,
            #the substring after that is the same as the substring after the current char in str1
            replace = str2[i+1:] == str1[i+1:] # if a char is replaced and that is the only changed
            #substr after that is the same
            remove = str2[i:] == str1[i+1:] # yata yata yata
            return insert or replace or remove
    return True # if there is no difference they are the same and there are no changes

print one_away('pale', 'pale') #true
print one_away('pale', 'ple') #true
print one_away('pales', 'pale') #true
print one_away('pale', 'bale') #true
print one_away('a', '') #true
print one_away('pale', 'bake') #false
print one_away('fabio', 'faboi') #false

            
