sentence = "Cracking the coding interview"


# new = sentence.split()
# string = ''
#
# while len(new)-1:
#     string += new.pop(-1)+" "
# print(string+new[0])

def reverse_word(string, st, e):
    while st < e:
        string[st], string[e] = string[e], string[st]
        st += 1
        e -= 1


start = 0
s = list(sentence)
while True:
    try:
        end = s.index(' ', start)
        reverse_word(s, start, end - 1)
        start = end + 1
    except ValueError:
        reverse_word(s, start, len(s) - 1)
        break

s.reverse()

print(''.join(s))


