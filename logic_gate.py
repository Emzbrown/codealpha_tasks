print('Welcome to Emzy gate'
      )
gate = input(f"choose your gate ")
A = int(input(f"A = "))

B = int(input(f"B = "))

if gate == 'and':
    print(A*B)
if gate == 'or':
    if (A + B) >= 2:
        print('1')
    else:
        print(A+B)
if gate == "nand":
    if A*B == 1:
        print(0)
    else:
        print(1)
