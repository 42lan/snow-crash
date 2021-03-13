#Made by achiu-au (aka MaoKo)
_secret = "0123456"
def ft_des(message):
    strdup = [ord(code) for code in message]
    _0x18 = 0x00
    _0x1C = 0x00
    while (len(strdup) > _0x1C):
        if (_0x18 == 0x06):
            _0x18 = 0x00
        if (not (_0x1C & 0x01)):
            _0x10 = 0x00
            while (ord(_secret[_0x18]) > _0x10):
                strdup[_0x1C] -= 0x01
                if (strdup[_0x1C] == 0x1F):
                    strdup[_0x1C] = 0x7E
                _0x10 += 0x01
        else:
            _0x14 = 0x00
            while (ord(_secret[_0x18]) > _0x14):
                strdup[_0x1C] += 0x01
                if (strdup[_0x1C] == 0x7f):
                      strdup[_0x1C] = 0x20
                _0x14 += 0x01
        _0x1C += 0x01
        _0x18 += 0x01
    return ("".join([chr(code) for code in strdup]))
flags = {
    "flag00":               "I`fA>_88eEd:=`85h0D8HE>,D",
    "flag01":               "7`4Ci4=^d=J,?>i;6,7d416,7",
    "flag02":              "<>B16\\AD<C6,G_<1>^7ci>l4B",
    "flag03":               "B8b:6,3fj7:,;bh>D@>8i:6@D",
    "flag04":               "?4d@:,C>8C60G>8:h:Gb4?l,A",
    "flag05":               "G8H.6,=4k5J0<cd/D@>>B:>:4",
    "flag06":              "H8B8h_20B4J43><8>\\ED<;j@3",
    "flag07":               "78H:J4<4<9i_I4k0J^5>B1j`9",
    "flag08":              "bci`mC{)jxkn<\"uD~6%g7FK`7",
    "flag09":               "Dc6m~;}f8Cj#xFkel;#&ycfbK",
    "flag10":               "74H9D^3ed7k05445J0E4e;Da4",
    "flag11":               "70hCi,E44Df[A4B/J@3f<=:`D",
    "flag12":              "8_Dw\"4#?+3i]q&;p6 gtw88EC",
    "flag13":               "boe]!ai0FB@.:|L6l@A?>qJ}I",
}
for key, value in flags.items():
    print("{} = {} = {}".format(key, ft_des(value), value))
