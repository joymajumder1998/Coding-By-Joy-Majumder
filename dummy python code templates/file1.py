with open("input.txt","r") as f:
	s=f.read()
f.close
with open("output.txt","w") as f:
	f.write(s)
f.close
