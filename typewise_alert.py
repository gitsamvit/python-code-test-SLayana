class CoolingType:
    def __init__(self, methodName) -> None:
        self.lowerlimit = 0
        return methodName()

    def passive_cooling(self):
        self.upperlimit = 35
        return (self.lowerlimit, self.upperlimit)

    def high_active_cooling(self):
        self.upperlimit = 45
        return (self.lowerlimit, self.upperlimit)

    def med_active_cooling(self):
        self.upperlimit = 40
        return (self.lowerlimit, self.upperlimit)


class BreachType:
    def __init__(self) -> None:
        pass

    def normal():
        pass

    def too_low():
        return "the temperature is too low"

    def too_high():
        return "the temperature is too high"


class SendEmailOrController:
    def __init__(self) -> None:
        pass

    def send_to_controller(BreachType):
        header = 0xFEED
        print(f"{header}, {BreachType}")

    def send_to_email(to_recipient, BreachType):
        print(f"To: { to_recipient }")
        print(f"Hi, { BreachType }")


def infer_breach(value, lowerLimit, upperLimit):
    bt = BreachType()
    if value < lowerLimit:
        return bt.too_low
    if value > upperLimit:
        return bt.too_high
    return bt.normal


def classify_temperature_breach(coolingType, temperatureInC):
    lowerLimit, upperlimit = CoolingType(coolingType)
    return infer_breach(temperatureInC, lowerLimit, upperlimit)


def check_and_alert(alertTarget, coolingType, temperatureInC):
    sec = SendEmailOrController()
    recepient = "a.b@c.com"
    breachType = classify_temperature_breach(coolingType, temperatureInC)
    if alertTarget == "TO_CONTROLLER":
        sec.send_to_controller(breachType)
    elif alertTarget == "TO_EMAIL":
        sec.send_to_email(recepient, breachType)
