#--- Jay Authement ---#
#--- Enhanced MongoDB Database ---#
#--- Greg Stefanelli ---#
#--- CS * 499 ---#

#--- Using pretty print(pprint) to make results easier to view ---#
from pprint import pprint
from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import date, timedelta, datetime

#--- Connects with 'accuser' to the AAC database ---#
client = MongoClient(host='mongodb://localhost:27017/',
    username='aacuser',
    password='Smokey204!!',
    authSource="AAC")
database = client['AAC']

#--- Connects with 'accuser' to the Bid database ---#
client2 = MongoClient(host='mongodb://localhost:27017/', 
    username='aacuser',
    password='password',
    authSource="Bid")
database2 = client2['Bid']

#--- Main program function to display menu and call other functions ---#
def main():

    while(1):
    
        print("(1) = AAC database\n(2) = Bid database\n(3) = Exit")

        selection = input('\n Choose your database from choices above! \n')

        # Use AAC database to perform CRUD operations
        if selection == '1':
            
            print("\nYou have successfully connected to the AAC database!\n")
            
            while(1):
                
                accSelection = input('\n Select 1 to Create, 2 to Read, 3 to Update, or 4 to Delete. To exit database, select 5!\n')
               
                if accSelection == '1':
                    createAAC()
                   
                elif accSelection == '2':
                    readAAC()
                   
                elif accSelection == '3':
                    updateAAC()
                   
                elif accSelection == '4':
                    deleteAAC()
                   
                elif accSelection == '5':
                    print("\n You are disconnecting from the AAC database. Goodbye!\n")
                    break

        #--- Use Bid database to perform CRUD operations ---#
        elif selection == '2':
        
            print("You have successfully connected to the Bid database!")
            
            while(1):
            
                bidSelection = input('\n Select 1 to Create, 2 to Read, 3 to Update, or 4 to Delete from the Bid database. To exit database, select 5!\n')
            
                if bidSelection == '1':
                    createBid()
                    
                elif bidSelection == '2':
                    readBid()
                   
                elif bidSelection == '3':
                    updateBid()
                   
                elif bidSelection == '4':
                    deleteBid()
                    
                elif bidSelection == '5':
                    print("\n You are disconnecting from the Bid database. Goodbye!\n")
                    break

        #--- Terminates the program ---#
        elif selection == '3':
            print("\nHave a nice day, goodbye!\n")
            break
#************************************************************************************************************************************#


#--- This will create an entry into the AAC MongoDB database! ---#
def createAAC():

    try:

        animalAge  = int(input('Enter animals age upon outcome in years :'))
        animalID = input('Enter animal ID :')
        animalType = input('Enter the animal type :')
        animalBreed = input('Enter the animal breed :')
        animalColor = input('Enter the animals color :')
        animalDOB = int(input('Enter the animals DOB :'))
        animalName = input('Enter animals name :')
        animalOutcome = input('Enter animals outcome subtype :')
        animalOutcomeType = input('Enter animals outcome type :')
        animalSex = input('Enter animals sex :')
        animalLat = int(input('Enter animals latitude location :'))
        animalLong = int(input('Enter animals longitude location :'))
        animalAgeWeeks = (animalAge * 365) / 7

        if database.animals.find({"animal_id" : animalID}).count() != 0:
            print("------ID number already used in database!------")
            print("------Animal was not added!------")

        else:

            database.animals.insert_one(
            {
                "age_upon_outcome" : animalAge,
                "animal_id" : animalID,
                "animal_type" : animalType,
                "breed" : animalBreed,
                "color" : animalColor,
                "date_of_birth" : animalDOB,
                "datetime" : datetime.now(),
                "monthyear" : datetime.now(),
                "name" : animalName,
                "outcome_subtype" : animalOutcome,
                "outcome_type" : animalOutcomeType,
                "sex_upon_outcome" : animalSex,
                "location_lat" : animalLat,
                "location_long" : animalLong,
                "age_upon_outcome_in_weeks" : animalAgeWeeks
            }
        )
            print('\n------Date was created in database!------\n')

    except Exception as e:
        print('\n------Entry not created in database!------\n')
        print(e)
        
#--- This will create an entry into the Bid MongoDB database! ---#
def createBid():

    try:
    
        bidID = int(input('Enter a bid ID :'))
        bidTitle = input('Enter the bid title :')
        bidDepartment = input('Enter the department name :')

        if database2.Products.find({"Auction ID" : bidID}).count() != 0:
            print("------ID number already used in database!------")
            print("------Bid was not added!------")

        else:

            database2.Products.insert_one(
            {
                "Auction Title" : bidTitle,
                "Auction ID" : bidID,
                "Department" : bidDepartment,
               
            }
        )
            print('\n------Date was created in database!------\n')

    except Exception as e:
        print('\n------Entry not created in database!------\n')
        print(e)
