with open("C:\\Users\\STICI\Desktop\\Input.txt", "r", encoding="utf-8") as f:
	a=f.read()
print("NR\tNume\t\tPrenume\t\tNota1\tNota2\tNota3")
print(a) # punctul a)afisarea continutului fisierului pe ecran

with open ("C:\\Users\\STICI\Desktop\\Rezerva.txt", "w", encoding="utf-8") as f:
	f.write(a)

with open ("C:\\Users\\STICI\Desktop\\Output.txt", "w", encoding="utf-8") as f:
	for i in a.rstrip().split("\n"):
		camp=i.split()
		for i in camp:
			sum=float(camp[3]) + float(camp[4]) + float(camp[5])
			med=round((sum/3), 3)
		f.write("\t\t".join(camp[0:3]) +"\t\t"+ str(med) + "\n")