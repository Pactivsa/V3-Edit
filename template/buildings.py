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
    
    def set_texture(self, texture_path):
        self.add("texture", "=", texture_path)

    def set_city_type(self, city_type):
        self.add("city_type", "=", city_type)

    def set_lpm(self, lpm):
        self.add("level_per_mesh", "=", lpm)

    # unlocking_technologies
    def add_unlocking_technology(self, tech):
        self.insert(tech, "unlocking_technologies",True)

    def remove_unlocking_technology(self, tech):
        self.delete(tech, "unlocking_technologies")

    def get_unlocking_technologies(self):
        return self.trace("unlocking_technologies")
    
    # production_method_groups
    def add_production_method_group(self, pmg):
        self.insert(pmg, "production_method_groups",True)

    def remove_production_method_group(self, pmg):
        self.delete(pmg, "production_method_groups")

    def get_production_method_groups(self):
        return self.trace("production_method_groups")
    
    # required_construction
    def set_required_construction(self, construction):
        self.add("required_construction", "=", construction)

    def get_required_construction(self):
        return self.trace("required_construction")
    

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
        if goods_dict is None:
            return result
        # 解析存在的输入
        for good in goods_dict:
            if good.startswith("goods_input_"):
                good_name = good.split("_")[2]
                result[good_name] = goods_dict[good][1]

        return result
    
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

    def get_level_scaled(self):
        return self.trace("building_modifiers.level_scaled")
    
    def get_unscaled(self):
        return self.trace("building_modifiers.unscaled")

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


        
