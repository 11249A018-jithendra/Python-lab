class Check:
    def check_palindrome(self, data):
        s = str(data)
        return s == s[::-1]
obj = Check()
print(obj.check_palindrome("wow"))
print(obj.check_palindrome("18"))
