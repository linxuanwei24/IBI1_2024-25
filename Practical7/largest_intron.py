seq = 'ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA'

index1 = seq.find("GT")  # the index of the first "GT"
index2 = seq.rfind("AG") # the index of the last "AG"

seq = seq[index1 : index2 + 2] # splice the sequence
print("The largest intron is :" , seq)
print("The lens of the intron is:" , len(seq))