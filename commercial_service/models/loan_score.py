class LoanScore:
    def __init__(self, initialScore):
        self.score = initialScore

    def __str__(self):
        return "LoanScore(initialScore={})".format(self.initialScore)
