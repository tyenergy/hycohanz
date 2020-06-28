import hycohanz as hfss

input('Press "Enter" to connect to HFSS.>')

with hfss.App() as App:
    input('Press "Enter" to create a new project.>')
    
    with hfss.NewProject(App.oDesktop) as P:
        
        input('Press "Enter" to insert a new DrivenModal design named HFSSDesign1.>')
        
        with hfss.InsertDesign(P.oProject, "HFSSDesign1", "DrivenModal") as D:
            input('Press "Enter" to insert a new property into the design named "length", having a value of "1m".>')
            
            hfss.add_property(D.oDesign, "length", hfss.Expression("1m"))
            
            input('Press "Enter" to quit HFSS.>')
