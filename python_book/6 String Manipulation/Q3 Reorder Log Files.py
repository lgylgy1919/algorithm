# letter-log가 digit-log 보다 먼저 온다.
# 모든건 알파벳 순서

logs1 = ["dig1 8 1 5 1", "let1 art can",
         "dig2 3 6", "let2 own kit dig", "let3 art zero"]
logs2 = ["a1 9 2 3 1", "g1 act car",
         "zo4 4 7", "ab1 off key dog", "a8 act zoo"]


def orderingLog(logs):
    letter_log, digit_log = [], []
    for log in logs:
        if log.split()[1].isdigit():
            digit_log.append(log)
        else:
            letter_log.append(log)
    letter_log.sort(key=lambda x: (x.split()[1:], x.split()[0]))
    answer = letter_log + digit_log
    print(answer)
    return answer


orderingLog(logs1)
