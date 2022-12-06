import pandas as pd

df = pd.read_csv("/home/Jack/Documents/college/Automobile_data.csv")
print(df.head(5))
print()

df = pd.read_csv("/home/Jack/Documents/college/Automobile_data.csv")
print(df.tail(5))
print()

df = pd.read_csv("/home/Jack/Documents/college/Automobile_data.csv")
df = df [["company","price"]][df.price==df["price"].max()]
print(df)
print()

df = pd.read_csv("/home/Jack/Documents/college/Automobile_data.csv")
car_Manufacturues = df.groupby("company")
toyotaDF = car_Manufacture,get_group("toyata")
print(toyotaDF)
print()

df.read_csv("/home/Jack/Documents/college/Automobile_data.csv")
print(df["company"].vaule_counts())
print()

df = pd.read_csv("/home/Jack/Documents/college/Automobile_data.csv")
car_Manufactures = df.grouphy("company")
priceDF = car_Manufactures["company","average-mileage"].mean()
print(mileageDF)
print()

df = pd.read_csv("/home/Jack/Documents/college/Automobile_data.csv")
car_Manufactures = df.grouphy("company")
mileageDF = car_Manufactures["company","average-mileage"].mean()
print(mileageDF)
print()

carsDF = pd.read_csvdf = pd.read_csv("/home/Jack/Documents/college/Automobile_data.csv")
car_Manufactures = df.grouphy("company")
priceDF = car_Manufactures["company","average-mileage"].mean()
print(mileageDF)
print()

carsDF = pd.read.csv("/home/Jack/Documents/college/Automobile_data.csv")
carsDF = carsdf.sort_vaules(by=["price","horsepower"], ascending=False)
print(carsDF.head(5))
print()

Germancars = {"company": {"ford", "Mercedes","BMV","Audi"}, "price": [23845, 171995, 135925, 71400]}
carsDF1 = pd.DataFrama.from_dict(GermanCars)

JapaneseCars = {"company": ["Ford", "Mercedes", "BMV", "Audi"], "price": [29995, 23600, 61500]}
carsDF2 = pd.Dataframe.from_dict(japaneseCars)

CarsDF = pd.concat([carsDF1, carsDF2], keys=["Germnay", "Japan"]
print(carsDF)
print()

pd.read_csv("/home/Jack/Documents/college/Automobile_data.csv")
carsDF.sort_vaules(by=["price", "horsepower"], ascending=False)
rsDF.head(5))

cars = {"company": ["Ford", "Mercedes", "BMV", "Audi"], "price": [23845, 171995, 135925, 71400]}
= pd.DataFrame.drin_dict(japansesCars)

cars = {"company": ["Toyota", "Honda", "Nissan", "Mitsubishi" ]. "price": [29995, 23600, 61500, 58900]
=

pd.contact([carsDF1, carsDF2], keys=["Germany", "Japan"])|
carsDF

Car_Price = {"Company": ["Toyota", "Honda", "BMV", "Audi"], "Price": [23845, 17995, 135925, 71400]}
carPriceDF = pd.DataFrame.from_dict(Car_Price)

car_Horsepower = {"Company": ["Toyota", "Honda", "BMV", "Audi"], "horsepower": [141, 80, 182, 160]}
carsHorsepowerDF = pd.DataFrame.from_dict(car_Horsepower)

carsDF = pd.merge(carPriceDF, carsHorsepowerDF, on="Company")
print(carsDF)
print()

    

        
