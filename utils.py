############## I SHOULD MAKE TESTS FOR THESE FUNCTIONS ###############

import arcpy

"""
Takes in a list of Feature Class file paths(@param:filesList). Deletes fields
that do not appear in all the Feature Classes. Results in all files
in filesList have the same fields.

Ex. filesList = ['C:/example/bridgeData1', 'C:/example/bridgeData2']
    Let's say that: bridgeData1 has fields 'length', 'width', 'height', 'date'
                    bridgeData2 has fields 'width', 'height', 'load', 'duration'
    The result of running makeFieldsSame leaves
                bridgeData1 and bridgeData2 with fields:   'width', 'height'
"""
def makeFieldsSame(filesList):
    fieldsListofLists = []

    # get fields from each fc
    for fc in filesList:
        fieldsListofLists.append([f.name for f in arcpy.ListFields(fc)])

    deleteList = []

    for fcFields in fieldsListofLists: 
        toDelete = []
        for field in fcFields:
            for fc in fieldsListofLists: # loop over all fcs again to check if field is a member
                if field not in fc and field not in toDelete:
                    toDelete.append(field)
        deleteList.append(toDelete)

    
    for x in range(0, len(filesList)):
            if(deleteList[x]):
                arcpy.DeleteField_management(filesList[x], deleteList[x])


# This function gets the path to any resourceName passed in, which is in the workingDir
# folder tree (ie. it doesn't need to be in the root of workingDir, just beneath the folder)
def getResourcePath(resourceName, workingDir=workingDir):
    def noResource():
        print("\n\n\nRESOURCE IS MISSING: " + resourceName)
        print("Please add this resource to the project. Once it is added, type 'yes' below")
        proceed = raw_input("Has the resource been added?")
        if proceed.lower() == "yes":
            getResourcePath(resourceName)
        else:
            noResource()


    for root, dirs, files in arcpy.da.Walk(workingDir):
        if resourceName in files:
            res = root + '\\' + resourceName
            return res.encode('utf-8')

    noResource()



def getDate():
    # Need to calculate the time for the file naming convention below
    today = datetime.date.today()
    temp = today.isoformat()
    todayList = temp.split("-")
    year = todayList[0]
    month = int(todayList[1])
    print(year)
    print(month)
    monthNames = ['Jan','Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    currMonth = monthNames[month-1]
    
