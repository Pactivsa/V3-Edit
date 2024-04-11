from utils.template import BaseManager
from template.buildings import Buildings, Buildings_group, Pmg, Pm
from template.goods import Goods
from utils.folder import get_all_txt_files

import os
import pandas as pd



class structure():
    
    def __init__(self) -> None:
        #定义整个项目的文件夹结构,index为组件名，列包括路径和manager
        pass

    @staticmethod
    def folder_structure() -> pd.DataFrame:
        '''
            返回整个项目的文件夹结构
            @return: index为组件名，列包括路径和manager
        '''

        # 每一次调用时应当是一个新的BaseManager实例
        structure = pd.DataFrame(columns=['path', 'manager'])

        structure.loc['bg'] = ['common/building_groups', BaseManager(Buildings_group)]
        structure.loc['buildings'] = ['common/buildings', BaseManager(Buildings)]
        structure.loc['pmgs'] = ['common/production_method_groups', BaseManager(Pmg)]
        structure.loc['pm'] = ['common/production_methods', BaseManager(Pm)]
        structure.loc['goods'] = ['common/goods', BaseManager(Goods)]

        return structure

def parser_default_single(path) -> dict[str, BaseManager]:
    '''
        在给定的根目录下，按V3结构依次解析所有文件夹的内容
        @param path: 游戏或mod的根目录
        @param exclude: 排除的 index:set 
        @return: 以文件夹名为key, 对应模板的manager为value的字典

        
        增加此项目中的解析内容时需同步更新utils.backend/BackendManager类中函数的str的类型注解限制
    '''

    folder_structure = structure.folder_structure()
    result = {}

    for index in folder_structure.index:
        folder = folder_structure.loc[index]
        folder_path = os.path.join(path, folder['path'])

        manager:BaseManager = folder['manager']
        #manager.init_from_folder(folder_path)
        _, error = manager.init_from_folder_wr(folder_path) 
        result[index] = manager
        
        if error:
            print(f"在{index}中有{error}文件未被解析")

    return result

def parser_default(game_path, mod_path, exclude:bool = False) -> tuple[dict[str, BaseManager], dict[str, BaseManager]
                                                                     ]:
    '''
        在给定的根目录下，按V3结构依次解析所有文件夹的内容
        @param game_path: 游戏的根目录
        @param mod_path: mod的根目录
        @param if_exclude: 是否排除已经存在的文件
        @return: 以文件夹名为key, 对应模板的manager为value的字典
        返回值前者为mods，后者为raw

        
        增加此项目中的解析内容时需同步更新utils.backend/BackendManager类中函数的str的类型注解限制
    '''

    folder_structure = structure.folder_structure()
    mods_result = {}
    raw_result = {}

    for index in folder_structure.index:
        folder = folder_structure.loc[index]
        game_folder_path = os.path.join(game_path, folder['path'])
        mod_folder_path = os.path.join(mod_path, folder['path'])

        mod_manager:BaseManager = structure.folder_structure().loc[index]['manager']
        raw_manager:BaseManager = structure.folder_structure().loc[index]['manager']

        #解析mod,并获取exclude的文件
        exclude_i, error = mod_manager.init_from_folder_wr(mod_folder_path)
        if error:
            print(f"在{index}中有{error}文件未被解析")

        error = None

        if exclude:
            _,error = raw_manager.init_from_folder_wr(game_folder_path, exclude_i)
        else:
            _,error = raw_manager.init_from_folder_wr(game_folder_path)

        if error:
            print(f"在{index}中有{error}文件未被解析")

        mods_result[index] = mod_manager
        raw_result[index] = raw_manager

    return mods_result, raw_result

#将指定的BaseManager输出成文件
def output_manager(manager, path, outputname = 'zzzzz_generated.txt'):
    '''
        将指定的BaseManager编译成文件
        @param manager: BaseManager对象
        @param path: 游戏或mod的根目录
        @param outputname: 输出文件名

    '''

    
    #检测outputname是存在后缀，如果没有则添加后缀 txt
    if not outputname.endswith('.txt'):
        outputname += '.txt'
        print("原文件名后缀不符合，已添加后缀 " + outputname)

    folder_structure = structure.folder_structure()
        
    for index in folder_structure.index:
        folder = folder_structure.loc[index]
        if manager.class_type == folder['manager'].class_type:
            output_txt = os.path.join(path, folder['path'], outputname)
            manager.output(output_txt)
            return
        
    raise Exception("无法识别的class_type")

    
def init_folder_structure(mod_base_path):
    '''
        初始化mod的文件夹结构
        @param mod_base_path: mod的根目录
    '''

    #创建common文件夹
    common_path = os.path.join(mod_base_path, 'common')
    if not os.path.exists(common_path):
        os.makedirs(common_path)

    common_list = [
        'building_groups',
        'buildings',
        'production_method_groups',
        'production_methods',
        'goods',
    ]

    #依次创建common下的文件夹
    for folder in common_list:
        folder_path = os.path.join(common_path, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
    return

def replace_empty(mod_path, game_path):
    '''
        将游戏内的所有文件以空的txt文件替换
    '''
    folder_structure = structure.folder_structure()

    for index in folder_structure.index:
        folder = folder_structure.loc[index]
        folder_path = os.path.join(game_path, folder['path'])
        #获取所有txt文件
        files = get_all_txt_files(folder_path)
        # 在mod中的相应位置生成对应的空文件
        for file in files:
            file = file.replace(game_path, mod_path)
            if not os.path.exists(file):
                with open(file, 'w') as f:
                    f.write('')



