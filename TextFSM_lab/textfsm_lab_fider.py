from textfsm import TextFSM
from pprint import pprint
import os

filepath = 'E:/桌面文件/配置模版/代码/TextFSM_lab/99/'
filelist = os.listdir(filepath)#列出文件夹内的文件列表（包含子文件夹）
#print(filelist)
# 定义模板文件路径
template_path = 'template2.text'

# 打开模板文件并创建 TextFSM 模板对象



for file in filelist:#循环filelist中的列表元素一次一个，赋值给file，下面代码的file代表着列表中每一个元素
    with open(filepath + file) as f , open(template_path, 'r', encoding='utf-8') as template_file:
        template = TextFSM(template_file)
        raw_text_data = f.read()
        
        # 使用 TextFSM 解析文件内容
    result = template.ParseText(raw_text_data)
    # 打印解析结果
    print(f"文件: {file}")
    print("解析结果:")
    for row in result:
        print(row)
    print("\n")    