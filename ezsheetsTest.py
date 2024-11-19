import ezsheets

ss = ezsheets.Spreadsheet('1jDZEdvSIh4TmZxccyy0ZXrH-ELlrwq8_YYiZrEOB4jg')
sheet = ss[0]
for i, row in enumerate(sheet.getRows()):
    if i != 0 and row[0] != '':
        if int(row[0]) * int(row[1]) != int(row[2]):
            print("The data in row %s is wrong." % str(i + 1))
