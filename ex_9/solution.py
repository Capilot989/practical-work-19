class StrandsDNA:
    """
    A class for managing DNA strand sequences.

    This class stores multiple DNA strands (represented as strings) and provides
    methods to add strands, find the longest strands, and get string representation.

    Attributes:
        all_strands: List of all DNA strands stored
    """
    def __init__(self) -> None:
        """
        Initialize a new StrandsDNA instance with an empty list of strands.
        """
        self.all_strands = []

    def add_strands(self, strands: str) -> None:
        """
        Add DNA strands to the collection.

        Splits the input string by whitespace and appends each strand to the list.

        Args:
            strands: Space-separated string of DNA strands
        """
        self.all_strands += strands.split()

    def get_max_strands(self) -> str:
        """
        Get the longest DNA strands sorted alphabetically.

        Finds the maximum length among all stored strands, filters strands
        of that length, sorts them alphabetically, and returns as a space-separated string.

        Returns:
            Space-separated string of the longest strands sorted alphabetically
        """
        max_len = max([len(strand) for strand in self.all_strands])
        result = filter(lambda x: len(x) == max_len, self.all_strands)
        return ' '.join(sorted(result))

    def __str__(self) -> None:
        """
        Get string representation of all stored DNA strands.

        Returns:
            Space-separated string of all strands
        """
        return f"{' '.join(self.all_strands)}"
