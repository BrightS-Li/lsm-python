import xlwings

app = xlwings.App(visible=False,add_book=False)
f = app.books.open('./testcase/testcase.xlsx')
sheet = f.sheets('单接口测试')
lest_call = sheet.used_range.last_cell
last_row = lest_call.row
last_col = lest_call.column
print(chr(last_col+97))




app.kill()