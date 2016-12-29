def urlify(input_str, max_len):
    return (input_str[:max_len].replace(' ', '%20'))

print urlify('Mr John Smith        ', 13)
