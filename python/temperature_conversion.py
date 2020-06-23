# Temperature Conversion from Celsius from/to Fahrenheit
UNITS = {
    'C':'F',
    'F':'C'
}

def convert(temp, unit):
    if unit == 'F':
        result = temp / 5 * 9 + 32
    else:
        result = (temp -32) * 5 / 9
    
    print(temp, UNITS[unit], '==>', round(result,2), unit)

def is_float(num):
    try:
        result = float(num)
    except ValueError:
        result = False
    return result

################################################################################
temp = None
unit = None

while not isinstance(temp, float):
    temp = is_float(input('Type the temperature: '))

while unit not in ['C','F']:
    unit = input('Convert to Fahrenheit or Celsius? (F / C) ').upper()

convert(temp, unit)
