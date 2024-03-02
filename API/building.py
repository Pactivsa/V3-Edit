from utils.backend import BackendManager


def get_buildings(BM:BackendManager):
    mods_list, raw_list = BM.get_part("buildings")
    ans = mods_list + raw_list
    return ans.sort()

def get_building_detail(BM:BackendManager, name:str):
    buildings, source = BM.get_part_detail("buildings", name)
    return buildings, source

