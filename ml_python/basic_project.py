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
available_cars= [car_1, car_2, car_3]

#Step 2: Ask the passenger destination
print('Station Location: Pourashava More')
print('Available Cars going to Destinations: Haruya, Akrampur, Haybotnogor')
print('Available Vehicles: Auto, Rickshaw, CNG')

choice_car= input('Choose your vehicle: ')
if choice_car == available_cars[0]['name']:
    destination= input('Please enter your destination: ')
elif choice_car == available_cars[1]['name']:
    destination= input('Please enter your destination: ')
elif choice_car == available_cars[2]['name']:
    destination= input('Please enter your destination: ')
else:
    print('Not available vehicle. Please choose from the available vehicles.')

#Step 3: Check available cars


found= False
for car in available_cars:
    if destination in car['destinations']:
        found= True
        print(f'Vehicle Name: {car['name']}.')
        print(f'Fare: {car['fare']} Taka.')

        #Step 5: Ask passenger's money
        money= int(input('please enter your money: '))

        #Step 6: Make a money decision
        if money >= car['fare']:
            print('You can take this vehicle. Have a nice jurney!')
            break
        else:
            print('Sorry, you do not have enough money to take this vehicle.')

# Step 7: If no vehicle is available
if not found: 
    print('Sorry, there is no available vehicle for your destination.') 

