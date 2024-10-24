def decode(code):
    new_code = ""
    for digit in range(len(code)):
        if code[digit] >= 3:
            new_code += str(int(code[digit]) - 3)
        else:
            new_code += str(int(code[digit]) + 7)
    return new_code