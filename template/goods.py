from utils.template import BaseTemplate
from utils.template import BaseManager
import pandas as pd

class Goods(BaseTemplate):
    '''
    "cost", "texture", "category", "prestige_factor", "consumption_tax_cost", "traded_quantity",
    "convoy_cost_multiplier", "obsession_chance", "local", "tradeable", "fixed_price"
    
    '''
    structure = pd.DataFrame(columns=['path', 'default'])
    structure.loc['cost'] = ['cost', '']
    structure.loc['texture'] = ['texture', '']
    structure.loc['category'] = ['category', '']
    structure.loc['prestige_factor'] = ['prestige_factor', '']
    structure.loc['consumption_tax_cost'] = ['consumption_tax_cost', '']
    structure.loc['traded_quantity'] = ['traded_quantity', '']
    structure.loc['convoy_cost_multiplier'] = ['convoy_cost_multiplier', '']
    structure.loc['obsession_chance'] = ['obsession_chance', '']
    structure.loc['local'] = ['local', '']
    structure.loc['tradeable'] = ['tradeable', '']
    structure.loc['fixed_price'] = ['fixed_price', '']

    @classmethod
    def structure_list(cls) -> list:
        return cls.structure.index.tolist()

    def __init__(self, name ,if_init=False):
        original_file = "template/original/goods.txt"
        super().__init__(name,original_file, if_init)

    def _clone(self,name):
        return Goods(name, self.if_init)
    
    def __getitem__(self, key):
        structure_path = Goods.structure['path']
        if key not in structure_path:
            raise Exception(f"Goods中不存在{key}，允许的属性有{list(structure_path.keys())}")
        #返回对应的值
        result = self.trace(structure_path[key])
        if result is None:
            return Goods.structure["default"][key]
        return result
    
    def __setitem__(self, key, value):
        structure_path = Goods.structure['path']
        if key not in structure_path:
            raise Exception(f"Goods中不存在{key}，允许的属性有{list(structure_path.keys())}")
        #设置对应的值
        self.add(structure_path[key], "=", value)
            
    
    @staticmethod
    #从goods_manager中获取所有的goods与对应的cost
    def goods_dict(goods_manager: BaseManager):
        #检测goods_manager中的prototype是否为Goods
        if not isinstance(goods_manager.prototype, Goods):
            raise Exception("goods_manager中的prototype必须为Goods")
        result = {}
        for key in goods_manager.map:
            goods = goods_manager.map[key]
            cost = goods["cost"][1]
            result[key] = cost

        return result
    
    @staticmethod
    #获取指定key的goods的cost
    def goods(goods_manager: BaseManager, key: str):
        #检测goods_manager中的prototype是否为Goods
        if not isinstance(goods_manager.prototype, Goods):
            raise Exception("goods_manager中的prototype必须为Goods")
        goods = goods_manager.map[key]
        cost = goods["cost"][1]
        return cost
    
    
