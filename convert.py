def convert_temp(unit_in, unit_out, temp):
    """Convert farenheit <-> celsius and return results.
    """
    units = ['F', 'C']
    if unit_in.upper() == 'C' and unit_out.upper() == 'F':
        return temp * 1.8 + 32
    elif unit_in.upper() == 'F' and unit_out.upper() == 'C':
        return (temp-32)/1.8
    elif unit_in == unit_out:
        return temp
    elif unit_in.upper() not in units:
        return f'Invalid Unit {unit_in}'
    elif unit_out.upper() not in units:
        return f'Invalid Unit {unit_out}'


print(convert_temp("c", "f", 0), "should be 32.0")
print(convert_temp("f", "c", 212), "should be 100.0")
print(convert_temp("z", "f", 32), "should be Invalid unit z")
print(convert_temp("c", "z", 32), "should be Invalid unit z")
print(convert_temp("f", "f", 75.5), "should be 75.5")

