def alt(s, t):
    if not (s and t):
        return s + t
    return s[0] + t[0] + alt(s[1:], t[1:])



if __name__ == "__main__":
    a="ab"
    b="zsd"
    print(alt(a,b))