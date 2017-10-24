from django.test import TestCase

# Create your tests here.
a = 1
def test():
    global a
    a = 2

test()
print(a)