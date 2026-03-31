
class Game:
    """
    A class representing a basketball game between two teams.

    This class tracks the scores of two teams and provides methods to
    update scores, retrieve the current score, and determine the winner.

    Attributes:
        team1: Name of the first team
        team2: Name of the second team
        score_1: Current score of the first team
        score_2: Current score of the second team
    """

    def __init__(self, teams: dict[str: str]) -> None:
        """
        Initialize a new Game instance.

        Args:
            teams: Dictionary with keys 'command1' and 'command2' containing
                   the names of the two teams
        """
        self.team1 = teams['command1']
        self.team2 = teams['command2']
        self.score_1 = 0
        self.score_2 = 0

    def ball_thrown(self, command: str, points: int) -> None:
        """
        Record points scored by a team.

        Args:
            command: Team identifier (1 for first team, 2 for second team)
            points: Number of points scored
        """
        match command:
            case 1:
                self.score_1 += points
            case 2:
                self.score_2 += points

    def get_score(self) -> tuple[int, int]:
        """
        Get the current scores of both teams.

        Returns:
            Tuple containing (score of team 1, score of team 2)
        """
        return (self.score_1, self.score_2)

    def get_winner(self) -> str:
        """
        Determine the winner of the game.

        Returns:
            Name of the winning team, or 'Ничья' (tie) if scores are equal
        """

        if self.score_1 > self.score_2:
            return self.team1
        if self.score_1 < self.score_2:
            return self.team1
        return 'Ничья'
