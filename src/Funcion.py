def mayor(A,B,C):
    if A>B:
        if A>C:
            return A
        else:
            return C
    elif B>C:
        return B
    else:
        return C
