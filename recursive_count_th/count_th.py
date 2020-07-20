'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

##we are going to take a string and we have to check how many times it contains th
##case sensitive
##has to use recursion

def count_th(word):
    target = 'th'
    
    if len(word) < 2:
        return 0
    if word[0] + word[1] == target:
        return 1 + count_th(word[2:])
    else:
        return count_th(word[1:])

    

