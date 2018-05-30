# parsing for PADBT type for hydroball

from decimal import Decimal

from ... import nmea

class ADB(nmea.ProprietarySentence):
    sentence_types = {}

    def __new__(_cls, manufacturer, data):
        name = manufacturer + data[0]
        cls = _cls.sentence_types.get(name, _cls)
        return super(ADB, cls).__new__(cls)

    def __init__(self, manufacturer, data):
        self.sentence_type = manufacturer + data[0]
        super(ADB, self).__init__(manufacturer, data)


class ADBT(ADB):
    """ PADBT
    """
    fields = (
        ("Subtype", "subtype"),
        ("Depth below surface, feet", "depth_feet", Decimal),
        ("Feet", "unit_feet"),
        ("Depth below surface, meters", "depth_meters", Decimal),
        ("Meters", "unit_meters"),
        ("Depth below surface, fathoms", "depth_fathoms", Decimal),
        ("fathoms", "unit_fathoms"),
    )
