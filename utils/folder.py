#对文件夹内的所有文件进行操作
import os
from utils.utils import ContentParser
import pandas as pd


def parser_file(path):
    '''
        @param path: 文件路径
    '''
    #检测目标路径是否为txt文件，否则报错
    if not path.endswith('.txt'):
        raise Exception('目标路径不是txt文件')
    #如果目标是txt文件,则进行解析
    #检测是否包含bom头，如果有则去除
    #如果目标是txt文件,则进行解析
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
        #检测是否包含bom头，如果有则去除
        if content.startswith('\ufeff'):
            content = content[1:]            
        #解析文件内容
        parser = ContentParser(content)
        result = parser.parse()
    return result


def parser_folder(path):
    '''
        @param path: 文件夹路径
    '''
    final_result = {}
    result_list = []
    files = os.listdir(path)
    for file in files:
        file_path = os.path.join(path, file)
        #如果目标是文件夹，递归调用parser_folder，将返回的结果添加到最终结果中
        if os.path.isdir(file_path):
            result, result_list = parser_folder(file_path)
            for key in result:
                final_result[key] = result[key]
            result_list += result_list
            continue

        #如果目标不是txt文件,则跳过
        if not file_path.endswith('.txt'):
            continue
        #如果目标是txt文件,则进行解析
        try:
            result = parser_file(file_path)
        except Exception as e:
            print('文件解析错误：', file_path)
            raise e
        #将解析结果添加到列表中，并将解析结果中的每一项添加到最终结果中
        result_list.append(result)
        #将解析结果中的每一项添加到最终结果中
        for key in result:
            final_result[key] = result[key]
    return final_result, result_list

#返回指定文件夹下中所有txt文件的文件名序列
def get_all_txt_files(path) -> list:
    '''
        获取指定文件夹下中所有txt文件的文件名序列，包括子文件夹内的txt文件
        @param path: 文件夹路径
        @return: 文件名序列
    '''
    files = os.listdir(path)
    result = []
    for file in files:
        file_path = os.path.join(path, file)
        #如果目标是文件夹，递归调用get_all_txt_files，将返回的结果添加到最终结果中
        if os.path.isdir(file_path):
            result += get_all_txt_files(file_path)
            continue
        #如果目标不是txt文件,则跳过
        if not file_path.endswith('.txt'):
            continue
        #如果目标是txt文件,则添加到最终结果中
        result.append(file_path)
    return result



    
    





        




