class account:
    def check_password_length(self, passwd):
        if len(passwd) > 8:
            return True
        else:
            return False

if __name__ == '__main__':
    accVerify = account()
    print(accVerify.check_password_length('hellodoctor'))

