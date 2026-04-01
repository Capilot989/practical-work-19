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

class Segment:
    """
    A class representing a line segment defined by two points.

    This class checks whether the segment intersects the coordinate axes
    (X-axis or Y-axis).

    Attributes:
        coordinates: Tuple containing the two Point objects that define the segment
        one_intersection: Boolean indicating if the segment intersects exactly one axis
    """
    def __init__(self, dot_1_obj: 'Point', dot_2_obj: 'Point') -> None:
        """
        Initialize a new Segment instance.

        Args:
            dot_1_obj: First endpoint of the segment
            dot_2_obj: Second endpoint of the segment
        """
        self.coordinates = (dot_1_obj, dot_2_obj)
        self.one_intersection = self.check_intersection()

    def check_intersection(self) -> bool:
        """
        Check if the segment intersects exactly one coordinate axis.

        A segment intersects the X-axis if the y-coordinates have opposite signs.
        A segment intersects the Y-axis if the x-coordinates have opposite signs.

        Returns:
            True if the segment intersects exactly one axis (X or Y, but not both),
            False otherwise
        """
        point_1, point_2 = self.coordinates
        x1, y1 = point_1.get_x(), point_1.get_y()
        x2, y2 = point_2.get_x(), point_2.get_y()

        x_intersection = int(y1 * y2 <= 0)
        y_intersection = int(x1 * x2 <= 0)
        return (x_intersection + y_intersection) == 1

    def __str__(self) -> str:
        """
        Get string representation of the segment.

        Returns:
            String in format '(point1, point2)'
        """
        return f'({self.coordinates[0]}, {self.coordinates[1]})'

    def __repr__(self) -> str:
        """
        Get unambiguous string representation of the segment.

        Returns:
            String in format '(point1, point2)'
        """
        return f'({self.coordinates[0]}, {self.coordinates[1]})'

class СoordinateSystem:
    """
    A class representing a coordinate system containing multiple segments.

    This class stores segments and provides methods to add segments and count
    those that intersect exactly one coordinate axis.

    Attributes:
        segments: List of Segment objects in the coordinate system
    """

    def __init__(self) -> None:
        """
        Initialize a new CoordinateSystem instance with an empty list of segments.
        """
        self.segments = []

    def add_segment(self, segment: 'Segment') -> None:
        """
        Add a segment to the coordinate system.

        Args:
            segment: Segment object to add
        """
        self.segments.append(segment)

    def axis_intersection(self) -> int:
        """
        Count segments that intersect exactly one coordinate axis.

        Returns:
            Number of segments that intersect exactly one axis (X or Y)
        """
        return sum(1 for s in self.segments if s.one_intersection)

    def __str__(self) -> str:
        """
        Get string representation of all segments in the coordinate system.

        Returns:
            String in format '[segment1, segment2, ...]'
        """
        return f"[{', '.join(str(s) for s in self.segments)}]"
