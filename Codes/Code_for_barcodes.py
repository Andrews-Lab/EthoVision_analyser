def code_for_barcodes(import_location, export_location, behaviours_results, behaviours_heading, 
                      behaviours_colors, find_overlap_with_zone, zone=''):
    
    import os
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    import numpy as np
    from tqdm import tqdm
    
    print('Start creating barcodes.')
    
    # Add a white color for no behaviour.
    temp_list = list(behaviours_colors)
    temp_list.append('#ffffff')
    behaviours_colors = tuple(temp_list)
    
    # Import each raw data excel file in import_location.
    
    import_files = [file for file in os.listdir(import_location) if 
                    (file.endswith(".xlsx") and file.startswith("~$")==False)]
    
    for filename in tqdm(import_files, ncols=70):
    
        # Name the output excel file.
        
        import_name = filename
        import_destination = import_location + import_name
        export_name = 'Barcode for ' + filename + '.png'
        export_destination = export_location + export_name
        
        # Read the excel data.

        df = pd.read_excel(import_destination, sheet_name=0)
        if list(df[:0])[0] == 'Number of header lines:':
            num_headers = int(list(df[:0])[1])
        rows_skip = list(range(0,num_headers-2)) + [num_headers-1]
        if find_overlap_with_zone == True:
            headings = ['Trial time'] + list(behaviours_results) + [zone]
        elif find_overlap_with_zone == False:
            headings = ['Trial time'] + list(behaviours_results)
        df = pd.read_excel(import_destination, sheet_name=0, usecols=headings, 
                           skiprows=rows_skip)
        
        # Rename the columns.
        for i in range(len(behaviours_results)):
            df = df.rename(columns = {behaviours_results[i]: behaviours_heading[i]})
            
        # Data for the barcode.
        color_dict = {}
        counter = 0
        for behaviour in behaviours_heading:
            color_dict[behaviour] = counter
            counter += 1
        # If there is no behaviour, the color should be white.
        df['Color values'] = [counter]*len(df['Trial time'])
        
        # Create the data.
                    
        for i in range(len(df['Trial time'])):

            for behaviour in behaviours_heading:
                
                if find_overlap_with_zone == True and df.at[i,zone] != 1:
                    break
                
                if df.at[i,behaviour] == 1:
                    df.at[i,'Color values'] = color_dict[behaviour]
                    break

        # Create the plots.
        plt.figure(figsize=(9, 2.5))
        sns.heatmap(data=np.array([df['Color values']]),cmap=list(behaviours_colors),cbar=False,
                    xticklabels=False, yticklabels=False, vmin=0, vmax=len(behaviours_colors))
        plt.savefig(export_destination, bbox_inches='tight', pad_inches=0.005)
        #plt.show()
        #print(filename + ' done')
        
    # Export the legend.
    table_text = []
    table_colors = []
    for behaviour in behaviours_heading:
        table_text.append(['',behaviour])
        table_colors.append([behaviours_colors[color_dict[behaviour]],'w'])
    # https://towardsdatascience.com/simple-little-tables-with-matplotlib-9780ef5d0bc4
    plt.figure(linewidth=2,tight_layout={'pad':1},dpi=300)
    the_table=plt.table(cellText=table_text, cellColours=table_colors, cellLoc='center', 
                        loc='center', colWidths=[0.25,0.5])
    the_table.scale(1, 1.5)
    ax = plt.gca()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.box(on=None)
    plt.suptitle('Legend',fontsize=30)
    plt.draw()
    fig = plt.gcf()
    plt.savefig(export_location + 'Legend' + '.png')
