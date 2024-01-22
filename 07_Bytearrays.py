str1 = "Python"
print("\n Str Type->", type(str1), id(str1))

# Convert to bytes
dataBytes = str1.encode(encoding="utf-8")
print("\n dataBytes Type->", type(dataBytes), dataBytes)

# Decode it back
str2 = dataBytes.decode(encoding="utf-8")
print("\n Str Type->", type(str2), id(str2), str2)
