

def cumsum_and_erase(A, erase=None):
    sum = 0
    C = []
    B = []
    for i in range(len(A)):
        sum += A[i]
        C.append(sum)
    print(C)
    if erase != None:
        i = 0
        while erase in C:
            C.remove(erase)
            i += 1
    B = C
    return B

A = [5, 1, 4, 5, 14]
B = cumsum_and_erase(A, erase=10)
assert B == [5, 6, 15, 29], "Something is wrong! Please try again"



'''
text = ['122', '2342', '24 fef defe dew2dewf']



def process(sentences):
    for j in range(len(sentences)):
        s = [str(i) for i in sentences[j].split()]  # список со словами одного текста
        n = len(s)  # Длина списка s
        i = 0
        while i < n:
            if not(s[i].isalpha()):
                del s[i]
                i -= 1
            i += 1
            n = len(s)
        stroka = ''
        for i in range(len(s)):
            stroka += str(s[i]) + ' '
        sentences[j] = stroka[0:-1]
    result = sentences
    return result


print(process(text))

'''


'''

w = [1,3,1,2,1,1]
x = [0,3,2,6,1,9]
class Neuron:

    def __init__(self, w, f = lambda x: x):
        self.w = w
        self.f = f

    def forward(self, x):
        self.x = x
        s = 0
        for i in range(len(self.x)):
            s += self.x[i] * self.w[i]
        return self.f(s)

    def backlog(self):
        return self.x


n1 = Neuron(w)
print(n1.forward(x))
print(n1.backlog())

'''
