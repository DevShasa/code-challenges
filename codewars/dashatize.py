def dashatize(n):
    '''
    Given a variable n,

    If n is an integer, Return a string with dash'-'marks before and after each odd integer, 
    but do not begin or end the string with a dash mark. If n is negative, 
    then the negative sign should be removed.

    If n is not an integer, return an empty value.

    Example
    dashatize(274) -> '2-7-4'
    dashatize(6815) -> '68-1-5'
    '''
    if (type(n) == int):

        outstr = ''
        for x in str(abs(n)):
            if (int(x) % 2) != 0:
                outstr += f'-{x}-'
            else:
                outstr += x
        
        if outstr[0] == "-":
            outstr = outstr[1:]

        if outstr[len(outstr)-1] == "-":
            outstr = outstr[:-1]

        return outstr.replace("--", '-')
    
    return "None"


print(dashatize(274)) # should be 2-7-4
print(dashatize(5311)) # 5-3-1-1
print(dashatize(86320)) # 86-3-20
print(dashatize(227474)) # 22-7-4-7-4
print(dashatize(974302)) # 9-7-4-3-02
print(dashatize(-1)) # 1
print(dashatize(None)) # None
print(dashatize("")) # None





