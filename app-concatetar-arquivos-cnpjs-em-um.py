import glob
import pandas as pd
import time

# specifying the path to csv files
path = './data/output/lista-cnpjs-separados'

# csv files in the path
file_list = glob.glob(path + "/*.xlsx")

# list of excel files we want to merge.
# pd.read_excel(file_path) reads the  
# excel data into pandas dataframe.
excl_list = []

for file in file_list:
    excl_list.append(pd.read_excel(file))

# concatenate all DataFrames in the list
# into a single DataFrame, returns new 
# DataFrame.
excl_merged = pd.concat(excl_list, ignore_index=True)
print(excl_merged['cnpj'].value_counts())

# cleaning dataframe before export to excel
excl_merged_complete = excl_merged.loc[(excl_merged['cnae'] != "cnpj nao encontrado")]
excl_merged_complete = excl_merged_complete.drop_duplicates('cnpj').reset_index(drop=True)

excl_merged_uncomplete = excl_merged.loc[(excl_merged['cnae'] == "cnpj nao encontrado")]
excl_merged_uncomplete = excl_merged_uncomplete.drop_duplicates('cnpj').reset_index(drop=True)

# drop all rows in the excl_merged_uncomplete if all of them  by 'cnpj' are in the excl_merged_complete
cnpj_list = excl_merged_complete['cnpj'].unique()
mask = excl_merged_uncomplete['cnpj'].isin(cnpj_list)
excl_merged_uncomplete = excl_merged_uncomplete[~mask]
excl_merged_uncomplete = excl_merged_uncomplete.drop_duplicates('cnpj').reset_index(drop=True)

# print the merged DataFrame and sum of number of rows in the dataframe
print(excl_merged_complete['cnae'].value_counts())
print(excl_merged_uncomplete['cnae'].value_counts())

# exporting to excel file with date and time
todays_date = time.strftime("%d-%m-%Y")
todays_time = time.strftime("%H-%M-%S")
excelfilename = "rnt-cnpj-com-cnae" + "-dia-" + todays_date + "-hora-" + todays_time +".xlsx"
excelfilename_uncomplete = "rnt-cnpj-com-cnae" + "-dia-" + todays_date + "-hora-" + todays_time + "-sem-cnae"+".xlsx"


excl_merged_complete.to_excel(f"data\output\{excelfilename}", sheet_name='sheet1', index=False)
excl_merged_uncomplete.to_excel(f"data\output\{excelfilename_uncomplete}", sheet_name='sheet1', index=False)