tempratures = [10,-20, -289, 100]
def c_to_f(c):
  if c<-273.15:
    return ""
  return c* 9/5 +32

def writeToFile(input):
    with open("output.txt","a") as file:
        file.write(input)

for temp in tempratures:
  writeToFile(str(c_to_f(temp)))
