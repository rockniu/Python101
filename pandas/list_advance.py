class person(object):

    name="Undefine"

    def person(self):
        pass

    def person(self, nm, ag):
        self.name=nm
        self.age=ag

    def __repr__(self):
        return self.name

list =[person() for i in range(10)]

print (list)