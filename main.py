from os import getcwd
from arffconvert import ArffDFClass

# Carregar o arquivo arff
path = getcwd()
path_datasets = path + "/datasets"

dataframes = ArffDFClass(path_datasets).arff_to_df()
for df in dataframes:
    print(df)