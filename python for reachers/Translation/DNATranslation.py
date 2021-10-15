inputfile = "DNA.txt"
f = open(inputfile,"r")
seq = f.read()
seq = seq.replace("\n", "") #Replace "\n" with "".
seq =seq.replace("\r", "") #Replace "\r" with "".