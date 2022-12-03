def code_for_bout_data(import_location, export_location, behaviours_results, behaviours_heading):
    
    import os
    import pandas as pd
    from tqdm import tqdm
    
    print('Start creating bout data.')
    
    include_extra_stats = False
    export_name = 'Bout data.csv'
    
    # Create a dataframe for the results.
    
    all_results = pd.DataFrame({'Filename':[]})
    for behaviour in behaviours_heading:
        all_results[behaviour+' (bout start time in secs)']       = []
        all_results[behaviour+' (bout end time in secs)']         = []
        all_results[behaviour+' (bout lengths in secs)']          = []
        all_results[behaviour+' (bout frequency)']                = []
    all_results['Number of transitions (sum of all frequencies)'] = []
    all_results['']                                               = []
    for behaviour in behaviours_heading:
        all_results[behaviour+' (sum of bout lengths in secs)']   = []
    all_results['Total time (sum of all bout lengths in secs)']   = []
    
    # Remove the raw bout data
    if include_extra_stats == False:
        for behaviour in behaviours_heading:
            all_results.pop(behaviour+' (bout start time in secs)')
            all_results.pop(behaviour+' (bout end time in secs)')
            all_results.pop(behaviour+' (bout lengths in secs)')
    
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
        find_overlap_with_zone = False
        if find_overlap_with_zone == True:
            headings = ['Trial time'] + list(behaviours_results) + [zone]
        elif find_overlap_with_zone == False:
            headings = ['Trial time'] + list(behaviours_results)
        df = pd.read_excel(import_destination, sheet_name=0, usecols=headings, 
                           skiprows=rows_skip)
        
        # Rename the columns.
        for i in range(len(behaviours_results)):
            df = df.rename(columns = {behaviours_results[i]: behaviours_heading[i]})
        
        # Create the bout data.
        
        df_results = {'Filename':[filename]}
        for behaviour in behaviours_heading:
            df_results[behaviour+' (bout start time in secs)']     = []
            df_results[behaviour+' (bout end time in secs)']       = []
            df_results[behaviour+' (bout lengths in secs)']        = []
            df_results[behaviour+' (bout frequency)']              = [0]
        df_results['Number of transitions (sum of all frequencies)'] = [0]
        df_results['']                                               = ['']
        for behaviour in behaviours_heading:
            df_results[behaviour+' (sum of bout lengths in secs)'] = [0]
        df_results['Total time (sum of all bout lengths in secs)'] = [0]
            
        for i in range(len(df['Trial time'])):
            
            for behaviour in behaviours_heading:
                
                # Make the behaviours mutually exclusive for this time point.
                if df.at[i,behaviour] == 1:
                    rest_behav = [behav for behav in behaviours_heading if behav!=behaviour]
                    for behav in rest_behav:
                        df.at[i,behav] = 0
                
                # Record the start time of a new behaviour.
                if df.at[i, behaviour] == 1 and (i==0 or df.at[i-1, behaviour]==0):
                    start_point = df.at[i,'Trial time']
                    df_results[behaviour+' (bout start time in secs)'].append(start_point)
                
                # Record the end time of a previous behaviour.
                if ((df.at[i, behaviour]==1 and i==len(df['Trial time'])-1) or
                    (df.at[i, behaviour]==0 and (i!=0 and df.at[i-1, behaviour]==1))):
                    end_point = df.at[i,'Trial time']
                    df_results[behaviour+' (bout end time in secs)'].append(end_point)
                    start_point = df_results[behaviour+' (bout start time in secs)'][-1]
                    df_results[behaviour+' (bout lengths in secs)'].append(end_point - start_point)
                    df_results[behaviour+' (bout frequency)'][0] += 1
                    df_results['Number of transitions (sum of all frequencies)'][0] += 1
                    df_results[behaviour+' (sum of bout lengths in secs)'][0] += (end_point - start_point)
                    df_results['Total time (sum of all bout lengths in secs)'][0] += (end_point - start_point)

        # Add a row to the output excel file.
        
        # Remove the raw bout data.
        if include_extra_stats == False:
            for behaviour in behaviours_heading:
                df_results.pop(behaviour+' (bout start time in secs)')
                df_results.pop(behaviour+' (bout end time in secs)')
                df_results.pop(behaviour+' (bout lengths in secs)')
            
        df_results = pd.DataFrame.from_dict(df_results, orient='index')
        df_results = df_results.transpose()
        all_results = pd.concat([all_results, pd.DataFrame(df_results)])
        #print(filename + ' done')
            
    # Export the data.
    
    all_results.to_csv(export_destination, index=False, header=list(all_results.columns))