class Emp:
    def __init__(self, id, nm, bs):
        self.eid = id
        self.ename = nm
        self.basic = bs

    def __str__(self):
        return str(self.eid) + "," + self.ename + "," + str(self.basic)
