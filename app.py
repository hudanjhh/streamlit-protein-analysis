import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#title
st.title("Protein Analysis")

#input for uniprot ID
uniprot_id = st.text_input("Please insert the Uniprot ID")

#import characteristic.py functions
from characteristic import *

#calling functions for characteristics
uni_seq = get_uniprot_sequence(uniprot_id)
sequence = u_sequence(uni_seq)
seq_length = sequence_length(sequence)
aa_composition = amino_acid_composition(sequence)
mol_weight = molecular_weight(sequence)
iso_point = isoelectric_point(sequence)

