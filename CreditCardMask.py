def maskify(cc):
    str1 = ''
    word_cut = ''
    
    if len(cc) >= 5:
        # slice the str by the index
        word_cut = cc[-4:]
        # Add as much of # as there is in the CC str
        count = len(cc) - len(word_cut)
        str1 = count * '#'
    
        return str1+word_cut
    return cc
