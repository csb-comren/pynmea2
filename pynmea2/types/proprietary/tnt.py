# parsing for PTNTHPR type for hydroball

from decimal import Decimal

from ... import nmea


class TNT(nmea.ProprietarySentence):
    sentence_types = {}

    def __new__(_cls, manufacturer, data):
        name = manufacturer + data[0]
        # print(name)
        cls = _cls.sentence_types.get(name, _cls)
        return super(TNT, cls).__new__(cls)

    def __init__(self, manufacturer, data):
        self.sentence_type = manufacturer + data[0]
        super(TNT, self).__init__(manufacturer, data)


class TNTHPR(TNT):
    """ PTNTHPR
    """
    fields = (
        ("Subtype", "subtype"),
        ("Heading", "heading", Decimal),
        ("Magnetic field status", "mag_stat"),
        ("Pitch", "pitch", Decimal),
        ("Pitch status", "pitch_stat"),
        ("Roll", "roll", Decimal),
        ("Roll status", "roll_stat"),
    )
#
# Keys for statuses in TNTHPR:
#     L = low alarm,
#     M = low warning,
#     N = normal,
#     O = high warning, or
#     P = high alarm.
#     C = Tuning analog circuit
#
