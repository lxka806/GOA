from django.shortcuts import render

cars_database = [
    {'id': 0, 'brand': 'BMW', 'model': 'M3 Competition', 'color': 'black', 'year': 2024},
    {'id': 1, 'brand': 'Mercedes', 'model': 'AMG C63', 'color': 'white', 'year': 2023},
    {'id': 2, 'brand': 'Audi', 'model': 'RS7', 'color': 'gray', 'year': 2024},
    {'id': 3, 'brand': 'Toyota', 'model': 'Supra', 'color': 'red', 'year': 2022},
    {'id': 4, 'brand': 'Nissan', 'model': 'GT-R R35', 'color': 'blue', 'year': 2023},
    {'id': 5, 'brand': 'Porsche', 'model': '911 Turbo S', 'color': 'yellow', 'year': 2024},
    {'id': 6, 'brand': 'Lamborghini', 'model': 'Huracan EVO', 'color': 'green', 'year': 2023},
    {'id': 7, 'brand': 'Ferrari', 'model': '488 GTB', 'color': 'red', 'year': 2022},
    {'id': 8, 'brand': 'Ford', 'model': 'Mustang GT', 'color': 'black', 'year': 2024},
    {'id': 9, 'brand': 'Chevrolet', 'model': 'Corvette C8', 'color': 'orange', 'year': 2023},
    {'id': 10, 'brand': 'Tesla', 'model': 'Model S Plaid', 'color': 'white', 'year': 2024},
    {'id': 11, 'brand': 'Tesla', 'model': 'Model 3 Performance', 'color': 'black', 'year': 2023},
    {'id': 12, 'brand': 'Honda', 'model': 'Civic Type R', 'color': 'blue', 'year': 2022},
    {'id': 13, 'brand': 'Subaru', 'model': 'WRX STI', 'color': 'blue', 'year': 2021},
    {'id': 14, 'brand': 'Mazda', 'model': 'RX-7', 'color': 'red', 'year': 2002},
    {'id': 15, 'brand': 'Mazda', 'model': 'RX-8', 'color': 'silver', 'year': 2008},
    {'id': 16, 'brand': 'Volkswagen', 'model': 'Golf R', 'color': 'gray', 'year': 2023},
    {'id': 17, 'brand': 'BMW', 'model': 'M5 Competition', 'color': 'black', 'year': 2024},
    {'id': 18, 'brand': 'Mercedes', 'model': 'AMG GT', 'color': 'green', 'year': 2023},
    {'id': 19, 'brand': 'Audi', 'model': 'R8 V10', 'color': 'white', 'year': 2022},
    {'id': 20, 'brand': 'Lexus', 'model': 'LC 500', 'color': 'blue', 'year': 2023},
    {'id': 21, 'brand': 'Jaguar', 'model': 'F-Type', 'color': 'red', 'year': 2022},
    {'id': 22, 'brand': 'McLaren', 'model': '720S', 'color': 'orange', 'year': 2024},
    {'id': 23, 'brand': 'Bugatti', 'model': 'Chiron', 'color': 'black', 'year': 2024},
    {'id': 24, 'brand': 'Aston Martin', 'model': 'DB11', 'color': 'silver', 'year': 2023},
    {'id': 25, 'brand': 'Kia', 'model': 'Stinger GT', 'color': 'red', 'year': 2022},
    {'id': 26, 'brand': 'Hyundai', 'model': 'Elantra N', 'color': 'blue', 'year': 2023},
    {'id': 27, 'brand': 'Peugeot', 'model': '508 GT', 'color': 'gray', 'year': 2022},
    {'id': 28, 'brand': 'Renault', 'model': 'Megane RS', 'color': 'yellow', 'year': 2021},
    {'id': 29, 'brand': 'Alfa Romeo', 'model': 'Giulia Quadrifoglio', 'color': 'red', 'year': 2024},
]

# Create your views here.
def all_cars(req):
    return render(req, 'index.html', {
        "cars": cars_database
    })

def car_with_id(req, id):
    if 0 <= id < len(cars_database):
        car = cars_database[id]
    else:
        car = None
    
    return render(req, "car.html", {
        "car": car
    })