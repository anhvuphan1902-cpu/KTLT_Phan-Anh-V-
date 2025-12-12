print("Sinh vien:Phan Anh Vu")
print("Ma so SV : 245751030310014")
print("###########################")
###################################
class Nguoi(object):
    def getGender(self):
        return "Unknown"

class Nam(Nguoi):
    def getGender(self):
        return "Nam"

class Nu(Nguoi):
    def getGender(self):
        return "Nữ"

# Test
aNam = Nam()
aNu = Nu()

print(aNam.getGender())  # Nam
print(aNu.getGender())   # Nữ
