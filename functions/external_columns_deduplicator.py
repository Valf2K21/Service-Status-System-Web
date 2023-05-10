# import dependencies
import pandas as pd

# FOURTH PART OF PROGRAM CODE: USER-DEFINED FUNCTION FOR EXTERNAL COLUMNS DEDUPLICATOR (CONFIRMED WORKING)
# create a function that will check and remove external column duplicates of the passed columnDataframe
def external_columns_deduplicator(columnData, external1, external2, columnName, external1Name, external2Name):
    # debugging: print a message telling that this function is successfully called
    # print('external_columns_deduplicator() function called successfully')
    
    # if the currently processed columnDf is not empty, proceed with the duplicate checking process
    if(not columnData.empty):
        # if the passed external1 is not empty, proceed with the duplicate checking process of columnDf and external1
        if(not external1.empty):
            # debugging: variable to keep track of dropped duplicates count
            # duplicatesNo = 0
            
            # for-loop that will loop through the unique content of the passed dataframe's 'plateno' column
            for plate in columnData['plateno'].unique():
                # create two new dataframes, one for columnData and another for external1, containing rows of detected duplicates of the current plate
                plateDuplicates1 = columnData[columnData['plateno'] == plate]
                plateDuplicates2 = external1[external1['plateno'] == plate]
                
                # if the number of found duplicates stored in the two plateDuplicates variables are both greater than 0...
                if len(plateDuplicates1) > 0 and len(plateDuplicates2) > 0:
                    # ...use .max() function to grab the maximum jrno values of the duplicates in the two plate_duplicates dataframes, then grab store the higher value in highest_jrno...
                    highestJrno = max(plateDuplicates1['jrno'].max(), plateDuplicates2['jrno'].max())

                    # ...then a for-loop will compare plateDuplicates1 unique element's jrno with highestJrno
                    for index, row in plateDuplicates1.iterrows():
                        # if the current row's jrno is less than the highestJrno...
                        if row['jrno'] < highestJrno:
                            # ...drop the current row to keep the unique element with the highest jrno
                            columnData = columnData.drop(index)
                            
                            # debugging: print the row that will be dropped, and add 1 to the current dropped duplicates counter
                            # print('Will drop ' + str(row))
                            # duplicatesNo = duplicatesNo + 1
            
            # debugging: print final counts of dropped duplicates between the main column and external1 dataframes
            # print('Number of removed ' + columnName + ' to ' + external1Name + ' column duplicates: ' + str(duplicatesNo) + '\n')
        
        # if the passed external2 is not empty, proceed with the duplicate checking process of columnDf and external2
        if(not external2.empty):
            # debugging: variable to keep track of dropped duplicates count
            # duplicatesNo = 0
            
            # for-loop that will loop through the unique contents of the passed dataframe's 'plateno' column
            for plate in columnData['plateno'].unique():
                # create two new dataframes, one for columnData and another for external2, containing rows of detected duplicates of the current plate
                plateDuplicates1 = columnData[columnData['plateno'] == plate]
                plateDuplicates3 = external2[external2['plateno'] == plate]
                
                # if the number of found duplicates stored in the two plateDuplicates variables are both greater than 0...
                if len(plateDuplicates1) > 0 and len(plateDuplicates3) > 0:
                    # ...use .max() function to grab the maximum jrno values of the duplicates in the two plateDuplicates dataframes, then grab store the higher value in highest_jrno...
                    highestJrno = max(plateDuplicates1['jrno'].max(), plateDuplicates3['jrno'].max())

                    # ...then a for-loop will compare plateDuplicates1 unique element's jrno with highestJrno
                    for index, row in plateDuplicates1.iterrows():
                        # if the current row's jrno is less than the highestJrno...
                        if row['jrno'] < highestJrno:
                            # ...drop the current row to keep the unique element with the highest jrno
                            columnData = columnData.drop(index)
                            
                            # debugging: print the row that will be dropped, and add 1 to the current dropped duplicates counter
                            # print('Will drop ' + str(row))
                            # duplicatesNo = duplicatesNo + 1
            
            # debugging: print final counts of dropped duplicates between the main column and external2 dataframes
            # print('Number of removed ' + columnName + ' to ' + external2Name + ' column duplicates: ' + str(duplicatesNo) + '\n')
    
    # return processed dataframe of a column, now free of duplicates when compared with other columns
    return columnData