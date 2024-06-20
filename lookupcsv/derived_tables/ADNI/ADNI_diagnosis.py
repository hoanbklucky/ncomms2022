import csv
import os

dict_data = []
column_names = ['PHASE',
               'ID',
               'RID',
               'SITEID',
               'VISCODE',
               'VISCODE2',
               'USERDATE',
               'USERDATE2',
               'EXAMDATE',
               'Diagnosis']

# Get the current working directory
cwd = os.getcwd()

with open(r"C:\Users\ngoth\OneDrive - flsouthern.edu\Research\AI4AD\ncomms2022\lookupcsv\raw_tables\ADNI\ADNI_DXSUM_PDXCONV.csv") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        content = {}
        for column in column_names:
            if column in ['PHASE', 'ID', 'RID', 'SITEID', 'VISCODE', 'VISCODE2', 'USERDATE', 'USERDATE2', 'EXAMDATE']:
                content[column] = row[column]
            elif column == 'Diagnosis':
                if row['DIAGNOSIS'] == '1': # normal
                    content[column] = 'NL'
                    dict_data.append(content)
                elif row['DIAGNOSIS'] == '2': # use all type of mci
                    content[column] = 'MCI'
                    dict_data.append(content)
                elif row['DIAGNOSIS'] == '3': # dementia
                    if row['DXAD'] == '1': # etiology is AD
                        content[column] = 'AD'
                        dict_data.append(content)

print(os.getcwd())
with open(r'C:\Users\ngoth\OneDrive - flsouthern.edu\Research\AI4AD\ncomms2022\lookupcsv\derived_tables\ADNI\ADNI_Diagnosis.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=column_names)
    writer.writeheader()
    for data in dict_data:
        writer.writerow(data)

