import os

from utils.backend import BackendManager
from API.building import *
from template.buildings import *


GamePath = r"D:\Steam\steamapps\common\Victoria 3\game"
ModPath = r"mod\test"

BM = BackendManager(GamePath, ModPath)

building_textile_mills ,rc = get_building_detail(BM, "building_textile_mills")

print(BM.get_part("pmgs"))


