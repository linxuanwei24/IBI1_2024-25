# the code will not go on unless you input the sequence correctyl
# example
# the DNA sequence is "AGGCCTTCACCTGCCTTACC"
# the recognized_sequence is "GCCT"
# the out put is "The restriction enzyme cut sites are: [3, 13]."


# input the DNA sequence and check whether the input is correct(AGCT)
def input_DNA():
    DNA_sequence = str(input("please input the DNA sequence:"))
    if set(DNA_sequence) <= {"A" , "G" , "C" , "T"}:
        return DNA_sequence
    else:
        print('Error! Please make sure the sequence contains only canonical("A" "G" "C" "T") nucleotides.')
        return input_DNA()
DNA_sequence = input_DNA()

# input the recognized sequence and check the input
def input_recognized():
    recognized_sequence = str(input("please input the sequence recognised by the restriction enzyme:"))
    if set(recognized_sequence) <= {"A" , "G" , "C" , "T"}:
        return recognized_sequence
    else:
        print('Error! Please make sure the sequence contains only canonical("A" "G" "C" "T") nucleotides.')
        return input_recognized()
recognized_sequence = input_recognized()

def position(DNA_sequence):
    if recognized_sequence not in DNA_sequence:
        print("Positions not found!")
    else:
        index = 0
        index_list = []
        while index != -1:
            index = DNA_sequence.find(recognized_sequence)
            if index != -1:
                index_list.append(index + 1)
                DNA_sequence = DNA_sequence[:index] + "a" + DNA_sequence[index + 1:]
        return index_list
       
print(f"The restriction enzyme cut sites are: {position(DNA_sequence)}.")