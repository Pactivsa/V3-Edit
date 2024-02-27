import os
from template.buildings import *
from template.goods import *
from utils.template import BaseManager

GamePath = r"D:\Steam\steamapps\common\Victoria 3"

pm_manager = BaseManager(Pm)
pm_manager.init_from_folder(os.path.join(GamePath, "game", "common", "production_methods"))

pm_manager.output("pm_manager.txt")

pm_test:Pm = pm_manager.get_property("test") 

pm_test.set_texture("test_texture_path")

pm_test.add_input("fabric", 1)
pm_test.add_output("oil", 1)

pm_test.output("pm_test.txt")

pm_leblanc_process:Pm = pm_manager.get_property("pm_leblanc_process",False)

print(pm_leblanc_process.get_inputs())

pm_leblanc_process.remove_input("fertilizer")

pm_manager.output("pm_manager.txt")




