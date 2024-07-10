class PrimeFactor:

    def of(self, number) -> list:
        factors = []
        if number > 1:
            if number == 4:
                factors.append(2)
                factors.append(2)
            else:
                factors.append(number)
        return factors
