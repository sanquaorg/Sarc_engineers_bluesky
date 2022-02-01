name = input("Enter Your Name")
place = input("Enter Your Place")
date = input("Enter the date of entry (dd-mm-yyyy)")
particulate = input("Enter the ratio of particulate matter present in the hyper spectral image")
no2 = int(input("Enter the density of No2 in air"))
so2 = int(input("Enter the density of So2 in air"))
o2 = int(input("Enter the density of O2 in air"))
n2 = int(input("Enter the density of N2 in air"))
co2 = int(input("Enter the density of Co2 in air"))
o3 = int(input("Enter the density of O3 in air"))
print("Displaying the details ")
total = no2+so2+o2+n2+co2+o3
pol_fact = float((no2/total)*0.01)

if pol_fact > 7:
    print("Pollutants are high in the given hyper spectral image")
elif 5 < pol_fact < 7:
    print("Pollutants are medium in the given hyper spectral image")
elif 3 < pol_fact < 5:
    print("Pollutants are low in the given hyper spectral image")
else:
    print("You live in a safe environment")

