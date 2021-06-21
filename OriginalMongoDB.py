#--- Jay Authement ---#
#--- Original MongoDB Database ---#
#--- v[1.0.0] ---#

# Using pretty print(pprint) to make results easier to view
from pprint import pprint
from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import date, timedelta, datetime

client = MongoClient(host='mongodb://localhost:27017/', 
                     username='aacuser', 
                     password='Smokey204!!',
                    authSource="AAC")
database = client['AAC']

def main():

    while(1):

        selection = input('\n Select 1 to Create, 2 to Read, 3 to Update, or 4 to Delete! To exit Program, press ctl+c!\n')
        
        if selection == '1':
            create()
            
        elif selection == '2':
            read()

        elif selection == '3':
            update()

        elif selection == '4':
            delete()

        else:
            print("Please enter a valid selection!")

# This will create an entry into the MongoDB database!-----------------------------------------------------------------------
def create():

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

# This will read an object in the MongoDB database!----------------------------------------------------------------------------
def read():

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

# This will update an object in the MongoDB database!-----------------------------------------------------------------------------
def update():

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

# This is the delete function for the MongoDB database!---------------------------------------------------------------------
def delete():
    try:

        animalID = input('\nPlease enter the animal ID# you wish to delete: \n')

        if database.animals.find({"animal_id" : animalID}).count() == 0:
            print('\n------The ID doesn\'t exist!------\n')

        else:
            database.animals.delete_many({"animal_id" : animalID})
            print ('\nDeletion successful\n') 

    except Exception as e:
        print(e)

main()



