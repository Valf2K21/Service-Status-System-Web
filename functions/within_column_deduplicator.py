# import dependencies
import pandas as pd

# THIRD PART OF PROGRAM CODE: USER-DEFINED FUNCTION FOR WITHIN COLUMN DEDUPLICATOR (CONFIRMED WORKING)
# create a function that will check and remove in-column duplicates of the passed columnDataframe
def within_column_deduplicator(columnData, columnName):
    # debugging: print a message telling that this function is successfully called
    # print('within_column_dedpulicator() function called successfully')
    
    # if the currently processed columnDf is not empty, proceed with the duplicate checking process
    if(not columnData.empty):
        # debugging: variable to keep track of dropped duplicates count
        # duplicatesNo = 0
        
        # for-loop that will loop through the unique content of the passed dataframe's 'plateno' column
        for plate in columnData['plateno'].unique():
            # create a new dataframe containing rows of detected duplicates of the current plate
            plateDuplicates = columnData[columnData['plateno'] == plate]

            # if the number of found duplicates stored in plateDuplicates is greater than 0...
            if len(plateDuplicates) > 0:
                # ...temporarily grab the jrno value of the current duplicate...
                highestJrno = plateDuplicates['jrno'].iloc[0]

                # ...then a for-loop will compare plateDuplicates unique element's jrno with highest_jrno
                for index, row in plateDuplicates.iterrows():    # .iterrows() function is used to iterate through the rows of plate_duplicates dataframe
                    # if the current row's jrno is less than the highestJrno...
                    if row['jrno'] < highestJrno:
                        # ...drop the current row to keep the unique element with the highest jrno
                        columnData = columnData.drop(index)
                        
                        # debugging: print the row that will be dropped, and add 1 to the current dropped duplicates counter
                        # print('Will drop ' + str(row))
                        # duplicatesNo = duplicatesNo + 1
        
        # debugging: print final counts of dropped duplicates
        # print('Number of removed ' + columnName + ' in-column duplicates: ' + str(duplicatesNo) + '\n')

    # return processed dataframe of a column, now free of duplicates within itself
    return columnData