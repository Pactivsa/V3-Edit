#后端的初始化部分
from utils.structure import parser_default,output_manager,init_folder_structure,replace_empty

from utils.template import BaseManager


def singleton(cls):
    instance = {}
    def wrapper(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]
    return wrapper

@singleton
class BackendManager():
    def __init__(self, game_path, mod_path):
        self.game_path = game_path
        self.mod_path = mod_path

        #初始化mod的文件夹结构

        init_folder_structure(mod_path)

        #解析V3原版的内容

        self.raw = parser_default(game_path)
        self.mods = parser_default(mod_path)

        #遍历所有组件，若mods.manager和raw.manager有key重复，则从raw.manager中删除
        for part in self.mods.keys():
            mods_manager:BaseManager = self.mods[part]
            raw_manager:BaseManager = self.raw[part]

            for key in mods_manager.keys():
                if key in raw_manager.keys():
                    raw_manager.pop(key)

        if True:
            self.replacement()

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
        
    def get_part(self, part:str):
        '''
            从raw和mods中获取指定的组件的所有key
            @param part: 组件的名称
            允许值从 utls.structure获取，包括：[
                "buildings",
                "bg",
                "pmg",
                "pm",
                "goods"
            ]
            @return: mods中的key列表，raw中的key列表
        '''
        mods_manager:BaseManager = self.mods[part]
        raw_manager:BaseManager = self.raw[part]

        return mods_manager.keys() , raw_manager.keys()
    
    def get_part_detail(self, part:str, key:str):
        '''
            从raw和mods中获取指定的组件的详细信息
            @param part: 组件的名称
            @param key: 组件的key,
            
            允许值从 utls.structure获取，包括：[
                "buildings",
                "bg",
                "pmg",
                "pm",
                "goods"
            ]
            @return: mods中的组件，raw中的组件
        '''
        mods_manager:BaseManager = self.mods[part]
        raw_manager:BaseManager = self.raw[part]

        #先从mods中获取
        mods = mods_manager[key]
        if mods is not None:
            return mods,"mods"
        
        #再从raw中获取
        return raw_manager[key],"raw"
    
    def set_modified(self, part:str, key:str) -> None:
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

    
    
    
        


                    





