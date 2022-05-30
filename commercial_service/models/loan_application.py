class LoanApplication:
    def __init__(self, id, personApplier, loanAmount, loanDuration, loanPurpose):
        self.id = id
        self.personApplier = personApplier
        self.loanAmount = loanAmount
        self.loanDuration = loanDuration
        self.loanPurpose = loanPurpose
    def __str__(self):
        return "LoanApplication(id={}, personApplier={}, loanAmount={}, loanDuration={}, loanPurpose={})".format(self.id, self.personApplier, self.loanAmount, self.loanDuration, self.loanPurpose)