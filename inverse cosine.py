import math
L = input("Enter length:")
D_Z = input("Enter Delta Zeta:")
L=int(L)
D_Z=int(D_Z)
answer = math.acos(L/math.sqrt(L**2+(D_Z)**2))

print(answer)
