# len(283472934)

# TypeError: object of type 'int' has no len()

# Specific Error
try:
    len(283472934)
except TypeError as e:
    print("Type Hatası")
    print(e)

# For All Errors
try:
    len(283472934)
except Exception as e:
    print("Genel Hata")
    print(e)