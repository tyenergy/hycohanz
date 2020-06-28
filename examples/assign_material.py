from __future__ import division

import hycohanz as hfss

input('Press "Enter" to connect to HFSS.>')

[oAnsoftApp, oDesktop] = hfss.setup_interface()

input('Press "Enter" to create a new project.>')

oProject = hfss.new_project(oDesktop)

input('Press "Enter" to insert a new DrivenModal design named HFSSDesign1.>')

oDesign = hfss.insert_design(oProject, "HFSSDesign1", "DrivenModal")

input('Press "Enter" to set the active editor to "3D Modeler" (The default and only known correct value).>')

oEditor = hfss.set_active_editor(oDesign)

input('Press "Enter" to insert some sphere properties into the design.>')

hfss.add_property(oDesign, "xcenter", hfss.Expression("1m"))
hfss.add_property(oDesign, "ycenter", hfss.Expression("2m"))
hfss.add_property(oDesign, "zcenter", hfss.Expression("3m"))
hfss.add_property(oDesign, "diam", hfss.Expression("1m"))

input('Press "Enter" to draw a sphere using the properties.>')

sphere1 = hfss.create_sphere(
    oEditor,   
    hfss.Expression("xcenter"), 
    hfss.Expression("ycenter"), 
    hfss.Expression("zcenter"), 
    hfss.Expression("diam")/2)

input('''Press "Enter" to change the sphere's material to copper>''')

hfss.assign_material(oEditor, [sphere1], MaterialName="copper")

input('Press "Enter" to quit HFSS.>')

hfss.quit_application(oDesktop)

del oEditor
del oDesign
del oProject
del oDesktop
del oAnsoftApp
