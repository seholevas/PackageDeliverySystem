#import necessary modules
import csv
from Data.Package import Package
from Data.Location import Location

class FileReader():

    with open("../CSV/WGUPSPackageFile.csv",'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            # print(Package(line[1]))
            # print(line ["Starting Place"])
            package = Package(line["Package ID"], Location(line["Address"], line["City"], line["State"], line["Zip"]), line["Delivery Deadline"], line["Weight"], line["Special Notes"])
            # print(package)

    # def open_file(self, relative_file_path):
    #


