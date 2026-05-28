class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password)<8:
            return False

        for i in range(len(password) - 1):
            if password[i]==password[i + 1]:
                return False

        count_u=0
        count_l=0
        count_s=0
        count_d=0

        chars="!@#$%^&*()-+"

        for i in password:
            if i.isupper():
                count_u+=1
            if i.islower():
                count_l+=1
            if i.isdigit():
                count_d+=1
            if i in chars:
                count_s+=1

        return count_u>0 and count_l>0 and count_s>0 and count_d>0