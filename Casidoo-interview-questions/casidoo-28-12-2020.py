

def find2020(string2020):
    z = list(string2020)
    for x in range(0, len(z)-1):
        is_2020 = z[x]+z[x+1]+z[x+2]+z[x+3]
        if is_2020 == '2020':
            return x
    return -1


# Activating the function
print(find2020('222000020222002020'))
