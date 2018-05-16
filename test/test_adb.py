import pynmea2

def test_adbt():
    data = '$PADBT,000.000,f,019.04,M,000.000,F*3C'
    msg = pynmea2.parse(data)
    assert type(msg) == pynmea2.adb.ADBT
    assert msg.manufacturer == 'ABD'
    assert msg.subtype == 'T'
    assert msg.dpf == 0
    assert msg.dpf_unit == 'f'
    assert msg.dpm == 19.04
    assert msg.dpm_unit == 'm'
    assert msg.dpF == 0
    assert msg.dpF_unit == 'F'
    assert msg.render() == data