import os
import csv
import openpyxl

def main():
     filepath = os.path.join('data', 'cm_data_2016.xlsx')
     book = openpyxl.load_workbook(filepath, read_only=True, keep_vba=False)
     dest_dir = os.path.join('output', 'cm_data')
     os.makedirs(dest_dir, exist_ok=True)
     
     for sheet in book.worksheets:
         dest_path = os.path.join(dest_dir, "cm_data_2016.csv")
         
         with open(dest_path, 'w', newline='', encoding='utf-16') as fp:
             writer = csv.writer(fp, dialect='excel-tab', quoting=csv.QUOTE_ALL)
             
             for cols in sheet.rows:
                 writer.writerow([str(col.value or '') for col in cols])

if __name__ == '__main__':
    main()
