
def my_car(manufacturer,release_year=2024,**kwargs):
    car_details = [f"Manufacturer: {manufacturer}", f"Release year: {release_year}"]+[f"Additional info-{key}: {value}"for key, value in kwargs.items()]
    return car_details

car1= my_car("Toyota", 2020,model='Prius',comment='Nataxavebia')
print(car1)

car2= my_car("Kia", 2023,model='Sportage',vin_code='tr52b631',engine=2.5,comment='kanfetivitaa')
print(car2)