from utils.template import BaseTemplate

class Buildings_group(BaseTemplate):
    def __init__(self, name ,if_init=False):
        original_file = "template/original/buildings_groups.txt"
        super().__init__(name,original_file, if_init)

    def _clone(self,name):
        return Buildings_group(name, self.if_init)
    
class Buildings(BaseTemplate):
    def __init__(self, name ,if_init=False):
        original_file = "template/original/buildings.txt"
        super().__init__(name,original_file, if_init)

    def _clone(self,name):
        return Buildings(name,  self.if_init)

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
    
    def add_pm(self, pm_name):
        self.insert(pm_name, "production_methods",True)

    def rm_pm(self, pm_name):
        self.delete(pm_name, "production_methods")

    def get_pms(self):
        return self.trace("production_methods")

    def set_texture(self, texture_path):
        self.add("texture", "=", texture_path)

    
    

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
    
    def set_texture(self, texture_path):
        self.add("texture", "=", texture_path)

    def add_input(self, good, amount):
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
        # 解析存在的输入
        for good in goods_dict:
            if good.startswith("goods_input_"):
                good_name = good.split("_")[2]
                result[good_name] = goods_dict[good][1]

        return result
    
    def get_outputs(self):
        goods_dict = self.trace("building_modifiers.workforce_scaled")
        result = {}
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
        key = "goods_output_"+good+"_add"
        path = "building_modifiers.workforce_scaled"
        self.delete(key,path)

    def add_employee(self, type, amount):
        path = "building_modifiers.level_scaled"
        key = "building_employment_"+type+"_add"
        self.add(key,"=",amount,path, True)

    def remove_employee(self, type):
        path = "building_modifiers.level_scaled"
        key = "building_employment_"+type+"_add"
        self.delete(key,path)


        
