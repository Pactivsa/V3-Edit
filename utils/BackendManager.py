'''
    基于模块实现后端管理BM单例
'''
from utils.structure import (
    parser_default ,parser_default_single,
    output_manager,
    init_folder_structure, 
    replace_empty
)
from utils.template import BaseManager

from typing import Literal

def singleton(cls):
    instance = {}
    def wrapper(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]
    return wrapper

@singleton
class BackendManager():
    def __init__(self):
        self.game_path = None
        self.mod_path = None
        self.raw = None
        self.mods = None


    def setBM(self, game_path, mod_path, 
              readtype = Literal["rpALL","rpSAME"]
    ):
        '''
            设置BM的game_path和mod_path
            @param game_path: V3原版的路径
            @param mod_path: mod的路径
            @param readtype: 读取的类型，
            rpALL表示将原版文件全部覆盖到mods中，
            rpSAME表示将重名的文件从原版中删除

        '''        

        self.game_path = game_path
        self.mod_path = mod_path

        #初始化mod的文件夹结构

        init_folder_structure(mod_path)

        #解析V3原版的内容

        if readtype == "rpALL":

            self.raw = parser_default_single(game_path)
            self.mods = parser_default_single(mod_path)

            #遍历所有组件，若mods.manager和raw.manager有key重复，则从raw.manager中删除
            for part in self.mods.keys():
                mods_manager:BaseManager = self.mods[part]
                raw_manager:BaseManager = self.raw[part]

                for key in mods_manager.keys():
                    if key in raw_manager.keys():
                        raw_manager.pop(key)

            self.replacement()

            for part in self.mods.keys():   
                mods_manager:BaseManager = self.mods[part]
                raw_manager:BaseManager = self.raw[part]

                for key in mods_manager.keys():
                    if key in raw_manager.keys():
                        raw_manager.pop(key)

        elif readtype == "rpSAME":
            self.mods, self.raw = parser_default(game_path, mod_path, exclude = True)

            for part in self.mods.keys():
                mods_manager:BaseManager = self.mods[part]
                raw_manager:BaseManager = self.raw[part]

                for key in mods_manager.keys():
                    if key in raw_manager.keys():
                        raw_manager.pop(key)
                    
        else:
            raise ValueError("readtype参数错误")

    def replacement(self):
        '''
            将原版的所有文件置空，并全部转入
        '''

        #将raw中的所有内容移动到mods中
        for part in self.raw.keys():
            mods_manager:BaseManager = self.mods[part]
            raw_manager:BaseManager = self.raw[part]

            mods_manager.merge(raw_manager)

        #输出空文件到mods中
        replace_empty(self.mod_path, self.game_path)

    def output(self):
        '''
            将mods中的所有内容输出到mod_path中
        '''
        for part in self.mods.keys():
            mods_manager:BaseManager = self.mods[part]
            output_path = self.mod_path

            output_manager(mods_manager, output_path)
        
    def get_part(self, part:Literal['bg','buildings','pmgs','pm','goods']
                 ):
        '''
            从raw和mods中获取指定的组件的所有key
            @param part: 组件的名称
            @return: mods中的key列表，raw中的key列表
        '''
        mods_manager:BaseManager = self.mods[part]
        raw_manager:BaseManager = self.raw[part]

        return mods_manager.keys() , raw_manager.keys()
    
    def get_part_detail(self, part:Literal['bg','buildings','pmgs','pm','goods']
                        , key:str):
        '''
            从raw和mods中获取指定的组件的详细信息
            @param part: 组件的名称
            @param key: 组件的key
            @return: mods中的组件，raw中的组件
        '''
        mods_manager:BaseManager = self.mods[part]
        raw_manager:BaseManager = self.raw[part]

        #先从mods中获取
        mods = mods_manager[key]
        if mods is not None:
            return mods  ,"mods"
        
        #再从raw中获取
        return raw_manager[key],"raw"
    
    def set_modified(self, part:Literal['bg','buildings','pmgs','pm','goods']
                     , key:str) -> None:
        '''
            设置指定的组件为已修改
            @param part: 组件的名称
            @param key: 组件的key
        '''
        mods_manager:BaseManager = self.mods[part]
        raw_manager:BaseManager = self.raw[part]

        #将raw中的组件移动到mods中
        mods_manager[key] = raw_manager[key]
        raw_manager.pop(key)




BM = BackendManager()