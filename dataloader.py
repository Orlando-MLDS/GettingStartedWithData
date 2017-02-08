
import pandas as pd

# Suggestion: functions named after file type and if with Pandas
#   ie, csv_load and csv_pandas or similar

# only making one Excel function, two outputs to demo
def Excel(file):

    # Pandas excel loader is built off of several other excel readers,
    # such as openXLRD and xlsxwriter

    # this is reflected in how many ways there are to read in an excel file.
    basicLoad = pd.read_excel(file)
    alternateLoad = pd.ExcelFile(file)

    # read_excel defaults to read the first sheet in an excel book
    # For a comprehensive list of parameters for read_excel, see: http://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_excel.html
    # you can specify the sheets you want by name
    sheetByName = pd.read_excel(file, sheetname="Sheet1")
    # by index
    sheetsByIndex = pd.read_excel(file, sheetname=[0, 1, 5])

    # if you don't know which sheets you want, you can specify header=None and
    # all sheets will be loaded in a nested structure:
    # do both of these work???
    allSheetsByHeader = pd.read_excel(file, header=None)
    allSheetsBySheets = pd.read_excel(file, sheetname=0)

    # You can skip rows or columns
    subset = pd.read_excel(file, skip_footer=5, skiprows=2, names=["COLNAMES"])

    return basicLoad, alternateLoad, sheetByName, sheetsByIndex, allSheetsByHeader, allSheetsBySheets, subset