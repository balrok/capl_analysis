class Variable(object):
    def __init__(self, f, r):
        self.type = ''
        self.name = ''
        self.init = ''
        self.full = f
        self.initialized = False
        self.used = False
        self.used_without_init = False
        self.raw = r
    def setInit(self,i):
        self.init = i
        self.initialized = True
    def setUsed(self):
        self.used = True
        if not self.initialized:
            self.used_without_init = True
    def print(self):
        print("t:%s n:%s i:%s f:%s" % (self.type, self.name, self.init, self.full))
    def print_raw(self):
        print(self.raw)

class Function(object):
    def __init__(self, f, r, rh):
        self.vars = []
        self.full = f
        self.type = ''
        self.name = ''
        self.used = False
        self.raw = r
        self.raw_head = rh
    def setUsed(self):
        self.used = True
    def print(self):
        print("t:%s n:%s" % (self.type, self.name))
        for v in self.vars:
            print("   ", end="")
            v.print()
    def print_header(self):
        print(self.raw_head)
    def print_raw(self):
        print(self.raw)
