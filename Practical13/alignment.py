# import the BLOSUM62
from Bio.Align import substitution_matrices
matrix = substitution_matrices.load("BLOSUM62")

# read the file
file1 = open("P04179.fasta" , "r")
file2 = open("P09671.fasta" , "r")
file3 = open("random.fasta" , "r")
file1 = file1.read()
file2 = file2.read()
file3 = file3.read()

# find the name and the sequnce of the mRNA
index1 = file1.find("\n")
index2 = file2.find("\n")
index3 = file3.find("\n")
name1 = "P04179"
name2 = "P09671"
name3 = "the random protein"
seq1 = file1[index1:]
seq1 = seq1.replace("\n" , "")
seq2 = file2[index2:]
seq2 = seq2.replace("\n" , "")
seq3 = file3[index3:]
seq3 = seq3.replace("\n" , "")
print(name1 + "\n" + seq1)
print(name2 + "\n" + seq2)

# initialize the score
score12 = 0
score13 = 0
score23 = 0
num12 = 0
num13 = 0
num23 = 0

for i in range(222):
    if seq1[i] == seq2[i]:
        num12 += 1
    if seq1[i] == seq3[i]:
        num13 += 1
    if seq2[i] == seq3[i]:
        num23 += 1
    
    # workflow: Compare the first amino acid in the two sequence -> Add the score according to the BLOSUM62 -> Compare the second amino acid -> Add the score ...
    score12 += matrix[seq1[i]][seq2[i]]
    score13 += matrix[seq1[i]][seq3[i]]
    score23 += matrix[seq2[i]][seq3[i]]

print(f"The percentage of identical amino acids of {name1} and {name2} is {round(num12/222*100 , 1)}%.")
print(f"The percentage of identical amino acids of {name1} and {name3} is {round(num13/222*100 , 1)}%.")
print(f"The percentage of identical amino acids of {name2} and {name3} is {round(num23/222*100 , 1)}%.")
print(f"The alignment score of {name1} and {name2} is {score12}.")
print(f"The alignment score of {name1} and {name3} is {score13}.")
print(f"The alignment score of {name2} and {name3} is {score23}.")