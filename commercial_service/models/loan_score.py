class LoanScore:
    def __init__(self, loan_id, score):
        self.loan_id = loan_id
        self.score = score

    def __str__(self):
        return "LoanScore(loan_id={}, score={})".format(self.loan_id, self.score)
