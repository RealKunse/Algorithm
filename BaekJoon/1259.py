while True:
    inp = int(input())
    txt = list(str(inp))
    if inp == 0:
        break

    reverse_txt = list(txt)
    reverse_txt.reverse()
    # print(txt, reverse_txt)
    if txt != reverse_txt:
        print('no')
    else:
        print('yes')
