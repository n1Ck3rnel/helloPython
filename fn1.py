def fn():
    print("fn called")

fn()

def get_fruits():
	return ['오렌지', '사과', '바나나']

print(get_fruits()[0])


def var_param(a, *vp):
    print(type(vp))
    print(a, len(vp), vp[len(vp) -1])

var_param(1,2,3)

def plus(a,b):
    return a+b

s = '3 + 4'
if '+' in s:
    a = s.split('+')
    b = [ int(i.strip()) for i in a]
    # print(b)
    print(plus(b[0], b[1]))
    


