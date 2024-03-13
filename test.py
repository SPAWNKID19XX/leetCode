class A:
    def add_a(self, s,f,l=[]):
        for x in range(s,f):
            l.append(str(x))

    def print_a(self):
        l = []
        self.add_a(1,3,l)
        print(l)
        self.add_a(5,8,l)
        return ' '.join(l)
    
a = A()
print(a.print_a())