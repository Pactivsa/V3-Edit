from utils.backend import BackendManager
from template.buildings import *


def get_buildings(BM: BackendManager):
    mods_list, raw_list = BM.get_part("buildings")
    ans = mods_list + raw_list
    return ans.sort()


def get_building_detail(BM: BackendManager, name: str):
    buildings, source = BM.get_part_detail("buildings", name)
    return buildings, source


def get_goods_detail(BM: BackendManager, name: str):
    goods, source = BM.get_part_detail("goods", name)
    return goods, source


def get_pm_detail(BM: BackendManager, name: str):
    pm, source = BM.get_part_detail("pm", name)
    pm: Pm
    pm_dict = {
        "name": pm.name,
        "input": pm.get_inputs(),
        "output": pm.get_outputs(),
        "level": pm.get_level_scaled(),
        "unscaled": pm.get_unscaled(),
        "texture": pm.get_texture(),
        "is_default": pm.get_is_default(),
        "country_modifiers_workforce": pm.get_country_modifiers_workforce(),
        "country_modifiers_level": pm.get_country_modifiers_level(),
        "country_modifiers_unscaled": pm.get_country_modifiers_unscaled(),
        "state_modifiers_workforce": pm.get_state_modifiers_workforce(),
        "state_modifiers_level": pm.get_state_modifiers_level(),
        "state_modifiers_unscaled": pm.get_state_modifiers_unscaled(),
        "timed_modifiers": pm.get_timed_modifiers(),
        "required_input_goods": pm.get_required_input_goods(),
        "unlocking_laws": pm.get_unlocking_laws(),
        "unlocking_technologies": pm.get_unlocking_technologies(),
        "unlocking_production_methods": pm.get_unlocking_production_methods(),
        "unlocking_global_technologies": pm.get_unlocking_global_technologies(),
        "ai_weight": pm.get_ai_weight(),
        "pollution_generation": pm.get_pollution_generation()
    }
    return pm_dict, source
