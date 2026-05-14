# What is Anagram?
#
# Two strings are anagrams if:
#
# * same characters
# * same frequency
# * different order allowed


def group_anagram(words):

    anagram_map = {}

    for word in words:

        key = "".join(sorted(word))

        if key not in anagram_map:
            anagram_map[key] = []

        anagram_map[key].append(word)

    print(anagram_map)
    return list(anagram_map.values())



words = ["aet", "eat", "tea", "tan", "ate", "nat", "bat"]

print(group_anagram(words))