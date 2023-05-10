# import dependencies
import pandas as pd
import pyodbc

# SECOND PART OF PROGRAM CODE: DATA ANALYSIS (CONFIRMED WORKING)
# create a callable function that handles data query and putting collected data in dataframes
def data_query_and_dataframing():
    # debugging: print a message telling that this function is successfully called
    # print('data_query_and_dataframing() function called successfully')
    
    # create three variables to store server, database, and trusted device details, respectively
    server = 'LAPTOP-PLVL436R'
    database = 'isuzugencars'
    trusted = 'yes'
    
    # read contents of server.txt to grab its content
    # with open('server.txt', 'r') as file:
        # server = file.read()
    # database = 'isuzugencars'
    # username = 'sa'
    # password = 'gencars@dominga3'
    
    # use pyodbc.connect() function to connect to MS SQL Server specified above
    conn = pyodbc.connect('DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database + ';TRUSTED_CONNECTION=' + trusted)
    # conn = pyodbc.connect('DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    
    # create a cursor for executing SQL commands
    c = conn.cursor()
    
    # modifiable query code for counter column which selects all records of jrhead not in jehead
    counterQuery = """SELECT jrno, plateno, csno, appointment
                      FROM dbo.tbl_jrhead
                      WHERE jrno NOT IN (SELECT jrno FROM dbo.tbl_jehead)
                      AND jc1 = 1
                      AND jrstatus = 0
                      AND jrdate >= DATEADD(day, -7, GETDATE())
                      ORDER BY jrdate DESC"""

    # modifiable query code for in progress column which selects all records of jrhead with jestatus = 0
    progressQuery = """SELECT jr.jrno, jr.plateno, jr.csno, jr.appointment
                      FROM dbo.tbl_jrhead jr
                      INNER JOIN (SELECT plateno, MAX(transdate) AS latest_date
                      FROM dbo.tbl_jehead GROUP BY plateno) je
                      ON jr.plateno = je.plateno
                      WHERE jr.jrno IN (SELECT jrno FROM dbo.tbl_jehead)
                      AND jr.jc1 = 1
                      AND jr.jrstatus = 0
                      AND jr.jrdate >= DATEADD(day, -7, GETDATE())
                      ORDER BY je.latest_date DESC"""

    # modifiable query code for completed column which selects all records of jrhead with jestatus = 1 and rono = jrno
    completedQuery = """SELECT jr.jrno, jr.plateno, jr.csno, jr.appointment
                      FROM dbo.tbl_jrhead jr
                      INNER JOIN (SELECT headuid, MAX(time2) AS latest_date
                      FROM dbo.tbl_jr_techlog GROUP BY headuid) jrtech
                      ON jr.uid = jrtech.headuid
                      WHERE jr.jrno IN (SELECT jrno FROM dbo.tbl_jehead)
                      AND jr.jrno IN (SELECT jrno FROM dbo.tbl_rohead WHERE jrno = rono)
                      AND jr.jc1 = 1
                      AND jr.jrstatus = 1
                      AND jr.jrdate >= DATEADD(day, -7, GETDATE())
                      ORDER BY jrtech.latest_date DESC"""
    
    # use the created cursor to execute and fetch data of the stored query codes of each column
    counterData = c.execute(counterQuery).fetchall()
    progressData = c.execute(progressQuery).fetchall()
    completedData = c.execute(completedQuery).fetchall()

    # use pd.dataframe() function to store fetched data of each column data in their respective dataframes
    counterDf = pd.DataFrame(counterData, columns = ['counterTuple'])
    progressDf = pd.DataFrame(progressData, columns = ['progressTuple'])
    completedDf = pd.DataFrame(completedData, columns = ['completedTuple'])

    # create lists to prepare columns in preparation for tuple splitting
    columnHeaders = ['jrno', 'plateno', 'csno', 'appointment']

    # use a for-loop and counterHeaders to split tuples stored in counterDf into their respective columns
    for n, col in enumerate(columnHeaders):
        counterDf[col] = counterDf['counterTuple'].apply(lambda location: location[n])

    # use a for-loop and progressHeaders to split tuples stored in progressDf into their respective columns
    for n, col in enumerate(columnHeaders):
        progressDf[col] = progressDf['progressTuple'].apply(lambda location: location[n])

    # use a for-loop and completedHeaders to split tuples stored in completedDf into their respective columns
    for n, col in enumerate(columnHeaders):
        completedDf[col] = completedDf['completedTuple'].apply(lambda location: location[n])

    # use df.drop() function to drop the columns of each column dataframes that still holds fetched tuples
    counterDf = counterDf.drop('counterTuple', axis = 1)
    progressDf = progressDf.drop('progressTuple', axis = 1)
    completedDf = completedDf.drop('completedTuple', axis = 1)
    
    # close the created cursor used to do queries
    c.close()

    # close the MS SQL Server 2014 connection
    conn.close()
    
    # return the three dataframes that will be used for preprocessing and plate preparation
    return counterDf, progressDf, completedDf