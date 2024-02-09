import math

def compoundInterestCalculator(deposit, interest, multiplicationFactor):
    try:
        if deposit < 1 or interest < 0 or multiplicationFactor < 1:
            raise ValueError()
        target = deposit * multiplicationFactor
        time = math.log(target/deposit) / math.log(1 + interest/100)
        return math.ceil(time)
    except:
        raise ValueError()