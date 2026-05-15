def decode_string(s: str) -> str:
    stack = []
    num_stack = []
    current = ""
    num = 0
    
    for ch in s:
        if ch.isdigit():
            num = num * 10 + int(ch)  # 여러 자릿수 처리
        elif ch == '[':
            stack.append(current)     # 현재 문자열 저장
            num_stack.append(num)     # 반복 횟수 저장
            current = ""              # 리셋
            num = 0
        elif ch == ']':
            prev = stack.pop()
            multi = num_stack.pop()
            current = prev + current * multi  # 바깥 + 안쪽*횟수
        else:
            current += ch
    
    return current