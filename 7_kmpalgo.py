def kmpcal(text, patt):
    patlen = len(patt)
    textlen = len(text)

    lps = [0] * patlen;

    lpscal(patt, lps)

    txtind = 0
    patind = 0
    while txtind < textlen:
        if text[txtind] == patt[patind]:
            txtind = txtind + 1
            patind = patind + 1

        if patind == patlen:
            print("Pattern matched at index", txtind - patind)
            patind = lps[patind - 1]

        if txtind < textlen and text[txtind] != patt[patind]:
            if patind != 0:
                patind = lps[patind - 1]
            else:
                txtind = txtind + 1


def lpscal(patt, lps):
    patlen = len(patt)

    lps[0] = 0;

    length = 0;
    i = 1

    while i < patlen:
        if patt[i] == patt[length]:
            length = length + 1
            lps[i] = length
            i = i + 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i = i + 1


text = input("Enter a text sample: ")
patt = input("Enter a pattern: ")

kmpcal(text, patt)
