a = input("Type some words!: ")
c = a.split()


def backwards_typing():
    e =   c[-1::-1]
    d = ' '
    d = d.join(e)
    return print(d)


backwards_typing()


