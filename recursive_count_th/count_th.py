'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    recurse_count = 0
    # count = 0
    # i = 0
    # j = 1

    # while i < len(word) - 1:
    #     while j < len(word):
    #         if word[i] == 't' and word[j] == 'h':
    #             count += 1

    # return count

    if len(word) < 2:
        return 0
    else:
        if word[len(word) - 1] == 'h' and word[len(word) - 2] == 't':
            return count_th(word[:-2]) + 1
        else:
            return count_th(word[:-1])

    # TBC
