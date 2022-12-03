#-----------------------------------------------------------------------------

# Choose the default values for the GUI (dv).

dv = {} # Ignore this.

# Choose the import and export locations.
# Note that these locations should not have a slash at the end.
dv['Import location'] = 'C:/Users/hazza/Desktop/Manual scoring for Felicia 24-12-21/Import files'
dv['Export location'] = 'C:/Users/hazza/Desktop/Manual scoring for Felicia 24-12-21/Export data'

# Choose the number of behaviours and whether to find overlap with a zone.
dv['No behaviours'] = 4
dv['Find overlap'] = 'True' # Note that this should be a string of 'True' or 'False'.

# Choose the excel names, custom names and barcode colours for each behaviour.
dv['Excel  name for zone'] = 'In zone(Arena / center-point)'
dv['Custom name for zone'] = 'Arena'
dv['Excel  names for behaviours'] = ['Walking(Mutually exclusive)', 'Stationary(Mutually exclusive)', 
                                     'Rearing(Mutually exclusive)', 'Grooming(Mutually exclusive)']
dv['Custom names for behaviours'] = ['Walking', 'Stationary', 'Rearing', 'Grooming']
dv['Colours for behaviours']      = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

# Choose the types of analysis to run based on these inputs.
dv['Create time data'] = 'True'
dv['Create bout data'] = 'True'
dv['Create barcodes']  = 'True'
    
#-----------------------------------------------------------------------------












# Import the modules and codes in the same folder.
import matplotlib.pyplot as plt
import matplotlib.colors as col
import PySimpleGUI as sg
import webbrowser
from Code_for_time_data import code_for_time_data
from Code_for_bout_data import code_for_bout_data
from Code_for_barcodes import code_for_barcodes

no_runs = 1 # One run is defined as a one loop through all the GUI windows.
every = {} # The input values for every run are stored here.

