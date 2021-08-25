import collections


class Farm:
    def find_area_of_fertile_lands(self, height, width, barren_coordinates):
        """
        Find the area of all fertile lands after excluding barren land and sort them in asending order
        Args:
            param1: (int) Height of the farm
            param2: (int) Width of the farm
            param3: (set) The coordinates of barren land. String seprated by space.
        Returns:
            (string) sorted areas of fertile land or error message
        """

        # check for invalid height or weight
        if height <= 0 or width <= 0:
            return "Invalid height or width"

        no_of_barren_land = len(barren_coordinates)
        if no_of_barren_land == 0:
            # if no barren land then return entire area of farm
            return str(height * width)
        elif no_of_barren_land == 1:
            # checks if it is single fertile land then return total farm land - barren land
            # this will avoid traversing through the farm
            barren_land_lst = [int(i) for i in next(iter(barren_coordinates)).split()]
            if self.check_single_fertile_land(height, width, barren_land_lst):
                return str(
                    (height * width)
                    - (
                        (barren_land_lst[2] - barren_land_lst[0] + 1)
                        * (barren_land_lst[3] - barren_land_lst[1] + 1)
                    )
                )

        # build an empty farm
        farm = [[0 for x in range(width)] for y in range(height)]

        # checks for valid barren coordinates and fill barren land area into farm
        valid_barren, farm = self.build_barren_land(
            height, width, barren_coordinates, farm
        )
        if not valid_barren:
            return "Barren coordinates are outside of farm"

        # fill and find areas of farm land using bfs
        fertile_land_areas = self.bfs(height, width, farm)

        if len(fertile_land_areas) == 0:
            return "0"
        else:
            fertile_land_areas.sort()
            return " ".join([str(i) for i in fertile_land_areas])

    def check_single_fertile_land(self, height, width, barren_land_lst):
        """
        Checks if it is single fertile land
        Args:
            param1: (int) Height of the farm
            param2: (int) Width of the farm
            param3: (list) The coordinates of barren land
        Returns:
            (boolean) True if barren land is not separating fertile land
        """

        return (
            (barren_land_lst[0] > 0 and barren_land_lst[2] <= width - 1)
            or (barren_land_lst[0] >= 0 and barren_land_lst[2] < width - 1)
        ) and (
            (barren_land_lst[1] > 0 and barren_land_lst[3] <= height - 1)
            or (barren_land_lst[1] >= 0 and barren_land_lst[3] < height - 1)
        )

    def build_barren_land(self, height, width, barren_coordinates, farm):
        """
        Fill barren land portion into farm
        Args:
            param1: (int) Height of the farm
            param2: (int) Width of the farm
            param3: (set) The coordinates of barren land. String seprated by space
            param4: (2D array int) farm land
        Returns:
            (boolean) checks if barren_coordinates are valid
            (2D array int) farm land
        """

        for barren in barren_coordinates:
            lst = barren.split()
            bottom_x = int(lst[0])
            bottom_y = int(lst[1])
            top_x = int(lst[2])
            top_y = int(lst[3])

            # check for invalid barren coordinates
            if (
                bottom_x >= width
                or top_x >= width
                or bottom_y >= height
                or top_y >= height
                or bottom_x < 0
                or top_x < 0
                or bottom_y < 0
                or top_y < 0
            ):
                return False, farm

            # fill barren land into farm
            farm = self.find_rectangle_land((bottom_x, bottom_y), (top_x, top_y), farm)

        return True, farm

    def find_rectangle_land(self, x_coordinates, y_coordinates, farm):
        """
        Fill each barren rectangle portion into farm
        Args:
            param1: (tuple) bottom left coordinates of barren land
            param2: (tuple) top right coordinates of barren land
            param3: (2D array int) farm land
        Returns:
            (2D array int) farm land
        """

        for i in range(x_coordinates[1], y_coordinates[1] + 1):
            for j in range(x_coordinates[0], y_coordinates[0] + 1):
                farm[i][j] = 1

        return farm

    def bfs(self, height, width, farm):
        """
        Traverse through all adjacent neighbours using breadth first search technique
        Args:
            param1: (int) Height of the farm
            param2: (int) Width of the farm
            param3: (2D array int) farm land
        Returns:
            (list) areas of fertile lands
        """

        fertile_land_areas = []

        neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for i in range(height):
            for j in range(width):
                if farm[i][j] == 0:
                    area = 0
                    queue = collections.deque()
                    queue.append((i, j))
                    farm[i][j] = 2
                    area += 1
                    while queue:
                        pair = queue.popleft()
                        for x, y in neighbors:
                            new_row = pair[0] + x
                            new_col = pair[1] + y
                            if (
                                self.boundary_check(height, width, new_row, new_col)
                                and farm[new_row][new_col] == 0
                            ):
                                queue.append((new_row, new_col))
                                farm[new_row][new_col] = 2
                                area += 1
                    fertile_land_areas.append(area)

        return fertile_land_areas

    def boundary_check(self, height, width, row, col):
        """
        Checks if current exploration node row and col are in farm land boundary
        Args:
            param1: (int) Height of the farm
            param2: (int) Width of the farm
            param3: (int) current exploration node row
            param4: (int) current exploration node col
        Returns:
            (boolean) returns True if current exploration row and col within farm land
        """

        return row >= 0 and row < height and col >= 0 and col < width
