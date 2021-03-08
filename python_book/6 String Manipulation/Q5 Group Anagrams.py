import collections

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]


def group_anagrams(strs):
    anagrams = collections.defaultdict(list)
    print(anagrams)

    for word in strs:
        anagrams[''.join(sorted(word))].append(word)
        print(anagrams)

    print(anagrams)
    print(anagrams.values())
    return anagrams.values()


group_anagrams(strs)
