from utils.template import BaseTemplate
from template.goods import Goods
from typing import Literal, Union
import pandas as pd

class Buildings_group(BaseTemplate):
    def __init__(self, name, if_init=False):
        original_file = "template/original/buildings_groups.txt"
        super().__init__(name, original_file, if_init)

    def _clone(self, name):
        return Buildings_group(name, self.if_init)


class Buildings(BaseTemplate):
    def __init__(self, name, if_init=False):
        original_file = "template/original/buildings.txt"
        super().__init__(name, original_file, if_init)

    def _clone(self, name):
        return Buildings(name, self.if_init)

    def set_texture(self, texture_path):
        self.add("texture", "=", texture_path)

    def set_city_type(self, city_type):
        self.add("city_type", "=", city_type)

    def set_lpm(self, lpm):
        self.add("level_per_mesh", "=", lpm)

    # building_group
    def set_building_group(self, bg: Union[str, Buildings_group]) -> None:
        if isinstance(bg, Buildings_group):
            bg = bg.name
        self.add("building_group", "=", bg)

    def get_building_group(self) -> str:
        return self.trace("building_group")

    # unlocking_technologies
    def add_unlocking_technology(self, tech):
        self.insert(tech, "unlocking_technologies", True)

    def remove_unlocking_technology(self, tech):
        self.delete(tech, "unlocking_technologies")

    def get_unlocking_technologies(self) -> list:
        return self.trace("unlocking_technologies")

    # production_method_groups
    def add_production_method_group(self, pmg):
        self.insert(pmg, "production_method_groups", True)

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
    def __init__(self, name, if_init=False, Buildings: Buildings = None):
        original_file = "template/original/production_method_groups.txt"
        super().__init__(name, original_file, if_init)
        if Buildings:
            self.bind(Buildings)

    def bind(self, Building: Buildings):
        Building.insert(self.name, "production_methods", True)

    def _clone(self, name):
        return Pmg(name, self.if_init)

    def add_pm(self, pm_name):
        self.insert(pm_name, "production_methods", True)

    def rm_pm(self, pm_name):
        self.delete(pm_name, "production_methods")

    def get_pms(self) -> list:
        return self.trace("production_methods")

    def set_texture(self, texture_path):
        self.add("texture", "=", texture_path)


class Pm(BaseTemplate):
    def __init__(self, name, if_init=False, Pmg: Pmg = None):
        original_file = "template/original/production_methods.txt"
        super().__init__(name, if_init)
        if Pmg:
            self.bind(Pmg)

    def bind(self, Pmg: Pmg):
        Pmg.insert(self.name, "production_methods", True)

    def _clone(self, name):
        return Pm(name, self.if_init)

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

        key = "goods_input_" + good + "_add"
        self.add(key, "=", amount, path, True)

    def remove_input(self, good):
        key = "goods_input_" + good + "_add"
        path = "building_modifiers.workforce_scaled"
        self.delete(key, path)

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

        key = "goods_output_" + good + "_add"
        self.add(key, "=", amount, path, True)

    def get_level_scaled(self):
        return self.trace("building_modifiers.level_scaled")

    def get_unscaled(self):
        return self.trace("building_modifiers.unscaled")

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

    def remove_output(self, good):
        key = "goods_output_" + good + "_add"
        path = "building_modifiers.workforce_scaled"
        self.delete(key, path)

    def add_employee(self, type, amount):
        path = "building_modifiers.level_scaled"
        key = "building_employment_" + type + "_add"
        self.add(key, "=", amount, path, True)

    def remove_employee(self, type):
        path = "building_modifiers.level_scaled"
        key = "building_employment_" + type + "_add"
        self.delete(key, path)
