generator = int(input("Enter generator: "))
target = int(input("Enter target: "))
prime = int(input("Enter prime: "))
expo = 0

while True:
    if (generator ** expo) % prime == target:
        print("Found expoent: ", expo)
        break
        
    expo+=1