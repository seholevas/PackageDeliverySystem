import csv
from Data.Location import Location
from Data.Package import Package
from DataStructures.HashTable import HashTable
from DataStructures.Graph import WGUPS_Graph
class DataReader:

    def __init__(self):
        self

    # Loads package data from csv sheet and inserts them into package objects.
    # package data is then loaded into a hash table
    @staticmethod
    def load_package_data(csv_relative_path_name):

        package_hashtable = HashTable()

        with open(csv_relative_path_name, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)

            for line in csv_reader:
                address = Location(line["Address"].strip(), line["City"].strip(), line["State"].strip(),
                                   line["Zip"].strip())
                package = Package(line["Package ID"], address, line["Delivery Deadline"], line["Weight"],
                                  line["Special Notes"])
                # package = Package(line["Package ID"], line["Address"], line["Delivery Deadline"], line["Weight"],
                #                   line["Special Notes"])
                package_hashtable[line["Package ID"]] = package
                # list_of_packages.append(package)

        return package_hashtable

    # Loads package data from csv sheet and inserts them into package objects.
    # package objects are then inserted into hashtable
    def load_package_data_into_hash_table(self, csv_relative_path_name):

        package_hashtable = HashTable()

        with open(csv_relative_path_name, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)

            for line in csv_reader:

                address = Location(line["Address"].strip(), line["City"].strip(), line["State"].strip(), line["Zip"].strip())
                package = Package(line["Package ID"], address, line["Delivery Deadline"], line["Weight"], line["Special Notes"])
                # package = Package(line["Package ID"], line["Address"], line["Delivery Deadline"], line["Weight"],
                #                   line["Special Notes"])
                package_hashtable[line["Package ID"]] = package
                # list_of_packages.append(package)

        return package_hashtable

    # Loads location data from csv sheet and inserts them
    # into source locations and destination locations as well as weights.
    # loads location(s) data into graph to form a graph/map.
    def load_distance_data_into_graph(self, csv_relative_path_name):
        graph = WGUPS_Graph()

        with open(csv_relative_path_name, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)

            for line in csv_reader:
                # source = line["Starting Place"] + line["Starting Address"]
                # destination = line["Ending Place"] + line["Ending Address"]
                source = line["Starting Place Address"].strip() + ', ' + line["Starting Place City"].strip() + ', ' + line["Starting Place State"].strip() + ', ' + line["Starting Place Zip"].strip()
                destination = line["Ending Place Address"].strip() + ', ' + line["Ending Place City"].strip() + ', ' + line["Ending Place State"].strip() + ', ' + line["Ending Place Zip"].strip()
                # source = Location(line["Starting Place Address"], line["Starting Place City"],
                #                   line["Starting Place State"], line["Starting Place Zip"])
                # destination = Location(line["Ending Place Address"], line["Ending Place City"],
                #                        line["Ending Place State"], line["Ending Place Zip"])
                weight = float(line["Distance Between"])

                # print(source, destination, weight)
                graph.add_edge(source, destination, weight)

        return graph

# data = DataReader()
# data.load_distance_data_into_graph("../CSV/WGUPSDeliveries.csv")
