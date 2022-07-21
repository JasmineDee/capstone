# capstone
capstone project for PDX Guild
# BLUE
####  By Jasmine Davies

# Project Overview
- Interative web application that allows users to plan and record their morning routines. The idea behind the design is geared more towards self care than a to do list to just check off. The purpose is to help users develop and maintain positive and healthy habits to begin the day. The development will happen with Django/Django Rest Framework in backend handling features such as api and user registration and VUE as frontend.

# Features
- As a user I want the ability to track tasks as they are completed

        -[] Display a list of activites to be completed
        -[] Show option to remove or add more tasks as tasks are completed
        -[] Allow user to select duration of activity
        -[] Display clock to show user time elapsed

- As a user I want the ability to view other options to add to my morning routine
    
        -[] Build database of preselected options to choose from
        -[] Develop an inspirational tab to view other routines

- As a user I would like a more personalized experience

        -[] Create user registration and login page
        -[] Allow user to save morning routines for future use
        -[] Display calendar to block off what days the routine will be completed

- As a user I would like the ability to see more mental health into the morning routine features
        
        -[] Create space for user to journal as part of routine task
        -[] Display inspirational quotes at login
        -[] Allow user to select mood at login.. depending on the mood restrict allowed quantity of task for the day


# Data Models
- Task
    - user  
    - title - CHARFIELD / 128
    - complete - Boolean / False
    - created - DateTimeField / True



# Schedule

-Essential Elements

    - Day 1-2
        -[] Create user and login registration page
        -[] Create a single page view displaying a list of tasks to complete in morning routine

    - Day 3-4
        -[] Setup backend to accept post request to allow user to add and remove task to be completed

    - Day 4-6
        -[] Begin adding design and styling elements
        -[] Add clock feature allowing user to set time of activity and display running clock

    - Day 6 - 8
        - [] Incorporate nice to haves
        - [] Create another view that allows for journal entry

    - Day 9 - 10
        - [] Add more design elements and styling

    - Day 10-13
        - [] Allow for extra time to troubleshoot any existing bugs
        - [] Develop presentation 


-Nice to Haves

    - [] Create diary tab so user can journal within the app
    - [] Display interactive calender to allow user to create schedule
    - [] A seperate tab that will pull data from other morning routines to display for user to incorporate into their routine
    - [] Scrape for inspirational quotes to display after user login as a greeting message

-Really Nice to Haves
    
    -[] Feature that allows user to transition the app to nighttime feature (dark theme) and displays the option for a nighttime routine
    -[] Fitness Tabs that scrapes suggestive workouts
    -[] Food Tabs that scrapes for suggested eat in a day meal ideas
    -[] Incorporate sound features that gives user ablity to play calming sounds as they are completing activites

