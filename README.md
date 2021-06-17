# MongoDB-Database 

## About the Project

The MongoDB Database program is a standard database query program that was developed for my CS-340 class. The program utilizes the powerful Python programming language along with the versatility of the NoSQL MongoDB to create a program stack that allows the user to perform CRUD operations on the databases provided. MongoDB Database uses two .CSV files to create the databases which the program will use to perform all the operations. All options are displayed on a main menu, that allows users to easily find the option they are looking for.

## Motivation

This project was originally designed as part of a final project for my CS-340. The project has since been enhanced and serves as an artifact to show my comprehension in database design and interaction. By revising and adding a few new features to this program in my CS-499 class for v1.1.0, I believe the program now properly shows my ability and skills working with databases.

## Installation

To properly run this program, Python and MongoDB must first be installed on the users machine. Instructions for installing Python can be found at https://www.python.org/downloads/ and instructions for installing MongoDB can be found at https://docs.mongodb.com/manual/installation/. Once installed, the two .CSV files should be imported into MongoDB using the MongoDB shell with the commands, "mongoimport --type csv -d AAC -c animals --headerline --drop aac_shelter_outcomes.csv" and "mongoimport --type csv -d Bid -c bids --headerline --drop eBids_Monthly_Sales.csv". Once both databases are successfully imported, the user should now create a username and password in MongoDB for each database they wish to interact with using the command "db.createUser()". For more instructions on the specifics of creating each user, please visit https://docs.mongodb.com/manual/reference/method/db.createUser/.

## Getting Started

After the everything is properly installed, the next step would be to open the provided MongoDB.py file and alter the client1 and client2 information. Their is space to enter a username and password for each, which should match the previously created user logins created from the installation step. For client1 the code lines are at 14 and 15 and for client2 the code lines are at 21 and 22. If the databases were created using the same exact names as shown during the installation step, no further changes to the Python file are required. If the database was renamed, code lines 16,17,23, and 24 should reflect this by entering in the newly chosen database names.

## Usage

Once setup, the program is fairly simple to navigate. The user is first presented with a menu and given three options, connect to the AAC database, connect to the eBid database, or exit the program. Once a database option is selected, the program will login using the provided username and password from installation, and display a message that it has successfully connected to the database. From there another menu will give the user five more options, allowing them to perform CRUD (create, read, update, and delete) operations on the data or exit back to the database selection menu. Once finished, the user may select the exit option to return and disconnect from their selected database. Now they once again have the option to either connect to a new database or exit the program. Once all operations have been completed, the user may select option three at the database selection menu to properly exit the program.

## Changelog

[1.1.0] - 2021-6-17

This version was created for my CS-499 class, which adds a few more features to display my understanding of database structures and design. The first new feature includes adding a new database to the program, which is created under client2 in the MongoDB Python file. This now allows the user to connect to another seperate database, rather than just the AAC database. A new main menu was also created that allows the user to switch between the two databases as much as they'd like, along with an exit option. Another menu was created to allow users to perform CRUD operations on the second eBid database. To make this work properly four new functions were created, createBid(), readBid(), updateBid(), and deleteBid(). These functions allow the user to interact and manipulate the data that is contained in the eBid database. 

[1.0.0] - 2021-6-3

Original project upload from CS-340 class. Project includes all necessary files to allow the user to perform CRUD operations on the AAC database. When ran, the program connects the user to the AAC database and gives them one menu to perform CRUD operations on the database. The functions created to allow this manipulation are createAAC(), readAAC(), updateAAC(), and deleteAAC(). Each function will allow the user to manipulate the data inside the AAC database and save the changes. 
