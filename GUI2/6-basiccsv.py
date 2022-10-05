#basiccsv.py

import csv

#Comma-separated values: CSV

def WritetoCSV(ep):
	with open('allexpense.csv','a',newline='',encoding='utf-8') as file:
		# 'a' = append (เพิ่มได้เรื่อยๆ) , 'w' = replace (ทับไฟล์เดิม)
		fw = csv.writer(file) # fw คือ file writer
		# ep = ['ไก่',300]
		fw.writerow(ep)

	print('Done!')


x = ['ไข่ไก่',30]
WritetoCSV(x)