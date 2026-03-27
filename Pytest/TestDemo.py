# Using pytest, here only 2 will get passes as we haven't used test in register name

# def register():
#     print('registering...')
# def test_login():
#     print('logging in...')
# def test_logout():
#     print('logging out...')
#
# register()
# test_login()
# test_logout()

class Test_Demo:
    def __init__(self):
        print("This is a constructor")
    def test_register(self):
        print('registering...')
    def test_login(self):
        print('logging in...')
    def test_logout(self):
        print('logging out...')
