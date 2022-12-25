from parc7.guitar import Guitar

guitars = []

file = open("guitars.csv", "r")  # open file and read
file.readline()

for line in file:
    Distinguish = line.strip().split(",")
    guitar_part = Guitar(Distinguish[0], int(Distinguish[1]), Distinguish[2])  # p1,p2,p3
    guitars.append(guitar_part)

file.close()
guitars.sort()  # Sort by rule

my_guitar_name = input("Name: ")  # p1
my_guitar_year = int(input("Year: "))  # p2
my_guitar_cost = float(input("Cost: $"))  # p3

guitars.append(Guitar(my_guitar_name, my_guitar_year, my_guitar_cost))
print(f"{my_guitar_name} ({my_guitar_year}) : ${my_guitar_cost} is add in the file.\n")

update_file = open("guitars.csv", "w")  # input my own guitar
for own_guitar in guitars:
    print(f"{own_guitar.name}, {own_guitar.year}, {own_guitar.cost},", file=update_file)

update_file.close()
