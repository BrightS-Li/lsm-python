from control.excel_utils import Excel

def element_tojson(element):
    '''elemnet.xlsx表--->将元素和链接表处理为json格式,方便处理'''
    element_dict = {}
    for e in element:
        element_dict[e[0]] = {'type':e[1],'url':e[2]}
    return element_dict

def test_todict(testdata):
    '''testcase.xlsx--->处理成json,id:Test1,element:页面接口'''
    header = {
        '用例编号':'id',
        '用例标题':'title',
        '前置条件':'conditon',
        '测试功能点':'testdot',
        '测试步骤':'step',
        '页面':'page',
        '接口名称':'element',
        '测试数据':'data',
        '预期结果':'expected',
        '实际结果':'res',
        '设计者':'designer',
        '步骤结果':'score',
        '备注':'remark',
    }
    head = []
    list_dict_data = []
    # 标题转成成中文，如果在header中找不到，则返回原标题
    for title in testdata[0]:
        titles = header.get(title,title)
        head.append(titles)
    for case in testdata[1:]:
        # 头部和内容拼接
        dict_data = {}
        for i in range(len(head)):
            if isinstance(case[i],str):
                dict_data[head[i]] = case[i].strip()
            else:
                dict_data[head[i]] = case[i]
        list_dict_data.append(dict_data)
    return list_dict_data

def test_tosuit(data):
    element_test = Excel('./element/elements.xlsx')
    testcase = {}
    testsuit = []
    for i in data:
        if i['id']:
            if testcase:
                testsuit.append(testcase)
                testcase = {}
            testcase['id'] = i['id']
            testcase['title'] = i['title']
            testcase['testdot'] = i['testdot']
            testcase['steps'] = []
            testcase['remark'] = i['remark']

        # 步骤里面添加的字段
        step = {}
        # 前置步骤
        step['control'] = ''
        # 步骤
        step['no'] = str(i['step'])
        # 从接口表获取接口地址
        step['element'] = element_tojson(element_test.read_excel()).get(i['element'],'')
        # 测试参数
        step['data'] = i['data']
        # 预期结果
        step['expected'] = i['expected']
        # res实际结果
        step['__res'] = ''
        # 测试结果
        step['__testres'] = ''
        testcase['steps'].append(step)
    testsuit.append(testcase)
    element_test.kill_excel()
    return testsuit

e = Excel('./testcase/testcase.xlsx')
data = test_todict(e.read_excel())
e.kill_excel()
testsuit = test_tosuit(data)

# for i in testsuit:
#     print(i)




