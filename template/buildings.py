from utils.template import BaseTemplate
from template.goods import Goods
from typing import Literal, Union
import pandas as pd

class Buildings_group(BaseTemplate):
    def __init__(self, name ,if_init=False):
        original_file = "template/original/buildings_groups.txt"
        super().__init__(name,original_file, if_init)

    def _clone(self,name):
        return Buildings_group(name, self.if_init)
    
    @staticmethod
    def structure() -> dict:
        '''
            返回建筑组的结构
            以 key: path返回
        '''
        return {
            "name": "name",
            "category": "category",
            "always_possible": "always_possible",
            "economy_of_scale": "economy_of_scale",
            "cash_reserves_max": "cash_reserves_max",
            "should_auto_expand": "should_auto_expand"
        }

    def __getitem__(self, key):
        structure = self.structure()
        #检测key是否存在
        if key not in structure:
            raise KeyError(f"bg不存在{key}，允许的key有{list(structure.keys())}")
        #返回对应的值
        return self.trace(structure[key])
    
    def __setitem__(self, key, value):
        structure = self.structure()
        #检测key是否存在
        if key not in structure:
            raise KeyError(f"bg不存在{key}，允许的key有{list(structure.keys())}")
        #设置对应的值
        self.add(structure[key], "=", value)
    
    #category

    def set_category(self, category:str) -> None:
        self.add("category", "=", category)

    def get_category(self) -> str:
        return self.trace("category")
    
    # always_possible
    def set_always_possible(self, always_possible:Literal["yes","no"]) -> None:
        self.add("always_possible", "=", always_possible)

    def get_always_possible(self) -> Literal["yes","no"]:
        return self.trace("always_possible")
    
    # economy_of_scale 
    def set_economy_of_scale(self, economy_of_scale:Literal["yes","no"]) -> None:
        self.add("economy_of_scale", "=", economy_of_scale)

    def get_economy_of_scale(self) -> Literal["yes","no"]:
        return self.trace("economy_of_scale")
    
    # cash_reserves_max

    def set_cash_reserves_max(self, cash_reserves_max:int) -> None:
        self.add("cash_reserves_max", "=", cash_reserves_max)

    def get_cash_reserves_max(self) -> int:
        return self.trace("cash_reserves_max")
    
    # should_auto_expand
    # TODO:以Trigger类返回与传入
    def set_SAE(self, SAE:str) -> None:
        self.add("should_auto_expand", "=", SAE)

    def get_SAE(self) -> str:
        return self.trace("should_auto_expand")
    
    
    
    

    
