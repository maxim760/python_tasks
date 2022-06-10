binars = (
    b'\x8fNQTR\xddZ\xa5j\xbf\xd4!\xaer5\xba\x90X\xbf\xeb\x93\xde6\x99\xee\xb8\x9d)'
    b'\x0e\x0f\xa5\xa9\xdc5\x008\xbf\xd8\xc7\xd2Kc\x8f\x08\xe5\xdf\xc6\x80'
    b'\xbd\xde\x9da>\xa7H\x8b\xbf\xbe~\xb7\xa2\xe6\x7f`?\xd7\xc2\xa0\xedW`h'
    b'\xbf\xe1\xe9\xee\x82\xd9b$\xbf\xdc\xe5\xd2\x19\xf3\xe3\xe8\xbf\xe9\xe2\\'
    b'\xde\xa9d\x1e\xbf\xdf\x01\x0b\xbam\xe4\\(\xe4?86H\xbe\xc1\x1d\xd9?^'
    b'3\xe0v\xda\xc6\x07i(\xcf\x13\x00\x00\x00\x02\x0002\x1f\xb9|NdMw\x89w\x83['
    b'\x12j%\xcb\x94PH\xf3\xff\xa63.')

binars2 = (
    b'\x8fNQTRYq2+\xbf\xeb\xe3\xd8\xf2<\x98nP\xbf\xea\xbe%\x8a\x0b\x9e\x96\xc0Z'
    b'\xbck\x8f\xa6\x8a&\x00H\xbf\xeb-\xca\xa9\xecu\x8a\x99\xa7Z\xb4\xbfc{;?\x00f/'
    b'\xbe\x1b\xfb\x96\xbe\xce.\xc8?G\xf6\xef\xbfA\x05\x18\xbf\xdf\xe5\x13'
    b'\x94\xd2M\xf0?\xe4\xcc)n\x197\x0e?\xd1\xeb;\xbe\xd5N\xa4\xbf\xed:BOyu2'
    b'?\xe3\xd8\xa2\x15\x9a\nP\xbf\xd7r\x9e\x84\xe3y4\xe3\\\xbem\xf1\x8d?h'
    b'\x07x\xbe\x02\xe3\xd360m\x0b\xde\x19\x83\x93\x00\x00\x00\x06\x000\x00\xdb;y'
    b'\xfbo\xc6\xf7Fe\xab\x12\xbcd0\xb3\xd8!!\xb67\x88\xfe\xa1')

import struct


def main(binars):
    fcount = binars[5::][binars[5::].index(b'\x00\x00\x00') + 3]
    fsymbols = "f" * fcount
    res = struct.unpack(f">IdbdQHdi{fsymbols}ddddddbBfffQIHhhhhhHhhQ",
                        binars[5::])
    A1 = res[0]

    B1 = res[1]
    B2 = res[2]
    B3 = res[3]
    B4 = res[4]

    D1_0 = res[8 + fcount]
    D2_0 = res[9 + fcount]
    D1_1 = res[10 + fcount]
    D2_1 = res[11 + fcount]
    D1_2 = res[12 + fcount]
    D2_2 = res[13 + fcount]

    C2 = res[14 + fcount]
    C3 = res[15 + fcount]
    C4 = list(res[16 + fcount:19 + fcount])
    C5 = res[19 + fcount]
    E1 = [res[x + 8] for x in range(fcount)]
    E2 = [res[x + 22 + fcount] for x in range(5)]
    E3 = res[27 + fcount]
    E4 = res[28 + fcount]
    E5 = res[29 + fcount]
    E6 = res[30 + fcount]

    B6 = res[6]
    B7 = res[7]

    tree = {
        "A1": A1,
        "A2": {
            "B1": B1,
            "B2": B2,
            "B3": B3,
            "B4": B4,
            "B5": {
                "C1": [
                    {
                        "D1": D1_0,
                        "D2": D2_0
                    },
                    {
                        "D1": D1_1,
                        "D2": D2_1
                    },
                    {
                        "D1": D1_2,
                        "D2": D2_2
                    },
                ],
                "C2":
                C2,
                "C3":
                C3,
                "C4":
                C4,
                "C5":
                C5,
                "C6": {
                    "E1": E1,
                    "E2": E2,
                    "E3": E3,
                    "E4": E4,
                    "E5": E5,
                    "E6": E6,
                },
            },
            "B6": B6,
            "B7": B7,
        }
    }

    return tree


main(binars)