#************************************************************************************************************************************#


#--- This will read an object in the AAC MongoDB database! ---#
def readAAC():

    try:

        animalType = input('Enter an animal type to find: ')

        query = database.animals.find({"animal_type" : animalType})

        if query.count() != 0:
            print('\nHere are your results from query!\n')
            for animal in query:
                pprint(animal)

        else:
            print('\n------Nothing found from query!------\n')

    except Exception as e:
        print(e)

#--- This will read an object in the Bid MongoDB database! ---#
def readBid():

    query = database2.Products.find()
    
    for items in query:
        pprint(items)
#************************************************************************************************************************************#


#--- This will update an object in the AAC MongoDB database! ---#
def updateAAC():

    try:

        animalToUpdate = input('Enter an animal ID# to update: ')

        if database.animals.find({"animal_id" : animalToUpdate}).count() != 0:
        
            animalAge  = int(input('Enter animals age upon outcome in years to update :'))
            animalType = input('Enter the animals type to update:')
            animalBreed = input('Enter the animals breed to update:')
            animalColor = input('Enter the animals color to update:')
            animalDOB = int(input('Enter the animals DOB to update:'))
            animalName = input('Enter animals name to update:')
            animalOutcome = input('Enter animals outcome subtype to update:')
            animalOutcomeType = input('Enter animals outcome type to update:')
            animalSex = input('Enter animals sex to update:')
            animalLat = int(input('Enter animals latitude location to update:'))
            animalLong = int(input('Enter animals longitude location to update:'))
            animalAgeWeeks = (animalAge * 365) / 7

            database.animals.update_one(
                {"animal_id" : animalToUpdate},
                {
                    "$set" : {
                        "age_upon_outcome" : animalAge,
                        "animal_type" : animalType,
                        "breed" : animalBreed,
                        "color" : animalColor,
                        "date_of_birth" : animalDOB,
                        "datetime" : datetime.now(),
                        "monthyear" : datetime.now(),
                        "name" : animalName,
                        "outcome_subtype" : animalOutcome,
                        "outcome_type" : animalOutcomeType,
                        "sex_upon_outcome" : animalSex,
                        "location_lat" : animalLat,
                        "location_long" : animalLong,
                        "age_upon_outcome_in_weeks" : animalAgeWeeks
                    }
                }
            )
            print('------Animal ID: ' + animalToUpdate + ' was updated!------')

        else:
            
            print('\n------The ID doesn\'t exist!------\n')

    except Exception as e:
        print(e)
        
        
#--- This will update an object in the Bid MongoDB database! ---#
def updateBid():

    try:

        bidToUpdate = int(input('Enter a bid ID# to update: '))

        if database2.Products.find({"Auction ID" : bidToUpdate}).count() != 0:
        
            bidTitle = input('Enter the new bid title:')
            bidDepartment = input('Enter the new department:')

            database2.Products.update_one(
                {"Auction ID" : bidToUpdate},
                {
                    "$set" : {
                        "Auction Title" : bidTitle,
                        "Department" : bidDepartment
                    }
                }
            )
            print('------Bid ID: ' + bidToUpdate + ' was updated!------')

        else:
            
            print('\n------The ID doesn\'t exist!------\n')

    except Exception as e:
        print(e)
#************************************************************************************************************************************#      
        


#--- This is the delete function for the AAC MongoDB database! ---#
def deleteAAC():
    try:

        animalID = input('\nPlease enter the animal ID# you wish to delete: \n')

        if database.animals.find({"animal_id" : animalID}).count() == 0:
            print('\n------The ID doesn\'t exist!------\n')

        else:
            database.animals.delete_many({"animal_id" : animalID})
            print ('\nDeletion successful\n') 

    except Exception as e:
        print(e)

#--- This is the delete function for the Bid MongoDB database! ---#
def deleteBid():
    try:

        bidID = int(input('\nPlease enter the bid ID# you wish to delete: \n'))

        if database2.Products.find({"Auction ID" : bidID}).count() == 0:
            print('\n------The ID doesn\'t exist!------\n')

        else:
            database2.Products.delete_many({"Auction ID" : bidID})
            print ('\nDeletion successful\n') 

    except Exception as e:
        print(e)
#************************************************************************************************************************************#

        
        
        
#--- Running main program ---#
main()



