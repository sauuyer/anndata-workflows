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

# Load the TCR data (annotations)
adata_tcr_blood = ir.io.read_10x_vdj("filtered_contig_annotations.csv")
adata_tcr_tumor = ir.io.read_10x_vdj("filtered_contig_annotations_tumor020420.csv")

# Load the associated transcriptomics data
adata_blood = sc.read_10x_h5("filtered_feature_bc_matrix-2.h5")
adata_tumor = sc.read_10x_h5("filtered_feature_bc_matrix_tumor020420.h5")

print('done line 30. data imported')

### merging
#blood
ir.pp.merge_with_tcr(adata_blood, adata_tcr_blood)
adata_blood.var_names_make_unique()
#tumor
ir.pp.merge_with_tcr(adata_tumor, adata_tcr_tumor)
adata_tumor.var_names_make_unique()

### import the subset from excel
subset = pd.read_csv('csvsubset02420_metgoednamen.csv')
# Here take out only the barcode column and make into list
subset_list = subset['barcode.'].tolist()
print('this is col_one_list')
print(subset_list)

print("**********")
print('begin testing')
print("**********")
print("this is obs_names")
print(adata_blood.obs_names)
print(adata_tumor.obs_names)

print("********")
print("*****whatabouthisone?****")
#blood
blood_sub_adata = adata_blood[adata_blood.obs_names.isin(subset_list)]
blood_sub_adata_filteredcsv = adata_blood[adata_blood.obs_names.isin(subset_list)].obs
blood_sub_adata_filteredcsv.to_csv("output_data/2020-01-26_blood_sub_adata.csv")
#tumor
tumor_sub_adata = adata_tumor[adata_tumor.obs_names.isin(subset_list)]
tumor_sub_adata_filteredcsv = adata_tumor[adata_tumor.obs_names.isin(subset_list)].obs
tumor_sub_adata_filteredcsv.to_csv("output_data/2020-01-26_tumor_sub_adata.csv")

print('*****')
print('this is the blood adata file ------->>>>>')
print(blood_sub_adata)
print('this is the tumor adata file ------->>>>>')
print(tumor_sub_adata)

print('*****')
print("done")












