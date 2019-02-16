x=['blue','red','green']
print("Our color list:")
print(x)
y=str(input("Enter a new color:"))
z=y.split(",")
x.extend(z)
print("Our new color list:")
print(x)