class Buildings(BaseTemplate):
    def __init__(self, name ,if_init=False):
        original_file = "template/original/buildings.txt"
        super().__init__(name,original_file, if_init)

    def _clone(self,name) -> "Buildings":
        return Buildings(name,  self.if_init)
    
    @staticmethod
    def structure() -> dict:
        '''
            返回建筑的结构
            以 key: path返回
        '''
        return {
            "name": "name",
            "category": "category",
            "level_per_mesh": "level_per_mesh",
            "building_group": "building_group",
            "unlocking_technologies": "unlocking_technologies",
            "production_method_groups": "production_method_groups",
            "required_construction": "required_construction",
            "terrain_manipulator": "terrain_manipulator",
            "texture": "texture",
            "city_type": "city_type"
        }
    
    def __getitem__(self, key):
        structure = self.structure()
        #检测key是否存在
        if key not in structure:
            raise KeyError(f"building不存在{key}，允许的key有{list(structure.keys())}")
        #返回对应的值
        return self.trace(structure[key])
    
    def __setitem__(self, key, value):
        structure = self.structure()
        #检测key是否存在
        if key not in structure:
            raise KeyError(f"building不存在{key}，允许的key有{list(structure.keys())}")
        #设置对应的值
        self.add(structure[key], "=", value)

    # texture
    def set_texture(self, texture_path) -> None:
        self.add("texture", "=", texture_path)

    def get_texture(self) -> str:
        return self.trace("texture")

    # city_type
    def set_city_type(self, city_type) -> None:
        self.add("city_type", "=", city_type)

    def get_city_type(self) -> str:
        return self.trace("city_type")
    
    # level_per_mesh
    def get_lpm(self) -> int:
        return int(self.trace("level_per_mesh"))

    def set_lpm(self, lpm) -> None:
        self.add("level_per_mesh", "=", lpm)

    # building_group
    def set_building_group(self, bg: Union[str, Buildings_group]) -> None:
        if isinstance(bg, Buildings_group):
            bg = bg.name
        self.add("building_group", "=", bg)

    def get_building_group(self) -> str:
        return self.trace("building_group")

    # unlocking_technologies
    def add_unlocking_technology(self, tech: str) -> None:
        self.insert(tech, "unlocking_technologies",True)

    def remove_unlocking_technology(self, tech: str) -> None:
        self.delete(tech, "unlocking_technologies")

    def get_unlocking_technologies(self) -> list:
        return self.trace("unlocking_technologies")
    
    def set_unlocking_technologies(self, techs: list):
        #清空原有的
        self.delete("unlocking_technologies")
        for tech in techs:
            self.add_unlocking_technology(tech)
    
    # production_method_groups
    def add_production_method_group(self, pmg: str) -> None:
        self.insert(pmg, "production_method_groups",True)

    def remove_production_method_group(self, pmg: str) -> None:
        self.delete(pmg, "production_method_groups")

    def get_production_method_groups(self) -> str:
        return self.trace("production_method_groups")
    
    def set_production_method_groups(self, pmgs: list) -> None:
        #清空原有的
        self.delete("production_method_groups")
        for pmg in pmgs:
            self.add_production_method_group(pmg)
    
    # required_construction
    def set_required_construction(self, construction) -> None:
        self.add("required_construction", "=", construction)

    def get_required_construction(self) -> str:
        return self.trace("required_construction")
    
    # terrain_manipulator
    def set_terrain_manipulator(self, terrain_manipulator) -> None:
        self.add("terrain_manipulator", "=", terrain_manipulator)

    def get_terrain_manipulator(self) -> str:
        return self.trace("terrain_manipulator")

    
    

class Pmg(BaseTemplate):
    def __init__(self,name , if_init=False,Buildings: Buildings=None):
        original_file = "template/original/production_method_groups.txt"
        super().__init__(name ,original_file, if_init)
        if Buildings:
            self.bind(Buildings)
    def bind(self, Building: Buildings):
        Building.insert(self.name, "production_methods",True)

    def _clone(self,name):
        return Pmg(name, self.if_init)
    
    @staticmethod
    def structure() -> dict:
        '''
            返回生产方法组的结构
            以 key: path返回
        '''
        return {
            "name": "name",
            "production_methods": "production_methods",
            "texture": "texture"
        }
    
    def __getitem__(self, key):
        structure = self.structure()
        #检测key是否存在
        if key not in structure:
            raise KeyError(f"pmg不存在{key}，允许的key有{list(structure.keys())}")
        #返回对应的值
        return self.trace(structure[key])
    
    def __setitem__(self, key, value):
        structure = self.structure()
        #检测key是否存在
        if key not in structure:
            raise KeyError(f"pmg不存在{key}，允许的key有{list(structure.keys())}")
        #设置对应的值
        self.add(structure[key], "=", value)
    
    # production_methods
    def add_pm(self, pm_name: str):
        self.insert(pm_name, "production_methods",True)

    def remove_pm(self, pm_name: str):
        self.delete(pm_name, "production_methods")

    def get_pms(self) -> list:
        return self.trace("production_methods")
    
    def set_pms(self, pms: list):
        #清空原有的
        self.delete("production_methods")
        for pm in pms:
            self.add_pm(pm)

    # texture
    def set_texture(self, texture_path):
        self.add("texture", "=", texture_path)

    def get_texture(self):
        return self.trace("texture")
    
