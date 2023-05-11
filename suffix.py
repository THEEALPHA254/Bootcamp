#prints the longest most common suffix in a llist of strings
def longestComnSuffix(strs):
    comn_suffix = strs[0]
    for next_word in strs[1:]:
        while not next_word.endswith(comn_suffix):
            comn_suffix = comn_suffix[1:]
    return comn_suffix

print(longestComnSuffix(['education', 'attention', 'convocation', 'reveletion']))