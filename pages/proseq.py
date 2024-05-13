import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
#import characteristic.py functions
from characteristic import *
#import ppi.py function
from ppi import *

#title
st.title("Protein Analysis using Protein Sequences")

if st.button("Use UniProt ID as Input"):
    st.switch_page("app.py")

#input for uniprot ID
protein_seq = st.text_input("Please insert the Protein Sequences")

#check the input for any non protein character
non_protein_pattern = re.compile(r'[^ACDEFGHIKLMNPQRSTVWY]')

if non_protein_pattern.search(protein_seq):
    check = True
    st.warning("Input contains non protein character(s). Please insert another Protein Sequence.", icon="🚨")
else:
    check = False

if protein_seq:
    if check == False:
        #call functions for characteristics
        seq_length = sequence_length(protein_seq)
        aa_composition = amino_acid_composition(protein_seq)
        mol_weight = molecular_weight(protein_seq)
        iso_point = isoelectric_point(protein_seq)

        st.divider()

else:
    st.warning('Please insert the Protein Sequences :sunglasses:')