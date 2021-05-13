new_id1 = "...!@BaT#*..y.abcdefghijklm"  # "bat.y.abcdefghi"
new_id2 = "z-+.^."  # "z--"
new_id3 = "=.="  # "aaa"
new_id4 = "123_.def"  # "123_.def"
new_id5 = "Abcdefghijklmn.p"  # "abcdefghijklmn"


def solution(new_id):
    # 1단계 : 문자를 소문자로 모두 치환
    new_id = new_id.lower()

    # for 함수 사용 위해 리스트로 치환
    new_id = list(new_id)
    new_ids = []

    # 2단계 : 알파벳 소문자, 숫자, ".", "_", "=" 제외 모두 제거
    for i in new_id:
        if (i.isalpha()) or (i.isdigit()) or (i == "_") or (i == "-") or (i == "."):
            new_ids.append(i)

    new_ids = "".join(new_ids)
    while ".." in new_ids:
        new_ids = new_ids.replace("..", ".")

    new_ids = list(new_ids)
    # 4단계 : "." 가 가장 앞이나 뒤에 있으면 제거
    if new_ids[0] == ".":
        del new_ids[0]

    if len(new_ids) >= 1 and new_ids[-1] == ".":
        del new_ids[-1]

    # 5단계 : 빈문자열이면 "a" 붙이기
    if len(new_ids) == 0:
        new_ids.append("a")

    # 6단계 : 16자이상이면 15자 까지만, 나머진 버리기
    if len(new_ids) >= 16:
        new_ids = new_ids[0:15]

    # 6-1단계 : 마지막 문자 '.' 이면 제거
    if new_ids[-1] == ".":
        del new_ids[-1]

    # 7단계 : 길이가 2자 이하면 길이가 3 될때까지 마지막 문자 반복 붙이기
    while len(new_ids) <= 2:
        new_ids.append(new_ids[-1])

    answer = "".join(new_ids)
    return answer


solution(new_id4)