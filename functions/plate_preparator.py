# import dependencies
import pandas as pd

# FIFTH PART OF PROGRAM CODE: USER-DEFINED FUNCTION FOR PLATE AND COLOR PREPARATOR (CONFIRMED WORKING)
# create an automated plate and color preparing function for each plate number, which will take a columnDf data content
def plate_preparator(columnData):
    # debugging: print a message telling that this function is successfully called
    # print('plate_preparator() function called successfully')
    
    # create a variable that will store values of jrno as index
    indexColumn = columnData['jrno'].unique()

    # create a list to store biglist (aka list of lists of lists of plateno and its respective jrno)
    bigList = []
    
    # for-loop that will grab all plateno and appointment data where jrno equals current value
    for index in indexColumn:
        # use loc[] function to access current row matching the index value...
        # ...but only grab the stored values in plateno and appointment columns...
        # ...then use values.tolist() function to turn the grabbed values into a list 
        dataGrab = columnData.loc[columnData['jrno'] == index, ['plateno', 'csno', 'appointment']].values.tolist()
        
        # append datagrab to biglist
        bigList.append((dataGrab))
    
    # create a list to store generatorData (aka list of lists transformed using bigList's list of lists of lists)
    generatorData = []
    
    # for-loop that will transform biglist into smalllist
    for smallList in bigList:
        # append curent index 0 of smallList to generatorData
        generatorData.append(smallList[0])
    
    # return generatorData that will be used to generate colored plateno labels
    return generatorData