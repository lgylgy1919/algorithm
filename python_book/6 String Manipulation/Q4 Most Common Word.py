import collections
import re

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

text = re.sub(r'[^\w]', ' ', paragraph)
# 정규식 : re.sub(조건, 대체, 대상) : 조건에 해당하는 항목을 대체어로  SUBstitude 한다.
# Bob hit a ball  the hit BALL flew far after it was hit


def most_common_word(paragraph, banned):

    words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
             .lower().split()
             if word not in banned]

    counts = collections.Counter(words)
   # Counter({'ball': 2, 'bob': 1, 'a': 1, 'the': 1, 'flew': 1, 'far': 1, 'after': 1, 'it': 1, 'was': 1})

    print(counts.most_common(2))
    #[('ball', 2), ('bob', 1)]
    return counts.most_common(1)[0][0]


most_common_word(paragraph, banned)
