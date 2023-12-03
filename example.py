import pandas as pd

# Load and show labeled data
labeled_data = pd.read_hdf('data/labeled_data_embed.h5')

print(labeled_data)

# Load nolabel data
nolabel_data = pd.read_hdf('data/nolabel_data_embed.h5')

print(nolabel_data)