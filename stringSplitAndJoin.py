
#s = 'My name is Shirantha'

#s = s.split (' ')                  # s = ['My', 'name', 'is', 'Shirantha']

#s = "+".join(s)                    # My+name+is+Shirantha

def splitAndJoin (text) :
    text = text.split (' ')
    text = '-'.join (text)

    return text

s = input ()

res = splitAndJoin (s)
print (res)