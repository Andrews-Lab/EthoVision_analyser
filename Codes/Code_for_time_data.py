def code_for_time_data(import_location, export_location, behaviours_results, behaviours_heading, 
                       find_overlap_with_zone, zone=''):

    import os
    import pandas as pd    
    from tqdm import tqdm
    
    print('Start creating time data.')
    
    export_name = 'Time Data.csv'    
    
    # Create a dataframe for the results.
    
    all_results = pd.DataFrame({'Filename':[]})
    for behaviour in behaviours_heading:
        all_results[behaviour+' (secs)'] = []
    all_results['Total (secs)'] = []
    
    # Import each raw data excel file in import_location.
    
    import_files = [file for file in os.listdir(import_location) if 
                    (file.endswith(".xlsx") and file.startswith("~$")==False)]
    
    for filename in tqdm(import_files, ncols=70):

        # Name the output excel file.
        
        import_name = filename
        import_destination = import_location + import_name
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
        
        # Create the data.
        
        df_results = {'Filename':[filename]}
        for behaviour in behaviours_heading:
            df_results[behaviour+' (secs)'] = [0]
        df_results['Total (secs)'] = [0]
        
        df_results[''] = ['']
        for behaviour in behaviours_heading:
            df_results[behaviour+' (%)']    = [0]
        df_results['Total (%)'] = [0]
            
        for i in range(len(df['Trial time'])-1):

            for behaviour in behaviours_heading:
                
                if find_overlap_with_zone == True and df.at[i,zone] != 1:
                    break
                
                if df.at[i,behaviour] == 1: 
                    df_results[behaviour+' (secs)'] += (df.at[i+1,'Trial time'] 
                                                        - df.at[i,'Trial time'])
                    break
        
        # Add the total time in secs column.
        total = 0
        for behaviour in behaviours_heading:
            total += df_results[behaviour+' (secs)'][0]
        df_results['Total (secs)'] = [total]
        
        # Add the percentage times of each behaviour.
        df_results[''] = ['']
        total = 0
        for behaviour in behaviours_heading:
            df_results[behaviour+' (%)'] = ((df_results[behaviour+' (secs)'][0] * 100) 
                                             / df_results['Total (secs)'][0])
            total                       += ((df_results[behaviour+' (secs)'][0] * 100) 
                                             / df_results['Total (secs)'][0])
        df_results['Total (%)'] = total
        
        # Add a row to the output excel file.
        
        all_results = pd.concat([all_results, pd.DataFrame(df_results)])
        #print(filename + ' done')
            
    # Export the data.
    
    all_results.to_csv(export_destination, index=False, header=list(all_results.columns))