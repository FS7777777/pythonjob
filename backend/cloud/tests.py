class test():
    name="xiaohua"
    def run(self):
        return "HelloWord"
t=test()
print (getattr(t, "name",None))