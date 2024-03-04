from utils.backend import BackendManager
from template.buildings import *


def get_buildings(BM:BackendManager):
    mods_list, raw_list = BM.get_part("buildings")
    ans = mods_list + raw_list
    return ans.sort()

def get_bgs(BM:BackendManager):
    mods_list, raw_list = BM.get_part("bg")
    ans = mods_list + raw_list
    return ans.sort()

def get_pmgs(BM:BackendManager):
    mods_list, raw_list = BM.get_part("pmg")
    ans = mods_list + raw_list
    return ans.sort()

def get_pms(BM:BackendManager):
    mods_list, raw_list = BM.get_part("pm")
    ans = mods_list + raw_list
    return ans.sort()

def get_goods(BM:BackendManager):
    mods_list, raw_list = BM.get_part("goods")
    ans = mods_list + raw_list
    return ans.sort()

def get_building(BM:BackendManager, name:str):
    buildings, source = BM.get_part_detail("buildings", name)
    buildings: Buildings

    return buildings, source

def get_goods_detail(BM:BackendManager, name:str):
    goods, source = BM.get_part_detail("goods", name)
    return goods, source

def get_pm_detail(BM:BackendManager, name:str):
    pm, source = BM.get_part_detail("pm", name)
    pm: Pm
    pm_dict = {
        "name":pm.name,
        "input":pm.get_inputs(),
        "output":pm.get_outputs(),
        "level":pm.get_level_scaled(),
        "unscaled":pm.get_unscaled()
    }
    return pm_dict, source

    