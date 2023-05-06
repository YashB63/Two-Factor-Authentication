import time
import pyotp
import qrcode

#key = pyotp.random_base32()

key = "YashSuperSecretKey"

#------------------------ Generate OTP --------------------------------

# totp = pyotp.TOTP(key)

# print(totp.now())

# # time.sleep(30)

# # print(totp.now())


# input_code = input("Enter 2 FA Code:")

# # code = totp.now()
# # print(input_code == code)

# print(totp.verify(input_code))

counter = 0

hotp = pyotp.HOTP(key)

print(hotp.at(0))
print(hotp.at(1))
print(hotp.at(2))
print(hotp.at(3))
print(hotp.at(4))

for _ in range (5):
    print(hotp.verify(input("Enter Code: "), counter))
    counter += 1
    
#----------------Generate QR code------------

# uri = pyotp.totp.TOTP(key).provisioning_uri(name="AhamBrahmasmi63",
#                                             issuer_name="Yash App")

# print(uri)

# qrcode.make(uri).save("totp.png")

#-----------------------------------------------------------------

# totp = pyotp.TOTP(key)
# print(totp)

# while True:
#     print(totp.verify(input("Enter code:")))
