# PYTHON GST CALCULATOR

cp = float(input("Enter Cost Price: "))
gp = float(input("Enter GST Percent: "))

net = cp+(gp*cp)/100

print("Amount without GST:", cp)
print("Amount including GST:", net)