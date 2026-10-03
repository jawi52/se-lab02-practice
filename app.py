print('Welcome to Software Engineering Lab 02')

def login(email, password, two_factor=False):
    if two_factor:
        return 'Login with 2FA successful for ' + email
    return 'Login successful for ' + email
