import time
print("seconds remain")
for i in range (12):
    print(str(12-i)+"\r",end="")
    time.sleep(1)
print("time is up")  