class Pm(BaseTemplate):
    def __init__(self,name , if_init=False,Pmg: Pmg=None):
        original_file = "template/original/production_methods.txt"
        super().__init__(name , if_init)
        if Pmg:
            self.bind(Pmg)
        
    def bind(self, Pmg: Pmg):
        Pmg.insert(self.name, "production_methods",True)

    def _clone(self,name):
        return Pm(name, self.if_init)
    
    @staticmethod
    def structure() -> dict:
        '''
            返回生产方法的结构
            以 key: path返回
        '''
        #完整占据一个子结构的属性
        f_structure = {
            "name": "name",
            "texture": "texture",
            "disallowing_laws": "disallowing_laws",
            "building_modifiers": "building_modifiers",
            "unlocking_technologies": "unlocking_technologies",
            "workforce_scaled": "building_modifiers.workforce_scaled",
            "level_scaled": "building_modifiers.level_scaled",
            "unscaled": "building_modifiers.unscaled"
        }
        #从某一子结构中部分提取的属性
        p_structure = {
            "inputs": "building_modifiers.workforce_scaled",
            "outputs": "building_modifiers.workforce_scaled",
            "employees": "building_modifiers.level_scaled",
            "shares": "building_modifiers.unscaled"
        }

        return f_structure, p_structure

    
    def __getitem__(self, key):
        f_structure, p_structure = self.structure()
        #检测key是否存在
        if key in f_structure:
            #返回对应的值
            return self.trace(f_structure[key])
        elif key in p_structure:
            return self.trace(p_structure[key])
        else:
            raise KeyError(f"pm不存在{key}，允许的key有{list(f_structure.keys())+list(p_structure.keys())}")


    # texture
    def set_texture(self, texture_path):
        self.add("texture", "=", texture_path)

    def get_texture(self) -> str:
        return self.trace("texture")
    
    # disallowing_laws

    def get_disallowing_laws(self) -> list:
        return self.trace("disallowing_laws")
    
    def add_disallowing_law(self, law: str):
        self.insert(law, "disallowing_laws",True)

    def remove_disallowing_law(self, law: str):
        self.delete(law, "disallowing_laws")

    def set_disallowing_laws(self, laws: list):
        #清空原有的
        self.delete("disallowing_laws")
        for law in laws:
            self.add_disallowing_law(law)

    # unlocking_technologies
            
    def get_unlocking_technologies(self) -> list:
        return self.trace("unlocking_technologies")
    
    def add_unlocking_technology(self, tech: str):
        self.insert(tech, "unlocking_technologies",True)

    def remove_unlocking_technology(self, tech: str):
        self.delete(tech, "unlocking_technologies")

    def set_unlocking_technologies(self, techs: list):
        #清空原有的
        self.delete("unlocking_technologies")
        for tech in techs:
            self.add_unlocking_technology(tech)

    # workforce_scaled

    def get_workforce_scaled(self) -> dict:
        return self.trace("building_modifiers.workforce_scaled")
    
    def set_workforce_scaled(self, workforce_scaled: dict):
        #清空原有的workforce_scaled
        self.delete("building_modifiers.workforce_scaled")

        self.add("building_modifiers.workforce_scaled", "=", workforce_scaled)

    # workforce_scaled.inputs
    def add_input(self, good:str, amount:int) -> None:
        path = "building_modifiers.workforce_scaled"
        key = "goods_input_"+good+"_add"
        self.add(key,"=",amount,path, True)

    def remove_input(self, good):
        key = "goods_input_"+good+"_add"
        path = "building_modifiers.workforce_scaled"
        self.delete(key,path)

    def get_inputs(self):
        goods_dict = self.trace("building_modifiers.workforce_scaled")
        result = {}
        if goods_dict is None:
            return result
        # 解析存在的输入
        for good in goods_dict:
            if good.startswith("goods_input_"):
                good_name = good.split("_")[2]
                result[good_name] = goods_dict[good][1]

        return result
    
    def set_inputs(self, inputs: dict):
        #清空原有的关于input的内容
        goods_dict = self.trace("building_modifiers.workforce_scaled")
        if goods_dict is not None:
            for good in goods_dict:
                if good.startswith("goods_input_"):
                    self.delete(good,"building_modifiers.workforce_scaled")

        for good in inputs:
            self.add_input(good, inputs[good])

    # workforce_scaled.output
    def get_outputs(self):
        goods_dict = self.trace("building_modifiers.workforce_scaled")
        result = {}

        if goods_dict is None:
            return result
        # 解析存在的输入
        for good in goods_dict:
            if good.startswith("goods_output_"):
                good_name = good.split("_")[2]
                result[good_name] = goods_dict[good][1]

        return result
                
    def add_output(self, good, amount):
        path = "building_modifiers.workforce_scaled"

        key = "goods_output_"+good+"_add"
        self.add(key,"=",amount,path, True)

    def remove_output(self, good):
        path = "building_modifiers.workforce_scaled"
        key = "goods_output_"+good+"_add"
        self.delete(key,path)

    def set_outputs(self, outputs: dict):
        #清空原有的关于output的内容
        goods_dict = self.trace("building_modifiers.workforce_scaled")
        if goods_dict is not None:
            for good in goods_dict:
                if good.startswith("goods_output_"):
                    self.delete(good,"building_modifiers.workforce_scaled")

        for good in outputs:
            self.add_output(good, outputs[good])

    # level_scaled
    def get_level_scaled(self) -> dict:
        return self.trace("building_modifiers.level_scaled")
    
    def set_level_scaled(self, level_scaled: dict):
        #清空原有的level_scaled
        self.delete("building_modifiers.level_scaled")
        self.add("building_modifiers.level_scaled", "=", level_scaled)

    # level_scaled.employment
        
    def add_employee(self, type, amount):
        path = "building_modifiers.level_scaled"
        key = "building_employment_"+type+"_add"
        self.add(key,"=",amount,path, True)

    def remove_employee(self, type):
        path = "building_modifiers.level_scaled"
        key = "building_employment_"+type+"_add"
        self.delete(key,path)

    def get_employees(self):
        path = "building_modifiers.level_scaled"
        employees = self.trace(path)
        result = {}
        if employees is None:
            return result
        
        for employee in employees:
            if employee.startswith("building_employment_"):
                employee_name = employee.split("_")[2]
                result[employee_name] = employees[employee][1]

        return result
    
    def set_employees(self, employees: dict):
        #清空原有的关于employee的内容
        employees_dict = self.trace("building_modifiers.level_scaled")
        if employees_dict is not None:
            for employee in employees_dict:
                if employee.startswith("building_employment_"):
                    self.delete(employee,"building_modifiers.level_scaled")

        for employee in employees:
            self.add_employee(employee, employees[employee])

    def get_unscaled(self) -> dict:
        return self.trace("building_modifiers.unscaled")
    
    def set_unscaled(self, unscaled: dict):
        #清空原有的unscaled
        self.delete("building_modifiers.unscaled")
        self.add("building_modifiers.unscaled", "=", unscaled)


    def get_country_modifiers_workforce(self):
        return self.trace("country_modifiers.workforce_scaled")

    def get_country_modifiers_level(self):
        return self.trace("country_modifiers.level_scaled")

    def get_country_modifiers_unscaled(self):
        return self.trace("country_modifiers.unscaled")

    def get_state_modifiers_workforce(self):
        return self.trace("state_modifiers.workforce_scaled")

    def get_state_modifiers_level(self):
        return self.trace("state_modifiers.level_scaled")

    def get_state_modifiers_unscaled(self):
        return self.trace("state_modifiers.unscaled")

    def get_timed_modifiers(self):
        return self.trace("timed_modifier")

    def get_texture(self):
        return self.trace("texture")

    def get_required_input_goods(self):
        return self.trace("required_input_goods")

    def get_is_default(self):
        return self.trace("is_default")

    def get_unlocking_laws(self):
        return self.trace("unlocking_laws")

    def get_unlocking_technologies(self):
        return self.trace("unlocking_technologies")

    def get_unlocking_production_methods(self):
        return self.trace("unlocking_production_methods")

    def get_unlocking_global_technologies(self):
        return self.trace("unlocking_global_technologies")

    def get_ai_weight(self):
        return self.trace("ai_weight")

    def get_pollution_generation(self):
        return self.trace("pollution_generation")
    # unscaled.shares
    
    def add_share(self, type, amount):
        path = "building_modifiers.unscaled"
        key = "building_"+type+"_shares_add"
        self.add(key,"=",amount,path, True)

    def remove_share(self, type):
        path = "building_modifiers.unscaled"
        key = "building_"+type+"_shares_add"
        self.delete(key,path)

    def get_shares(self):
        path = "building_modifiers.unscaled"
        shares = self.trace(path)
        result = {}
        if shares is None:
            return result
        
        for share in shares:
            if share.startswith("building_"):
                share_name = share.split("_")[1]
                result[share_name] = shares[share][1]

        return result
    
    def set_shares(self, shares: dict):
        #清空原有的关于share的内容
        shares_dict = self.trace("building_modifiers.unscaled")
        if shares_dict is not None:
            for share in shares_dict:
                if share.startswith("building_"):
                    self.delete(share,"building_modifiers.unscaled")

        for share in shares:
            self.add_share(share, shares[share])

            






        
