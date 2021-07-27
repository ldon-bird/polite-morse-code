# ch = []
# for i in range(ord('a'), ord('z')+1):
#     ch.append(chr(i))
# # print(ch)

# morse = ['01','1000','1010','100','0','0010','110',
#         '0000','00','0111','101','0100','11','10',
#         '111','0110','1101','010','000','1','001',
#         '0001','011','1001','1011','1100']


# cm = dict()
# for i in range(26):
#     cm[ch[i]] = morse[i]
# print(cm)
cm = {'a': '01', 'b': '1000', 'c': '1010', 'd': '100', 'e': '0', 'f': '0010', 'g': '110', 'h': '0000', 'i': '00', 'j': '0111', 'k': '101', 'l': '0100', 'm': '11', 'n': '10', 'o': '111', 'p': '0110', 'q': '1101', 'r': '010', 's': '000', 't': '1', 'u': '001', 'v': '0001', 'w': '011', 'x': '1001', 'y': '1011', 'z': '1100'}
mystring = input()

ch0 = '·'
ch1 = '-'
spcr = ' '

for char in mystring:
    if char == ' ':
        print(spcr,end = '')
        print(spcr,end = '')
        print(spcr,end = '')
    else:
        for c in cm[char]:
            if c == '0':
                print(ch0,end = '')
            elif c =='1':
                print(ch1,end = '')
        print(spcr,end = '')
