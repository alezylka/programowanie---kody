"""
@source: https://www.biostars.org/p/315732/
"""

import pandas as pd
from Bio import SeqIO

output_handle1 = open("new_fasta1.fasta", "a")
output_handle2 = open("new_fasta2.fasta", "a")

records1 = SeqIO.index("fasta1.fasta", "fasta")
records2 = SeqIO.index("fasta2.fasta", "fasta")

candidate_df=pd.read_csv("dispatch.csv",sep='\t')

for i in candidate_df['Seq_1.id']:
    if i in records1:
        SeqIO.write(records1[i], output_handle1, 'fasta')
    elif i in records2:
        SeqIO.write(records2[i], output_handle1, 'fasta')

for i in candidate_df['Seq_2.id']:
    if i in records1:
        SeqIO.write(records1[i], output_handle2, 'fasta')
    elif i in records2:
        SeqIO.write(records2[i], output_handle2, 'fasta')

records = SeqIO.index("your_file.fasta", "fasta")
print(len(records))