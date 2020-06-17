def lite(x):
    if x.startswith("#"):
        x=x[1:len(x)]
    v=[eval(f"0x{x[0:2]}"),eval(f"0x{x[2:4]}"),eval(f"0x{x[4:6]}")]
    v=sum(v)
    return (v,f"#{x}")
def srt(l):
    o=[]
    for i in l:
        o.append(lite(i))
    o=sorted(o, key=lambda x: x[0])
    oo=[]
    for t in o:
        oo.append(t[1])
    print(f"{'-'*75}\nlinear-gradient(90deg, {oo[0]} 0% 12.5%, {oo[1]} 12.5% 25%, {oo[2]} 25% 37.5%, {oo[3]} 37.5% 50%, {oo[4]} 50% 62.5%, {oo[5]} 62.5% 75%, {oo[6]} 75% 87.5%, {oo[7]} 87.5% 100%)\n{'-'*75}")
def init(s):
    srt([s[23:30],s[41:48],s[60:67],s[79:86],s[98:105],s[117:124],s[136:143],s[155:162]])
init("linear grad to be sorted")