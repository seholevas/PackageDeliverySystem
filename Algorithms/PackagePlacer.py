class PackageSort:

    def __init__(self):
        self

    # Manually Sorts Packages Into Trucks
    # TODO: make this an automatic search.
    def package_sort(self, h, truck1,truck2,truck3):

        packages_on_truck_1 = [h["7"], h["29"], h["13"], h["39"], h["15"], h["16"], h["34"], h["14"], h["20"], h["21"], h["1"], h["19"], h["2"], h["33"], h["24"], h["22"]]
        packages_on_truck_2 = [h["5"], h["37"], h["38"], h["36"], h["3"], h["18"], h["6"], h["17"], h["31"], h["32"], h["25"], h["26"], h["4"], h["40"], h["8"], h["9"]]
        packages_on_truck_3 = [h["30"], h["27"], h["35"], h["28"], h["11"], h["12"], h["23"], h["10"]]

        # Loops Through Packages and sets them to certain truck
        for package in packages_on_truck_1:
            package.set_truck_number("1")

        for package in packages_on_truck_2:
            package.set_truck_number("2")

        for package in packages_on_truck_3:
            package.set_truck_number("3")

        # Places Packages on Trucks
        truck1.set_packages(packages_on_truck_1)
        truck2.set_packages(packages_on_truck_2)
        truck3.set_packages(packages_on_truck_3)









