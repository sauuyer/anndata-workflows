library(dplyr)

subset_file <- read.csv("csvsubset02420_metgoednamen.csv")
subset_file <- select(subset_file, barcode., barcode)
colnames(subset_file) <- paste(colnames(subset_file), ".subsetfile", sep = "")
filtered_blood <- read.csv("output_data/2020-01-19_blood_sub_adata.csv")
colnames(filtered_blood) <- paste(colnames(filtered_blood), ".filteredblood", sep = "")
filtered_tumor <- read.csv("output_data/2020-01-26_tumor_sub_adata.csv")
colnames(filtered_tumor) <- paste(colnames(filtered_tumor), ".filteredtumor", sep = "")
joined_sheet <- full_join(subset_file, filtered_blood, by = c("barcode..subsetfile" = "X.filteredblood"))
joined_sheet_full <- full_join(joined_sheet, filtered_tumor, by = c("barcode..subsetfile" = "X.filteredtumor"))

write.csv(joined_sheet_full, "output_data/all_data_merged.csv")
