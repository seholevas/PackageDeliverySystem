from CSV.DataReader import DataReader
from Algorithms.PackagePlacer import PackageSort
from Data.Truck import Truck
from Algorithms.Dijkstra import Dijkstra
from Data.Location import Location

dr = DataReader()

hash_table = dr.load_package_data_into_hash_table("../CSV/WGUPSPackageFile.csv")
graph = dr.load_distance_data_into_graph("../CSV/WGUPSDeliveries.csv")

print("unordered list: ", l)

start = Location("4001 South 700 East", "Salt Lake City", "UT", "84107")
t = Truck(None, start, l, graph)
t.set_total_amount_of_mileage_allowed_to_drive(40)
# t.drive(hash_table)
t.prioritize_packages()

t.drive()
print("ordered list: ", t.get_packages())
print(t.current_mileage)
print(Truck.get_total_amount_of_mileage_allowed_to_drive())



