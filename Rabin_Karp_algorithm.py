t = """Вместе шли они в сраженья через минные поля,
на узлах сопротивленья славу поровну деля.
Не страшили дождь и ночь их, и немало огневых
подавили они точек, не считая запятых.
Воевала дело зная та четверка храбрецов -
Иваненко, Иванбаев, Иванидзе, Иванов."""
p = "Иван"


def find_all_rabin_karp(text, pattern):
    result = []
    patternsum = sum(ord(s) for s in pattern)
    textwindowsum = sum(ord(text[j]) for j in range(len(pattern) - 1))
    for i in range(len(text) - len(pattern) + 1):
        textwindowsum += ord(text[i+len(pattern)-1])
        if patternsum == textwindowsum:
            if text.startswith(pattern, i):
                result.append(i)
        textwindowsum -= ord(text[i])
    return result
print(find_all_rabin_karp(t, p))
