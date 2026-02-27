# 作者: 王道 龙哥
# 2025年01月03日10时50分15秒
# xxx@qq.com

import sys
sys.path.insert(0,'module')  # sys.path 为导入模块库的顺序目录
print(sys.path)
print('-'*50)
import my_module  # 注意，这里的模块并不在当前路径下。所以，在import之前需要先将该模块所在文件夹（库）加入到sys.path中去
# 如果文件夹是包的格式，可直接导入

my_module.test1()