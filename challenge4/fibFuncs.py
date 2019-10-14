# copied from w3schools


def fibLooping(n):
    if n <=1:
        return n
    else:
        return fibLooping(n - 1) + fibLooping(n - 2)
