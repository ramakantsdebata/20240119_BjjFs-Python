class IntType:
    pass

class SpecialIntType(IntType):
    pass

it = IntType()
st = SpecialIntType()

print(isinstance(it, IntType))
print(isinstance(st, IntType))
print(isinstance(it, SpecialIntType))
print(isinstance(st, SpecialIntType))

print(issubclass(SpecialIntType, IntType))
print(issubclass(IntType, SpecialIntType))
