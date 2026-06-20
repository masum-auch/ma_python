"""Smart Transport Fare System"""

#Step 1: Store car information
#Step 2: Ask the passenger destination
#Step 3: Check available cars
#Step 4: Show the fare
#Step 5: Ask passenger's money
#Step 6: Make a decision
#Step 7: Handle unavailable destinations

#Step 1: Store car information
print('Welcome to Smart Transport Fare System!')
car_1 = {
    "name": "Auto",
    "destinations": ["Haruya", "Akrampur", "Haybotnogor"],
    "fare": 50,
}
car_2 = {
    "name": "Rickshaw",
    "destinations": ["Haruya", "Akrampur", "Haybotnogor"],
    "fare": 30,
}
car_3 = {
    "name": "CNG",
    "destinations": ["Haruya", "Akrampur", "Haybotnogor"],
    "fare": 40,
}

#Step 2: Ask the passenger destination
print('Station Location Pourashava More')
destination= input('please enter you destination: ')

#Step 3: Check available cars

available_cars= [car_1, car_2, car_3]

 