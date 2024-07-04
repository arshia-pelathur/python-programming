def fibseq(n):
    if n==0:
        return 0
    elif (n==1) or (n==2):
        return 1
    else:
        return fibseq(n-1) + fibseq(n-2)

print([fibseq(i) for i in range(40)])