import h5py
import numpy as np

with h5py.File('filtered_feature_bc_matrix-2.h5', 'r') as f:
    data = f['default']
    print(data)
    print(f)