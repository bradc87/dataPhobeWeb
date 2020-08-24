class DPEngine():
    def calculateCompIntBalance(self, initialInvestment, intrestRate, compoundPerYear, recurringInvestment, recurringFrequency, yearsToGrow):
        x = initialInvestment * (1 + intrestRate/compoundPerYear) ** (compoundPerYear*yearsToGrow)
        return x