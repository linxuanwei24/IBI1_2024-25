splice = str(input("please input one of three possible splice donor/acceptor combinations (GTAG, GCAG, ATAC):"))
start = splice[:2]
stop = splice[2:]

# create an empty file
if splice == "GTAG":
    with open("GTAG_spliced_genes.fa", "w", encoding="utf-8") as f:
        pass
elif splice == "GCAG":
    with open("GCAG_spliced_genes.fa", "w", encoding="utf-8") as f:
        pass
elif splice == "ATAC":
    with open("ATAC_spliced_genes.fa", "w", encoding="utf-8") as f:
        pass

# read the original file
file = open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa" , "r")

all_lines = file.read()     # turn the file to a string
data = all_lines.split(">") # split the string to several elements

# there is a "3-->5" in the original file, so we need to modify what we just split
modification = data.index("YBL055C_mRNA cdna chromosome:R64-1-1:II:115573:116829:-1 gene:YBL055C gene_biotype:protein_coding transcript_biotype:protein_coding gene_symbol:YBL055C description:3'--")
data[modification] = data[modification] + ">" + data[modification + 1]
del data[modification + 1]

for i in data:
    index3 = i.find("\n")
    seq = i[index3 + 1 :] # the sequence
    seq = seq.replace("\n" , "") # the DNA sequence in one row
    index1 = seq.find(start)  
    index2 = seq.rfind(stop)
    # if no donor/acceptor found or only one found
    if index1 == -1 or index2 == -1 or index1 == index2:
        continue
    spliced_seq = seq[index1 : index2 + 2] # splice the sequence
    if "TATAAAA" in spliced_seq or "TATAAAT" in spliced_seq or "TATATAA" in spliced_seq or "TATATAT" in spliced_seq:
        index1 = i.find("gene:")
        index2 = i.find("gene_biotype:")
        gene_name = ">" + i[index1 + 5 : index2 - 1] + " " # the gene name
        counter = spliced_seq.count("TATAAAA") + spliced_seq.count("TATAAAT") + spliced_seq.count("TATATAA") + spliced_seq.count("TATATAT")
        counter = str(counter) + "\n"
        seq = seq + "\n"
        # store the information
        if splice == "GTAG":
            with open("GTAG_spliced_genes.fa" , "a" , encoding="utf-8") as f:
                f.write(gene_name)
                f.write(counter)
                f.write(seq)
        if splice == "GCAG":
            with open("GCAG_spliced_genes.fa" , "a" , encoding="utf-8") as f:
                f.write(gene_name)
                f.write(counter)
                f.write(seq)
        if splice == "ATAC":
            with open("ATAC_spliced_genes.fa" , "a" , encoding="utf-8") as f:
                f.write(gene_name)
                f.write(counter)
                f.write(seq)