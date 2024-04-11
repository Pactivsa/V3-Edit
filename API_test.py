import os

from utils.backend import BackendManager
from API.building import *
from template.buildings import *



GamePath = r"D:\Steam\steamapps\common\Victoria 3\game"
ModPath = r"mod\2890076329"
# ModPath = r"D:/Steam/steamapps/workshop/content/529340/2879974531"

from utils.BackendManager import BM

BM.setBM(GamePath, ModPath, readtype="rpALL")

mods,raws = BM.get_part("pmgs")

pm, raw_pm = BM.get_part("pm")
print(pm)
exit()

pm_header = Pm.structure_list()

k = 0

for pm_name in pm:
    single_pm, rc = BM.get_part_detail("pm", pm_name)
    single_pm:Pm
    print(single_pm)

    for i in range(len(pm_header)):
        try:
            i_data = single_pm[pm_header[i]]
            text = ''
        except Exception as e:
            print(single_pm)
            print(pm_name,":",pm_header[i])
            raise e
        
        if i_data is None:
            text = ''
        #如果是字典，每行放一个key = value字符串
        elif isinstance(i_data, dict):
            try:
                for j in i_data.keys():
                    temptext = '{} = {}\n'.format(j, i_data[j])
                    text = text + temptext
            except Exception as e:
                print(pm_name,":",pm_header[i],":",i_data)
                print(e)

        #如果是列表，每行放一个字符串
        elif isinstance(i_data, list):
            for j in i_data:
                temptext = '{}\n'.format(j)
                text = text + temptext

        #其他情况直接转为字符串
        else:
            text = str(i_data)






# BM = BackendManager(GamePath, ModPath)
# # print(BM.get_part("buildings"))
# # building_textile_mills ,rc = get_building_detail(BM, "building_textile_mills")

pmname = "pm_patent_stills"
pm_test, rc = BM.get_part_detail(part="pm", key=pmname)

pm_test: Pm
print(pm_test["workforce_scaled"])

