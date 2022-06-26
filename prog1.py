def prog_1(str, max_l):
    mas = str.split()
    max_len = int(max_l)
    res = []
    for el in mas:
        el_len = len(el)
        if el_len < max_len:
            el = el + '*' * (max_len - el_len)
        res.append(el)
    res = ' '.join(res)
    return res

if __name__ == '__main__':
    sent = input('Enter data:')
    if len(sent) == 0:
        print("No data.")
    max_l = input('Enter max length:')
    print(prog_1(sent, max_l))
    input()