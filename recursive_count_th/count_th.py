'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    if word.find("th") == -1:
        return 0

    if "th" in word:
        index = word.find("th") + 2
        return 1 + count_th(word[index:])

