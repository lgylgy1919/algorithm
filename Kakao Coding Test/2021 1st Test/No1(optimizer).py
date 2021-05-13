new_id1 = "...!@BaT#*..y.abcdefghijklm"  # "bat.y.abcdefghi"
new_id2 = "z-+.^."  # "z--"
new_id3 = "=.="  # "aaa"
new_id4 = "123_.def"  # "123_.def"
new_id5 = "Abcdefghijklmn.p"  # "abcdefghijklmn"


def solution(new_id):
    # 1단계 : 문자를 소문자로 모두 치환
    new_id = new_id.lower()

    # 2단계 : 알파벳 소문자, 숫자, ".", "_", "=" 제외 모두 제거
    for i in new_id:
        if (i.isalpha()) or (i.isdigit()) or (i in ["_", "-", "."]):
            answer.append(i)

    while ".." in answer:
        answer = answer.replace("..", ".")

    # 4단계 : "." 가 가장 앞이나 뒤에 있으면 제거
    if answer[0] == ".":
        answer = answer[1:] if len(answer) > 1 else "."
    if answer[-1] == ".":
        answer = answer[:-1]

    # 5단계 : 빈문자열이면 "a" 붙이기
    if answer == "":
        answer = "a"

    # 6단계 : 16자이상이면 15자 까지만, 나머진 버리기
    if len(answer) > 15:
        answer = answer[:15]
        if answer[-1] == ".":
            answer = answer[:-1]

    # 7단계 : 길이가 2자 이하면 길이가 3 될때까지 마지막 문자 반복 붙이기
    while len(new_ids) < 3:
        answer += answer[-1]

    return answer


solution(new_id4)