import os
import subprocess
import xml.etree.ElementTree as ET
import Xml_change_followtrajectory
import Xml_change_dur
import Xml_changetools
import shutil
file_name = input("请输入文件名：")
xosc_name = file_name + '.xosc'
osgb_name = file_name + '.osgb'
geojson_name = file_name + '.geojson'
xodr_name = file_name + '.xodr'
file_path = r"C:\IPG\RoadRunner R2022b\Test\Exports\\" + xosc_name
osgb_path = r"C:\IPG\RoadRunner R2022b\Test\Exports\\" + osgb_name
testrun_file = r"C:\CM_Projects\PROJECTNAME\Data\TestRun\\" + file_name
xodr_path = r"C:\IPG\RoadRunner R2022b\Test\Exports\\" + xodr_name
shutil.copy(osgb_path,'C:\CM_Projects\PROJECTNAME\Data_osc\\')
shutil.copy(file_path,'C:\CM_Projects\PROJECTNAME\Data_osc\\')
shutil.copy(xodr_path,'C:\CM_Projects\PROJECTNAME\Data_osc\\')


tree = ET.ElementTree(file=file_path)
root = tree.getroot()


duration=0
for i in root.findall('.//Condition'):
    if i.get('name')=="Duration":
        duration+=1
#1.Condition类型为duration condition
if duration!=0:
    Xml_change_dur.dur(file_name)

#2.FollowTrajectory
elif root.find('.//FollowTrajectoryAction') is not None and len(root.findall('.//Private')) >1:
    Xml_changetools.change(file_name)
    print('Xml_changetools is running')
    Xml_change_followtrajectory.tra(file_name)
    print('Xml_change_followtrajectory is running')
elif root.find('.//FollowTrajectoryAction') is not None and len(root.findall('.//Private')) ==1:
    Xml_change_followtrajectory.tra(file_name)

#3.Condition类型为simulationtime condition
else:
    Xml_changetools.change(file_name)
    print('Xml_changetools is running')