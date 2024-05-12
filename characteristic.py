import streamlit as st
from Bio import SeqIO
from Bio import ExPASy
# from Bio import PDB
from Bio.SeqUtils.ProtParam import ProteinAnalysis

# Retrieve protein sequence data from UniProt
def get_uniprot_sequence(uniprot_id):
    url = f"https://www.uniprot.org/uniprot/{uniprot_id}.fasta"
    response = ExPASy._open(url)
    record = SeqIO.read(response, "fasta")
    return record

def u_sequence(uni_seq):
    return(uni_seq.seq)

#get the protein name
def name(uni_seq):
    header = uni_seq.description
    protein_name = header.split("|")[2].split(" ")[0]
    st.write('Protein Name: ', protein_name)
    return protein_name

# Calculate the length of the protein sequence
def sequence_length(sequence):
    seq_length = len(sequence)
    st.write('Sequence length: ', seq_length)
    return seq_length

# Calculate the amino acid composition of the protein sequence
def amino_acid_composition(sequence):
    analysis = ProteinAnalysis(str(sequence))
    aa_composition = analysis.count_amino_acids()
    st.write('Amino Acid Composition: ', aa_composition)
    return aa_composition

# Calculate the molecular weight of the protein sequence
def molecular_weight(sequence):
    analysis = ProteinAnalysis(str(sequence))
    mol_weight = analysis.molecular_weight()
    st.write('Molecular Weight:  {:.2f}'.format(mol_weight), 'Da')
    return mol_weight

# Calculate the isoelectric point of the protein sequence
def isoelectric_point(sequence):
    analysis = ProteinAnalysis(str(sequence))
    iso_point = analysis.isoelectric_point()
    st.write('Isoelectric Point:  {:.2f}'.format(iso_point), 'pI')
    return iso_point