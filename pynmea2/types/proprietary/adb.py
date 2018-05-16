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
        ("Depth in feet", "dpf", Decimal),
        ("Depth in feet (f)", "dpf_unit"),
        ("Depth in metres", "dpm", Decimal),
        ("Depth in metres (m)", "dpm_unit"),
        ("Depth in fathoms", "dpF", Decimal),
        ("Depth in fathoms (F)", "dpF_unit"),
    )
