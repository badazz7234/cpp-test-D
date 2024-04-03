x=0
abu_salim= "+"
y=0
z="ANSWER: "
nathan=input().split(" ")
x= nathan[0]
abu_salim=nathan[1]
y=nathan[2]


if abu_salim == "+":
    print(z + str(int(x) + int(y)))
elif abu_salim == "-":
    print(z + str(int(x) - int(y)))
elif abu_salim == "*":
    print(z + str(int(x) * int(y)))
elif abu_salim == "/":
    print(z + str(int(x) // int(y)))

else:
    print("NO ANSWER NIGGA")
