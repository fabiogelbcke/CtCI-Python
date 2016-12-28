def compress(var):
    if len(var) == 0:
        return var
    last_char = var[0]
    char_count = 0
    compressed_str = ''
    for i in range(len(var)):
        if var[i] == last_char:
            char_count += 1
        if var[i] != last_char or i == len(var) - 1:
            compressed_str += last_char
            compressed_str += str(char_count)
            last_char = var[i]
            char_count = 1
    return compressed_str if len(var) > len(compressed_str) else var
            
print compress('abcdef')
