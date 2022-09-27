from pyrecord import Record


class Address:
    Address = Record.create_type(
        "id", "street", "number", "district", "city", "state", "zip")
