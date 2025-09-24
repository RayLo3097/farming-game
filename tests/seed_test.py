import pytest
from classes.seed import Seed

@pytest.fixture
def seed_default():
    return Seed()

@pytest.fixture
def carrot_seed_parameterized():
    return Seed("carrot", 10, 20, 60, 40, 80)

@pytest.fixture
def potato_seed_parameterized():
    return Seed("potato", 20, 30, 90, 65, 80)

def test_seed_default(seed_default):
    assert seed_default.crop_name == "N/A"
    assert seed_default.price == 0
    assert seed_default.sellPrice == 0
    assert seed_default.growth_time == 0
    assert seed_default.min_temperature == 0
    assert seed_default.max_temperature == 0

def test_seed_parameterized_01(carrot_seed_parameterized):
    assert carrot_seed_parameterized.crop_name == "carrot"
    assert carrot_seed_parameterized.price == 10
    assert carrot_seed_parameterized.sellPrice == 20
    assert carrot_seed_parameterized.growth_time == 60
    assert carrot_seed_parameterized.min_temperature == 40
    assert carrot_seed_parameterized.max_temperature == 80

def test_seed_parameterized_02(potato_seed_parameterized):
    assert potato_seed_parameterized.crop_name == "potato"
    assert potato_seed_parameterized.price == 20
    assert potato_seed_parameterized.sellPrice == 30
    assert potato_seed_parameterized.growth_time == 90
    assert potato_seed_parameterized.min_temperature == 65
    assert potato_seed_parameterized.max_temperature == 80

def test_seed_equals_01(seed_default):
    assert seed_default == Seed()

def test_seed_equals_02(carrot_seed_parameterized):
    mySeed = Seed("carrot", 10, 20, 60, 40, 80)
    assert carrot_seed_parameterized == mySeed

def test_seed_equals_03(potato_seed_parameterized):
    mySeed = Seed("potato", 20, 30, 90, 65, 80)
    assert potato_seed_parameterized == mySeed

def test_seed_equals_04(carrot_seed_parameterized, potato_seed_parameterized):
    assert carrot_seed_parameterized != potato_seed_parameterized

def test_seed_equals_05(carrot_seed_parameterized, seed_default):
    assert carrot_seed_parameterized != seed_default

def test_seed_setters(carrot_seed_parameterized):
    with pytest.raises(ValueError):
        carrot_seed_parameterized.crop_name = ""
    with pytest.raises(ValueError):
        carrot_seed_parameterized.price = -1
    with pytest.raises(ValueError):
        carrot_seed_parameterized.growth_time = -1
    with pytest.raises(AttributeError):
        carrot_seed_parameterized.min_temperature = 0
    with pytest.raises(AttributeError):
        carrot_seed_parameterized.max_temperature = 0

def test_seed_crop_setter_01(seed_default):
    seed_default.crop_name = "lettuce"
    assert seed_default.crop_name == "lettuce"
    assert seed_default.price == 0
    assert seed_default.growth_time == 0
    assert seed_default.min_temperature == 0
    assert seed_default.max_temperature == 0

def test_seed_crop_setter_02(carrot_seed_parameterized):
    carrot_seed_parameterized.crop_name = "wheat"
    assert carrot_seed_parameterized.crop_name == "wheat"
    assert carrot_seed_parameterized.price == 10
    assert carrot_seed_parameterized.growth_time == 60
    assert carrot_seed_parameterized.min_temperature == 40
    assert carrot_seed_parameterized.max_temperature == 80

def test_seed_crop_setter_03(potato_seed_parameterized):
    potato_seed_parameterized.crop_name = "cabbage"
    assert potato_seed_parameterized.crop_name == "cabbage"
    assert potato_seed_parameterized.price == 20
    assert potato_seed_parameterized.growth_time == 90
    assert potato_seed_parameterized.min_temperature == 65
    assert potato_seed_parameterized.max_temperature == 80

def test_temp_require_01(seed_default):
    assert seed_default.meet_temp_requirements(0) == True

def test_temp_require_02(carrot_seed_parameterized):
    assert carrot_seed_parameterized.meet_temp_requirements(40) == True
    assert carrot_seed_parameterized.meet_temp_requirements(80) == True
    assert carrot_seed_parameterized.meet_temp_requirements(60) == True
    assert carrot_seed_parameterized.meet_temp_requirements(39) == False
    assert carrot_seed_parameterized.meet_temp_requirements(81) == False

def test_temp_require_03(potato_seed_parameterized):
    assert potato_seed_parameterized.meet_temp_requirements(65) == True
    assert potato_seed_parameterized.meet_temp_requirements(80) == True
    assert potato_seed_parameterized.meet_temp_requirements(70) == True
    assert potato_seed_parameterized.meet_temp_requirements(64) == False
    assert potato_seed_parameterized.meet_temp_requirements(81) == False
