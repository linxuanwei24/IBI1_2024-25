# read the original file
file = open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa" , "r")

all_lines = file.read()     # turn the file to a string
data = all_lines.split(">") # split the string to several elements

# there is a "3-->5" in the original file, so we need to modify what we just split
modification = data.index("YBL055C_mRNA cdna chromosome:R64-1-1:II:115573:116829:-1 gene:YBL055C gene_biotype:protein_coding transcript_biotype:protein_coding gene_symbol:YBL055C description:3'--")
data[modification] = data[modification] + ">" + data[modification + 1]
del data[modification + 1]

# create an empty file
with open("tata_genes.fa", "w", encoding="utf-8") as f:
    pass

for i in data:
    new_i = i.replace("\n" , "") # the DNA sequence in the original file has several rows, so we need to turn it to on row to detect the "TATAWAW" sequence
    if "TATAAAA" in new_i or "TATAAAT" in new_i or "TATATAA" in new_i or "TATATAT" in new_i:
        index1 = i.find("gene:")
        index2 = i.find("gene_biotype:")
        gene_name = ">" + i[index1 + 5 : index2 - 1] + "\n" # the gene name
        index3 = i.find("\n")
        seq = i[index3 + 1 :] # the sequence
        # store the information
        with open("tata_genes.fa" , "a" , encoding="utf-8") as f:
            f.write(gene_name)
            f.write(seq)