
prefix ="192.168.95." 
num = 2
f=open("boron-MAC.info","r")
for line in f:
   if(line[0] == "b"):
      word = line.split()
      print("host"+ str(num)+"{" )
      print("   hardware ethernet " + word[1]+";" )
      print("   fixed-address " + prefix + str(num) +";")
      print("   option host-name \"eboron\"" +str(num) +";")
      print("   filename \"\prelinux.0\";")
      num+=1

print("}")
