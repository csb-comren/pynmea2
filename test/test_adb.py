import pynmea2
from decimal import Decimal

def test_adbt():
    data = '$PADBT,000.000,f,019.04,M,000.000,F*3C'
    msg = pynmea2.parse(data)
    assert type(msg) == pynmea2.adb.ADBT
    assert msg.manufacturer == 'ADB'
    assert msg.subtype == 'T'
    assert msg.depth_feet == Decimal('0')
    assert msg.unit_feet == 'f'
    assert msg.depth_meters == Decimal('19.04')
    assert msg.unit_meters == 'M'
    assert msg.depth_fathoms == Decimal('0')
    assert msg.unit_fathoms == 'F'
    assert msg.render() == data
