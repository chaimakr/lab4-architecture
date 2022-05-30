class LoanApplication:
    def __init__(self,  personApplier, loanAmount, loanDuration, loanPurpose):
        self.personApplier = personApplier
        self.loanAmount = loanAmount
        self.loanDuration = loanDuration
        self.loanPurpose = loanPurpose
    def __str__(self):
        return "LoanApplication(personApplier={}, loanAmount={}, loanDuration={}, loanPurpose={})".format(self.personApplier, self.loanAmount, self.loanDuration, self.loanPurpose)