import pynmea2
from decimal import Decimal

def test_rdid():
    data = '$PTNTHPR,91.7,N,-0.0,N,1.6,N*00'
    msg = pynmea2.parse(data)
    assert type(msg) == pynmea2.tnt.TNTHPR
    assert msg.manufacturer == 'TNT'
    assert msg.subtype == 'HPR'
    assert msg.heading == Decimal('91.7')
    assert msg.mag_stat == 'N'
    assert msg.pitch == Decimal('-0.0')
    assert msg.pitch_stat == 'N'
    assert msg.roll == Decimal('1.6')
    assert msg.roll_stat == 'N'
    assert msg.render(checksum=False) == data
