#Dictionary value change

car_data={"Brand" : "Tata", "Model" : "Suzuki", "Year" : 2001}
car_data["year"]= 2005
print(car_data)

print(len(car_data))

car_data["colour"] = "white"
print(car_data)

car_data.pop("year")
print(car_data)



