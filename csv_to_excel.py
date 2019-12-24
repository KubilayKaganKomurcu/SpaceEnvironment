import pandas as pd

'''
reader = pd.read_csv('AC_H0_SWE_95692.csv')
reader.to_excel('Swepam_excel.xlsx', index=False)




writer = pd.read_excel('MOM_excel.xlsx')
writer.to_csv('THC_L2_MOM_216777.csv', index=False)

writer = pd.read_excel('FGM_excel.xlsx')
writer.to_csv('THC_L2_FGM_89446.csv', index=False)

writer = pd.read_excel('MFI_excel.xlsx')
writer.to_csv('AC_H0_MFI_95692.csv', index=False)



'''
writer = pd.read_excel('Swepam_excel.xlsx')
writer.to_csv('AC_H0_SWE_95692.csv', index=False)