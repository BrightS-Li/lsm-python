from control.test_utils import res_w,req_test
from control.testsuit_utils import testsuit
import sys
import os

sys.path.append(os.getcwd())

# 测试接口
test = req_test(testsuit)
# 结果写入testcase.xlsx
test_w = res_w(test)
