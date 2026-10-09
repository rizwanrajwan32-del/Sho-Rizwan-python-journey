# SHO Rizwan - Tijori App
print("💰 TIJORI - Kharcha Hisab")
balance = 1500
print(f"Total: {balance} Rs")

chai = 50
nashta = 300
khana = 700

kharcha = chai + nashta + khana
bachat = balance - kharcha

print(f"Chai: {chai}, Nashta: {nashta}, Khana: {khana}")
print(f"Total Kharcha: {kharcha}")
print(f"Bachat: {bachat} Rs")

if bachat > 0:
    print("MASHALLAH Bachat ho gayi!")
else:
    print("Kharcha zyada ho gaya SHO Sahab!")
