def plain(r):
    l = len(r)-1
    s = 0
    while s < l:
        if r[s] != r[l]:
            return False
        s += 1
        l -= 1
    return True
r = (1, 2, 3, 3, 2, 1)
if plain(r):
    print('it is a palindrome.')
else:
    print('it is not a palindrome.')