while True:
    
    # Choose the import and export locations, number of behaviours and whether 
    # to measure overlap with a zone.
    
    # Create the GUI.
    sg.theme("DarkTeal2")
    layout = [
        [sg.T("")], [sg.Text("Choose a folder for the import location"), 
                     sg.Input(key="Import" ,enable_events=True,
                              default_text=dv['Import location']), 
                     sg.FolderBrowse(key="Import2")],
        [sg.T("")], [sg.Text("Choose a folder for the export location"), 
                     sg.Input(key="Export" ,enable_events=True,
                              default_text=dv['Export location']), 
                     sg.FolderBrowse(key="Export2")],
        [sg.T("")], [sg.Text("How many behaviours?"), 
                     sg.Combo(list(range(1,15+1)),key="Num",enable_events=True,
                              default_value=dv['No behaviours'])],
        [sg.T("")], [sg.Text("Find overlap with a zone?"), 
                     sg.Combo(['True','False'],key="Overlap",enable_events=True,
                              default_value=dv['Find overlap'])],
        [sg.T("")], [sg.Button("Submit")]
              ]
    window = sg.Window('Manual scoring GUI', layout)
    
    # Convert 'True' to boolean True and 'False' to boolean False.
    def bool_check(value):
        if value == 'True':
            return(True)
        elif value == 'False':
            return(False)
        else:
            print('Make sure True or False is used.\n')
            exit()
    
    # Assign the values in the GUI to variables.
    val = {} # The input values, as opposed to the default values, are stored here.
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event=="Exit":
            window.close()
            exit()
        elif event == "Submit":
            val['Import location'] = values["Import"] + '/'
            val['Export location'] = values["Export"] + '/'
            val['No behaviours']  = values["Num"]
            val['Find overlap'] = bool_check(values["Overlap"])
            val['Excel  name for zone'] = ''
            window.close()
            break
    
    print('\nInputs for run '+str(no_runs))
    print('Import location is ' + val['Import location'])
    print('Export location is ' + val['Export location'])
    print('The number of behaviours is ' + str(val['No behaviours']))
    if val['Find overlap'] == True:
        print('Find overlap with a zone')
    elif val['Find overlap'] == False:
        print('Do not find overlap with a zone')
    
    # Choose the names of the behaviours in excel and the names and colors for the output.
    
    # Create the GUI.
    sg.theme("DarkTeal2")
    message =  "Put the behaviours in the order of importance. "
    message += "If 2 happen at the same time, only the first one will be counted. "
    message += "If the behaviours are mutually exclusive, the order does not matter."
    layout = [[sg.Text(message)],
              [sg.Text("Use the default colors or click this link to find HEX values. "
                       "Make sure you include the # at the start:"),
               sg.Text("https://coolors.co/", key="Link", enable_events=True)]]
    
    for i in range(1,len(dv['Excel  names for behaviours'])+1):
        dv['Excel  name for behaviour'+str(i)] = dv['Excel  names for behaviours'][i-1]
        dv['Custom name for behaviour'+str(i)] = dv['Custom names for behaviours'][i-1]
        dv['Colour for behaviour'+str(i)]      = dv['Colours for behaviours'][i-1]
    
    if val['Find overlap'] == True:
        layout += [[sg.T("")], [sg.Text("Excel name for zone         "), 
            sg.Input(key="Zone",enable_events=True,default_text=dv['Excel  name for zone']),
            sg.Text("Custom name for zone         "), 
            sg.Input(key="cZone",enable_events=True,default_text=dv['Custom name for zone'])]]
    for i in range(1,val['No behaviours']+1):
        if i <= dv['No behaviours']:
            layout += [[sg.T("")], [sg.Text("Excel name for behaviour "+str(i)), 
                sg.Input(key="Behaviour"+str(i),enable_events=True,
                         default_text=dv['Excel  name for behaviour'+str(i)]),
                sg.Text("Custom name for behaviour "+str(i)), 
                sg.Input(key="cBehaviour"+str(i),enable_events=True,
                         default_text=dv['Custom name for behaviour'+str(i)]),
                sg.Text("Choose color"),
                sg.Input(key="Color"+str(i),enable_events=True,
                         default_text=dv['Colour for behaviour'+str(i)])]]
        else:
            layout += [[sg.T("")], [sg.Text("Excel name for behaviour "+str(i)), 
                sg.Input(key="Behaviour"+str(i),enable_events=True,default_text=''),
                sg.Text("Custom name for behaviour "+str(i)), 
                sg.Input(key="cBehaviour"+str(i),enable_events=True,default_text=''),
                sg.Text("Choose color"),
                sg.Input(key="Color"+str(i),enable_events=True,default_text='')]]        
                           
    layout += [[sg.T("")],[sg.Button("Submit")]]
    window = sg.Window('Manual scoring GUI', layout)
    
    # Assign the values in the GUI to variables.
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event=="Exit":
            window.close()
            exit()
        elif event == "Link":
            webbrowser.open(r'https://coolors.co/')
        elif event == "Submit":
            if val['Find overlap'] == True:
                val['Excel  name for zone'] = values["Zone"]
                val['Custom name for zone'] = values["cZone"]
            val['Excel  names for behaviours'] = []
            val['Custom names for behaviours'] = []
            val['Colours for behaviours']  = []
            for i in range(1,val['No behaviours']+1):
                val['Excel  names for behaviours'].append(values["Behaviour"+str(i)])
                val['Custom names for behaviours'].append(values["cBehaviour"+str(i)])
                val['Colours for behaviours'].append(values["Color"+str(i)])
            val['Excel  names for behaviours'] = tuple(val['Excel  names for behaviours'])
            val['Custom names for behaviours'] = tuple(val['Custom names for behaviours'])
            val['Colours for behaviours']      = tuple(val['Colours for behaviours'])
            window.close()
            break
    
    print('Analyse the ' + str(val['No behaviours']) + ' behaviours in order of importance: ')
    for i in range(val['No behaviours']):
        print(str(i+1) + ') ' + val['Custom names for behaviours'][i] + 
              ' with HEX color ' + val['Colours for behaviours'][i])
    if val['Find overlap'] == True:
        print('Find the overlap of these behaviours with ' + val['Custom name for zone'])
    
    # Choose the codes to run.
    
    # Create the GUI.
    sg.theme("DarkTeal2")
    message1 = "Choose the types of analysis that should be done."
    message2 = "Click 'Submit' to run this analysis with the current inputs."
    message3 = ("Click 'Queue' to add this analysis to a queue, go back to the "
                "start and decide on more things to run.")
    message4 = "Make sure you use a different export location for each run in the queue." 
    layout = [[sg.Text(message1)], [sg.Text(message2)], [sg.Text(message3)], [sg.Text(message4)], 
        [sg.T("")], [sg.Text("Create time data"), 
                     sg.Combo(['True','False'],key="Time data",enable_events=True,
                              default_value=dv['Create time data'])],
        [sg.T("")], [sg.Text("Create bout data"), 
                     sg.Combo(['True','False'],key="Bout data",enable_events=True,
                              default_value=dv['Create bout data'])],
        [sg.T("")], [sg.Text("Create barcodes"),  
                     sg.Combo(['True','False'],key="Barcodes", enable_events=True,
                              default_value=dv['Create barcodes'])],
        [sg.T("")], [sg.Button("Submit"),sg.Text(116*" "),sg.Button("Queue")]]
    window = sg.Window('Manual scoring GUI', layout)
    
    # Based on the values in the GUI, choose which codes to run.
    arguments = {} # This is a list of the arguments needed for each function/code.
    arguments["Create time data"] = ['Import location','Export location',
                                     'Excel  names for behaviours', 'Custom names for behaviours',
                                     'Find overlap','Excel  name for zone']
    arguments["Create bout data"] = ['Import location','Export location',
                                     'Excel  names for behaviours','Custom names for behaviours']
    arguments["Create barcodes"]  = ['Import location','Export location',
                                     'Excel  names for behaviours','Custom names for behaviours',
                                     'Colours for behaviours','Find overlap','Excel  name for zone']
    
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event=="Exit":
            window.close()
            exit()
            break
        elif event == "Queue":
            val["Create time data"] = values["Time data"]
            val["Create bout data"] = values["Bout data"]
            val["Create barcodes"]  = values["Barcodes"]
            every["Run "+str(no_runs)] = val
            break
        elif event == "Submit":
            val["Create time data"] = values["Time data"]
            val["Create bout data"] = values["Bout data"]
            val["Create barcodes"]  = values["Barcodes"]
            every["Run "+str(no_runs)] = val
            
            # Run through all the recorded inputs in the queue.
            for run_no in every.keys():
                print('\n'+run_no)
                
                if every[run_no]["Create time data"] == "True":
                    arguments_list = [every[run_no][arg] for arg in arguments["Create time data"]]
                    code_for_time_data(*arguments_list)
        
                if every[run_no]["Create bout data"] == "True":
                    arguments_list = [every[run_no][arg] for arg in arguments["Create bout data"]]
                    code_for_bout_data(*arguments_list)
                    
                if every[run_no]["Create barcodes"] == "True":
                    arguments_list = [every[run_no][arg] for arg in arguments["Create barcodes"]]
                    code_for_barcodes(*arguments_list)
                    
    # Update the default values with the input values for the next run.
    for arg in val.keys():
        dv[arg] = val[arg]
    # PySimpleGUI does not display boolean values as default text entries.
    dv['Find overlap'] = str(dv['Find overlap'])
    # Remove the slashes at the end of file paths, because they will be added later on.
    dv['Import location'] = dv['Import location'][:-1]
    dv['Export location'] = dv['Export location'][:-1]
                    
    window.close()
    no_runs += 1