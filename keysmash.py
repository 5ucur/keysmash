import random as r

abcd = "abcdefghijklmnopqrstuvwxyz"
trow = "qwertyuiop"
mrow = "asdfghjkl"
brow = "zxcvbnm"

def encode_multiple(string, row=mrow, return_lists=False):
    '''Encodes string using row. Preserves non-alphabet characters. Does not
preserve case. Enable return_lists to return a nested list instead of continuous
text.'''
    string = string.casefold()
    if len(string) == 1:
        return encode(string, row)
    else:
        full = []
        code = []
        word = []
        symb = []
        for character in string:
            if character not in abcd:
                if word:
                    encoded = encode(''.join(word), row)
                    full.append(encoded[0])
                    code.append(encoded[1])
                    word = []
                symb.append(character)
            else:
                if symb:
                    full.append(''.join(symb))
                    code.append(''.join(symb))
                    symb = []
                word.append(character)
        if word:
            encoded = encode(''.join(word), row)
            full.append(encoded[0])
            code.append(encoded[1])
        if symb:
            full.append(''.join(symb))
            code.append(''.join(symb))
        if return_lists:
            return full, code
        else:
            return ''.join(full), ''.join(code)

def decode_multiple(encoded, code, in_lists=False):
    '''Decodes encoded using code. Enable in_lists if working on a nested list
instead of continuous text.'''
    if len(encoded) == 1:
        return decode(encoded, code)
    if in_lists:
        full = []
        word = []
        code_part = []
        symb = []
        for character, decoder in zip(encoded, code):
            if character not in abcd:
                if word:
                    full.append(decode(''.join(word), ''.join(code_part)))
                    word = []
                    code_part = []
                symb.append(character)
            else:
                if symb:
                    full.append(''.join(symb))
                    symb = []
                word.append(character)
                code_part.append(decoder)
        if word:
            full.append(decode(''.join(word), ''.join(code_part)))
        if symb:
            full.append(''.join(symb))
        return ''.join(full)
    else:
        full = []
        word = []
        symb = []
        for string, decoder in zip(encoded, code):
            if string[0] not in abcd:
                full.append(string)
            else:
                full.append(decode(''.join(string), decoder))
        return ''.join(full)

def encode(string, row=mrow):
    '''Encodes string into a keysmash in row. Does not preserve case. Strictly
works only on strings containing only the letters a-z. The row is by default
mrow (middle row), options are also trow and brow.'''
    string = string.casefold()
    if len(string) == 1:
        smash = r.choice(row)
        diff = ord(string) - ord(smash)
        code = abcd[diff]
    else:
        smash = ''.join([r.choice(row) for _ in range(len(string))])
        diff = [ord(o) - ord(n) for o,n in zip(string,smash)]
        code = ''.join([abcd[key] for key in diff])
    return smash, code

def decode(string, code):
    '''Decodes string using code. Strictly works only on strings containing only
the letters a-z.'''
    string = string.casefold()
    if len(string) == 1:
        if (code := abcd.index(code)) < 25 - abcd.index(string):
            return chr(ord(string) + code)
        else:
            return chr(ord(string) + (code - 26))
    else:
        decode = []
        text = []
        for a,b in zip(string, code):
            if (element := abcd.index(b)) < 25 - abcd.index(a):
                decode.append(element)
            else:
                decode.append(element - 26)
        for a,b in zip(string, decode):
            text.append(chr(ord(a) + b))
        return ''.join(text)

if __name__ == "__main__":
    smash, code = encode_multiple(input("Enter text: "))
    print(f'''Encoded:    {smash}
Code:       {code}''')
    print(f'Decoded:    {decode_multiple(smash, code)}')
