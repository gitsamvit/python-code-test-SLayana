cooling_type = {
    "passive_cooling": {"lowerlimit": 0, "upperlimit": 35},
    "high_active_cooling": {"lowerlimit": 0, "upperlimit": 45},
    "med_active_cooling": {"lowerlimit": 0, "upperlimit": 40},
}

breach_type = {"normal": "NORMAL", "too_high": "TOO_HIGH", "too_low": "TOO_LOW"}


def infer_breach(value, lowerLimit, upperLimit):
    if value < lowerLimit:
        return breach_type["too_low"]
    if value > upperLimit:
        return breach_type["too_high"]
    return breach_type["normal"]


def classify_temperature_breach(coolingType, temperatureInC):
    lowerLimit = cooling_type[coolingType][lowerLimit]
    upperLimit = cooling_type[coolingType][upperLimit]
    return infer_breach(temperatureInC, lowerLimit, upperLimit)


def check_and_alert(alertTarget, batteryChar, temperatureInC):
    breachType = classify_temperature_breach(batteryChar["coolingType"], temperatureInC)
    if alertTarget == "TO_CONTROLLER":
        send_to_controller(breachType)
    elif alertTarget == "TO_EMAIL":
        send_to_email(breachType)


def send_to_controller(breachType):
    header = 0xFEED
    print(f"{header}, {breachType}")


def send_to_email(breachType):
    recepient = "a.b@c.com"
    if breachType == "TOO_LOW":
        print(f"To: {recepient}")
        print("Hi, the temperature is too low")
    elif breachType == "TOO_HIGH":
        print(f"To: {recepient}")
        print("Hi, the temperature is too high")
