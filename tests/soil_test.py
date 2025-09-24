import pytest
from classes.soil import Soil

@pytest.fixture
def soil_default():
    return Soil()

@pytest.fixture
def soil_parameterized():
    return Soil(100, 100)

def test_soil_equals_01(soil_default):
    soil_obj = Soil()
    assert soil_default == soil_obj

def test_soil_equals_02(soil_parameterized):
    soil_obj = Soil(100, 100)
    assert soil_parameterized == soil_obj

def test_soil_equals_03(soil_default, soil_parameterized):
    assert soil_default != soil_parameterized

def test_soil_equals_04(soil_parameterized):
    soil_obj = Soil(100, 99)
    assert soil_parameterized != soil_obj

def test_soil_default(soil_default):
    assert soil_default.price == 0
    assert soil_default.fertilizer_amount == 0
    assert soil_default.water_amount == 0

def test_soil_parameterized(soil_parameterized):
    assert soil_parameterized.price == 0
    assert soil_parameterized.fertilizer_amount == 100
    assert soil_parameterized.water_amount == 100

def test_get_fertilizer_amount_01(soil_default):
    assert soil_default.fertilizer_amount == 0

def test_get_fertilizer_amount_02(soil_parameterized):
    assert soil_parameterized.fertilizer_amount == 100

def test_get_water_amount_01(soil_default):
    assert soil_default.water_amount == 0

def test_get_water_amount_02(soil_parameterized):
    assert soil_parameterized.water_amount == 100

def test_set_fertilizer_amount_01(soil_default):
    soil_default.fertilizer_amount = 50
    assert soil_default.fertilizer_amount == 50

def test_set_fertilizer_amount_02(soil_default):
    with pytest.raises(ValueError):
        soil_default.fertilizer_amount = -1

def test_set_fertilizer_amount_03(soil_default):
    soil_default.fertilizer_amount = 101
    assert soil_default.fertilizer_amount == 100

def test_set_fertilizer_amount_04(soil_parameterized):
    soil_parameterized.fertilizer_amount = 50
    assert soil_parameterized.fertilizer_amount == 50

def test_set_fertilizer_amount_05(soil_parameterized):
    with pytest.raises(ValueError):
        soil_parameterized.fertilizer_amount = -1

def test_set_fertilizer_amount_06(soil_parameterized):
    soil_parameterized.fertilizer_amount = 101
    assert soil_parameterized.fertilizer_amount == 100

def test_set_water_amount_01(soil_default):
    soil_default.water_amount = 50
    assert soil_default.water_amount == 50

def test_set_water_amount_02(soil_default):
    with pytest.raises(ValueError):
        soil_default.water_amount = -1

def test_set_water_amount_03(soil_default):
    soil_default.water_amount = 101
    assert soil_default.water_amount == 100

def test_set_water_amount_04(soil_parameterized):
    soil_parameterized.water_amount = 50
    assert soil_parameterized.water_amount == 50

def test_set_water_amount_05(soil_parameterized):
    with pytest.raises(ValueError):
        soil_parameterized.water_amount = -1

def test_set_water_amount_06(soil_parameterized):
    soil_parameterized.water_amount = 101
    assert soil_parameterized.water_amount == 100

def test_is_fertilized_01(soil_default):
    assert not soil_default.is_fertilized()

def test_is_fertilized_02(soil_parameterized):
    assert soil_parameterized.is_fertilized()

def test_is_fertilized_03():
    soil_obj = Soil(0, 100)
    assert not soil_obj.is_fertilized()

def test_is_fertilized_04():
    soil_obj = Soil(100, 2)
    assert soil_obj.is_fertilized()

def test_is_watered_01(soil_default):
    assert not soil_default.is_watered()

def test_is_watered_02(soil_parameterized):
    assert soil_parameterized.is_watered()

def test_is_watered_03():
    soil_obj = Soil(100, 0)
    assert not soil_obj.is_watered()

def test_is_watered_04():
    soil_obj = Soil(0, 100)
    assert soil_obj.is_watered()
