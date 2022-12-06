import pandas as pd
#Read the data.csv file
df = pd.read_csv("/home/Jack/Documents/college/Automobile_data.csv")
#Task 1
print(df.head(5))
print()
#Task 1b
print(df.tail(5))
print()
#Task 2
dg = df [['company', 'price',]][df.price==df['price'].max()]
print(dg)
print()
#Task 3
car_Manu = df.groupby('company')
toyotaDF = car_Manu.get_group('toyota')
print(toyotaDF)
print()
#Task 4
print(df['company'].value_counts())
print()
#Task 5
priceDF = car_Manu['company','price'].max()
print(priceDF)
print()
#Task 6
mileageDF = car_Manu['company', 'average-mileage'].mean()
print(mileageDF)
print()
#Task 7
carsDF = df.sort_values(by=['price', 'horsepower'], ascending=False)
print(carsDF)
#Task 8
GermanCars = {'Company': ['Ford', 'Mercedes', 'BMW', 'Audi'], 'Price': [23845, 171995, 135925, 71400]}
carsDF1 = pd.DataFrame.from_dict(GermanCars)
JapaneseCars = {'Company': ['Toyota', 'Honda', 'Nissan', 'Mitsubishi'], 'Price': [29995, 23600, 61500, 58900]}
carsDF2 = pd.DataFrame.from_dict(JapaneseCars)
carsDF = pd.concat([carsDF1, carsDF2], keys=["Germany", "Japan"])
print(carsDF)
print()
#Task 9
Car_price = {'Company': ['Toyota', 'Honda', 'BMW', 'Audi'], 'Price': [23845, 17995, 135925, 71400]}
car_priceDF = pd.DataFrame.from_dict(Car_price)
car_hp = {'Company': ['Toyota', 'Honda', 'BMW', 'Audi'], 'horsepower': [141, 80, 182, 160]}
car_hpDF = pd.DataFrame.from_dict(car_hp)
car_DF = pd.merge(car_priceDF, car_hpDF, on="Company")
print(car_DF)
print()