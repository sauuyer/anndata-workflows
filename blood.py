import scirpy
import sys
import scirpy as ir
import scanpy as sc
from glob import glob
import pandas as pd
import tarfile
import anndata
import warnings
import numpy as np
from numba import NumbaPerformanceWarning

##### GENERAL IMPORTS AND CONFIG FOR BOTH BLOOD AND TUMOR

# ignore numba performance warnings
warnings.filterwarnings("ignore", category=NumbaPerformanceWarning)

# suppress "storing XXX as categorical" warnings.
anndata.logging.anndata_logger.setLevel("ERROR")
print('done line 18')

# Load the TCR blood data
adata_tcr = ir.io.read_10x_vdj("filtered_contig_annotations.csv")

# Load the associated blood transcriptomics data
adata = sc.read_10x_h5("filtered_feature_bc_matrix-2.h5")

print('done line 30. data imported')
print('adata_tcr.shape = ', adata_tcr.shape)
print('adata.shape = ', adata.shape)


######### BLOOD
### merging
#blood
ir.pp.merge_with_tcr(adata, adata_tcr)
adata.var_names_make_unique()

### import the subset from excel
subset = pd.read_csv('csvsubset02420_metgoednamen.csv')
#print('subset.head() \n', subset.head())
# Here take out only the barcode column and make into list
blood_subset_list = subset['barcode.'].tolist()
print('this is col_one_list')
print(blood_subset_list)

print("**********")
print('begin testing')
print("**********")

print(adata.obs_names)

print('this is adata: \n', adata)

#subset = adata[adata.obs_names.isin(['col_one_list']), :]
#print(final_data_subset)

print("********")
print("*****whatabouthisone?****")
#adata_subset = final_data[final_data.obs_names.T.isin(col_one_list), :]
#sublist = ['AAACCTGAGTACATGA-1', 'AAACCTGAGTGTCCCG-1']
blood_sub_adata = adata[adata.obs_names.isin(blood_subset_list)] #.obs
#blood_sub_adata.to_csv("output_data/2020-01-19_blood_sub_adata.csv")

print('*****')
print('this is the adata_subset ------->>>>>')
print(blood_sub_adata)
#print(adata_subset)

print("****adada")
print()









