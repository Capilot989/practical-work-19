
class Point:
    """
    A class representing a point in 2D Cartesian coordinate system.

    This class provides methods to access coordinates, calculate distance
    to another point, add points together, and get string representation.

    Attributes:
        get_x_cords: X-coordinate of the point
        get_y_cords: Y-coordinate of the point
    """
    def __init__(self, coordinates: tuple[int, int]=(0, 0)) -> None:
        """
        Initialize a new Point instance.

        Args:
            coordinates: Tuple containing (x, y) coordinates. Defaults to (0, 0)
        """
        self.get_x_cords = coordinates[0]
        self.get_y_cords = coordinates[1]

    def get_x(self) -> int:
        """
        Get the x-coordinate of the point.

        Returns:
            X-coordinate as integer
        """
        return self.get_x_cords

    def get_y(self) -> int:
        """
        Get the y-coordinate of the point.

        Returns:
            Y-coordinate as integer
        """
        return self.get_y_cords

    def distance(self, other: 'Point') -> float:
        """
        Calculate Euclidean distance between this point and another point.

        Args:
            other: Another Point object

        Returns:
            Euclidean distance as float
        """
        self_x = self.get_x()
        self_y = self.get_y()

        other_x = other.get_x()
        other_y = other.get_y()

        distance = ((other_x - self_x) ** 2
                    + (other_y - self_y) ** 2) ** 0.5
        return distance

    def sum(self, other: 'Point') -> 'Point':
        """
        Add two points by summing their coordinates.

        Args:
            other: Another Point object

        Returns:
            New Point object with coordinates (x1 + x2, y1 + y2)
        """
        new_x = self.get_x() + other.get_x()
        new_y = self.get_y() + other.get_y()
        new_coordinates = (new_x, new_y)
        return Point(new_coordinates)

    def __str__(self):
        """
        Get string representation of the point.

        Returns:
            String in format '(x, y)'
        """
        coordinates = (self.get_x(), self.get_y())
        return f'{coordinates}'
