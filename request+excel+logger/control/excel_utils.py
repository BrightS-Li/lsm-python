import xlwings as ws

class Excel():
    '''
    操作excel表格
    '''
    def __init__(self,file_path):
        '''
        打开excel工作簿

        Args:
            type:r--读取文件,w--写入文件
            file_path:文件路径  
        return:
            self.app: excel程序
            self.f1:  excel打开工作簿
            self.sheet:打开sheet
            self.list: 存储数据到list
        '''
        # app excel程序
        self.app = ws.App(visible=False,add_book=False)
        # excel工作簿
        self.fl = self.app.books.open(file_path)
        # Sheet[0]
        self.sheet = self.fl.sheets[0]
        # 装载所有数据的list
        self.list = []

    def get_max_row(self):
        '''获取最大行'''
        return self.sheet.used_range.last_cell.row

    def get_max_column(self):
        '''获取最大列'''
        return self.sheet.used_range.last_cell.column

    def read_excel(self):
        '''读取exlce'''
        for i in range(1,self.get_max_row()+1):
            # 最大列字母转化
            
            # A1:D1  A4:D4  A是不变的,行号在遍历，D是最大列名
            rang = self.sheet.range(f'A{i}:{colname}{i}').value
            self.list.append(rang)
        return self.list

    def write_excel(self,col,data):
        '''写入实际结果，执行人，执行时间，测试结果'''
        self.sheet.range(col).value = data
        # 写入实际结果k2: ,执行人l2:，执行时间m2:，
        for i in range(2,self.get_max_row()+1):
            if isinstance(data,list):
                col = chr(len(data)+ord('k'))
                Fnt = self.sheet.range(f'k{i}:{col}{i}')
            else:
                Fnt = self.sheet.range(f'k{i}')
            Fnt.api.Font.Color = 51     # 设置字体的颜色，具体颜色索引见下方。
            Fnt.api.Font.Size = 9          # 设置字体的大小。
            Fnt.api.Font.Bold = True        # 设置为粗体。
            Fnt.api.HorizontalAlignment = -4108    # -4108 水平居中。 -4131 靠左，-4152 靠右。
            Fnt.api.VerticalAlignment = -4130      # -4108 垂直居中（默认）。 -4160 靠上，-4107 靠下， -4130 自动换行对齐。
            # 预期结果
            idea_res = self.sheet.range(f'j{i}').value
            # 实际结果
            real_res = self.sheet.range(f'k{i}').value
            # 测试结果
            test_real = self.sheet.range(f'n{i}')
            # 写入步骤结果
            if idea_res in real_res:
                test_real.value = 'PASS'
                test_real.api.Font.Color = 0x00FF00
            else:
                test_real.value = 'FAIL'
                test_real.api.Font.Color = 0x0000ff
            test_real.api.Font.Size = 9
        self.fl.save()
        return

    def kill_excel(self):
        '''退出excel程序'''
        self.app.kill()

if __name__ == '__main__':
    file = './testcase/testcase.xlsx'
    e = Excel(file)
    # print('\n---获取最大行---\n',e.get_max_row())
    # print('\n---获取最大列---\n',e.get_max_column())
    # print('\n---读取行---\n',element_tojson(e.read_excel()))
    for i in e.read_excel():
        print(i)
    e.kill_excel()