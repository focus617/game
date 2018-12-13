import sys
import os

if sys.version_info < (3, 0):
    print('本代码需要在python3.5以上的版本运行')
    print('当前版本号为%d.%d' % (sys.version_info[0], sys.version_info[1]))
    print('正在退出')
    sys.exit(1)

current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_path)

# optionally print the sys.path for debugging
# print("in __init__.py sys.path: \n", sys.path)