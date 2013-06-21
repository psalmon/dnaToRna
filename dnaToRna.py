f = open('seq.txt', 'r')			#open a file '/seq.txt' and convert it to uppercase
uppers = f.read()					#I try not to be perfect but a lowercase cost me a lot of time once!
f.close()
f = open('seq.txt', 'w')
f.write(uppers.upper())
f.close()
f = open('seq.txt', 'r')
t = f.read()						#our dna string 't'. At most 1000 nt
u = ""								#our rna string 'u'. initialized null.
f.close()

for i in t:							#do the replacement if necessary
	if (i == 'T'):
		u += 'U'
	else:
		u += i

print (u)
print ("writing to new file 'rnaSEQ'...")
rnaSeq = open('rnaSEQ.txt', 'w')
rnaSeq.write(u)
print ("done.")