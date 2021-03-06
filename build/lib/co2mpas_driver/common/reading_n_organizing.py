from co2mpas_driver.common import vehicle_specs_class as vcc


def load_db_to_dictionary(db_name):
    """
    input: file (without .csv)
    return: dict of dictionaries, every dict item is a car, every dict key is
    the car's characteristic's name, and the value returned from the key is the
    value of the characteristic

    """
    # reading csv file into dictionary
    with open(db_name + '.csv', 'r', encoding="ISO-8859-1") as file:
        header_line = file.readline()  # returns the header line in the file
        characteristics = []
        out = {}

        # create the list of the names of the characteristic
        while header_line != '':
            k = header_line.find(',')
            if k == -1:
                characteristics.append(header_line)
                header_line = ''
            else:
                characteristics.append(header_line[:k])
                header_line = header_line[k + 1:]

        # for every line of the csv creates a dictionary
        # then for every cell of the line, stores the value to the dictionary
        # using the characteristic's name as key
        for line in file:
            C = {}
            for i in range(len(characteristics) - 1):
                k = line.find(',')
                C[characteristics[i]] = line[:k]
                line = line[k + 1:]
            C[characteristics[-1].rstrip('\n')] = line.rstrip('\n')
            out[int(C[characteristics[0]])] = C

        return out


def get_vehicle_from_db(db_dict, car_id, **kwargs):
    """

    kwargs can be:
    lco = True          # Light co2mpas is to be used, so the relevant parameters must be imported
    electric = True     # The vehicle is an EV

    :param db_dict: dict of dicts ,A dictionary produced by the "load_db_to_dictionary@" function
    :param car_id: int, The car id in the db
    :return: veh_specs object

    """
    # select desired car with its id
    my_car = db_dict[car_id]

    my_car_specs = vcc.VehSpecs(my_car, **kwargs)

    return my_car_specs