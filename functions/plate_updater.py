# import user-created dependencies
from data_query_and_dataframing import data_query_and_dataframing
from external_columns_deduplicator import external_columns_deduplicator
from plate_preparator import plate_preparator
from within_column_deduplicator import within_column_deduplicator

# SIXTH PART OF PROGRAM CODE: USER-DEFINED FUNCTION FOR PLATE UPDATER (CONFIRMED WORKING)
# BASICALLY THIS IS GET_TIME BUT FOR PLATE UPDATES, AND MUST RETURN PLATES OF EACH COLUMN
# create an automated destroy and recreate function for existing label widgets of plates
def plate_updater():
    # debugging: print a message telling that this function is successfully called
    # print('plate_updater() function called successfully')
    
    # call data_query_and_dataframing() function then unpack its returned tuple into their respective variables
    counterDf, progressDf, completedDf = data_query_and_dataframing()
    
    # now pass the columnDfs into the within_column_deduplicator() function to remove outdated duplicates within the respective columns
    counterDf = within_column_deduplicator(counterDf, 'Counter')
    progressDf = within_column_deduplicator(progressDf, 'In Progress')
    completedDf = within_column_deduplicator(completedDf, 'Completed')
    
    # now pass the columnDfs into the external_columns_deduplicator() function to remove outdated duplicates found in other columns that is not the currently processed column
    counterDf = external_columns_deduplicator(counterDf, progressDf, completedDf, 'Counter', 'In Progress', 'Completed')
    progressDf = external_columns_deduplicator(progressDf, completedDf, counterDf, 'In Progress', 'Completed', 'Counter')
    completedDf = external_columns_deduplicator(completedDf, counterDf, progressDf, 'Completed', 'In Progress', 'Completed')

    # call variables outside of function and set them as global
    global counterPlates, progressPlates, completedPlates
    
    # put all plateno data of counterDf, progressDf, and completedDf dataframe into their respective lists
    counterPlates = plate_preparator(counterDf)
    progressPlates = plate_preparator(progressDf)
    completedPlates = plate_preparator(completedDf)

    # turn the three final, prepared results into a dictionary variable called allPlates
    allPlates = {'counter': counterPlates, 'progress': progressPlates, 'completed': completedPlates}
    
    # return allPlates that will be used to generate colored plateno labels by JavaScript
    return allPlates