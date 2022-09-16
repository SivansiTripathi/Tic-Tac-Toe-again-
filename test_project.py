from project import register, home, gainAccess, welcome

def test_register():
    assert register("enter a username-") == "Sivansi"
    assert register("enter a password") == "Sivansi88"
    assert register("confirm password") == "Sivansi88"
def test_home():
    assert home("welcome, please select an option") == "login"
    assert home("login") == gainAccess
def test_gain_access():
    assert gainAccess("enter a username") == "Sivansi"
    assert gainAccess("enter a password") == "Sivansi88"
def test_welcome():
    assert welcome("let'splay tic tac toe") 
