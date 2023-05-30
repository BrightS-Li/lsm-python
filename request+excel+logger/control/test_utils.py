from control.testsuit_utils import testsuit
from control.request_utils import Myrequest
from control.log_utils import logger
from control.excel_utils import Excel
from control.tools.Progress_bar_utils import progress_bar
import time
import requests

def req_test(testsuit):
    # 返回的实际结果
    res = []
    logger.info('===========================================开始测试===========================================')
    for i in testsuit:
        for x in i['steps']:
            try:
                if x['element']:
                    if x['element']['type'] == 'get':
                        result = Myrequest.get(x['element']['url']).text
                    elif x['element']['type'] == 'post':
                        data = eval(x['data'])
                        result = Myrequest.post(x['element']['url'],data=data).text
                    
                    logger.info(\
                        f'\n测试编号:{i["id"]},  测试步骤：{x["no"]}\n'\
                        f'测试接口:{x["element"]}\n'\
                        f'测试参数:{x["data"]}\n'\
                        f'result:{result}\n'\
                        '-----------------------------------------'
                        )
                else:
                    result = 'element为空'
                    logger.error(result)
                res.append(result)
            except requests.exceptions.ConnectionError as e:
                logger.info('由于目标计 算机积极拒绝，无法连接。')
    logger.info('===========================================测试结束===========================================\n')
    return res

def res_w(res):
    w = 2
    a = Excel('./testcase/testcase.xlsx')
    logger.info('===========================================开始写入===========================================')
    for i in res:  
        # 实际结果
        progress_bar(w-1,len(res))
        res_col = 'k' + str(w)
        a.write_excel(res_col,[i,'lsm',time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())])
        w = w + 1
        time.sleep(0.1)

    logger.info(f'{len(res)}条用例结果写入完成')
    a.kill_excel()
    logger.info('===========================================写入结束===========================================')

if __name__ == '__main__':
    res_w(req_test(testsuit))
