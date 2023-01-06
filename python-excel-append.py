#! /usr/bin/python3
import os
import sys
import pandas as pd
import openpyxl
#import xlsxwriter

path="/var/lib/awx/projects/python-workbook/"
files=os.listdir(path)
Target= sys.argv[1]

print(files)
Target= sys.argv[1]

wb = openpyxl.Workbook()
wb.save(Target)

for file in files:
  if file.endswith(".csv"):
    print(file)
    content = pd.read_fwf(file,index=None)
    with pd.ExcelWriter(Target,mode="a", engine="openpyxl") as writer:
      filename = file.split(".")
      content.to_excel(writer,sheet_name=filename[0])
    os.remove(file)
