def parse(feet_inches):
    split = feet_inches.split(" ")
    feet = float(split[0])
    inches = float(split[1])
    return {"feet": feet, "inches": inches}


def convert(feet, inches):
    meters = feet * 0.3048 + inches * 0.0254
    # return f"{feet} feet and  {inches} inches equals {meters} meters."
    return meters
