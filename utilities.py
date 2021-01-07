# This function will remove comma from a string which to be coverted to a float or int
def un_comma(str_to_covert, type = float):
    if "," in str_to_covert:
        str_to_covert = str_to_covert.replace(",", "")
        str_to_covert = type(str_to_covert)
        return str_to_covert

    else:
        str_to_covert = type(str_to_covert)
        return str_to_covert