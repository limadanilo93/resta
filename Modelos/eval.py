"""Evaluation record submitted by a client for a restaurant."""


class Eval:
    """Stores a single client evaluation score.

    Attributes:
        _client: Name or identifier of the client who submitted the score.
        _score: Numeric score between 0 and 5 (inclusive).
    """

    def __init__(self, client: str, score: float):
        """Initializes an evaluation.

        Args:
            client: Name or identifier of the client.
            score: Score value, expected between 0 and 5.
        """
        self._client = client
        self._score = score
