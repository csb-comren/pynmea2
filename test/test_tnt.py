import pynmea2

def test_rdid():
    data = '$PTNTHPR,91.7,N,-0.0,N,1.6,N*00'
    msg = pynmea2.parse(data)
    assert type(msg) == pynmea2.tnt.TNTHPR
    assert msg.manufacturer == 'TNT'
    assert msg.subtype == 'HPR'
    assert msg.heading == 91.7
    assert msg.mag_stat == 'N'
    assert msg.pitch == -0.0
    assert msg.pitch_stat == 'N'
    assert msg.roll == 1.6
    assert msg.roll_stat == 'N'
    assert msg.render() == data