import pytest
from classes.seed import Seed
from classes.soil import Soil
from classes.plot import Plot

@pytest.fixture
def plot_default():
    return Plot()

@pytest.fixture
def carrot_plot_parameterized():
    carrot_seed = Seed("carrot", 10, 20, 60, 40, 80)
    mySoil = Soil(100, 100)
    return Plot(mySoil, carrot_seed)

def test_plot_default(plot_default):
    assert plot_default.soil is None
    assert plot_default.seed is None

def test_plot_parameterized(carrot_plot_parameterized):
    get_soil = carrot_plot_parameterized.soil
    get_seed = carrot_plot_parameterized.seed
    assert get_soil.water_amount == 100
    assert get_soil.fertilizer_amount == 100
    
    assert get_seed.crop_name == "carrot"
    assert get_seed.price == 10
    assert get_seed.growth_time == 60
    assert get_seed.min_temperature == 40
    assert get_seed.max_temperature == 80

def test_get_soil_01(plot_default):
    assert plot_default.soil is None

def test_get_soil_02(carrot_plot_parameterized):
    test_soil = Soil(100, 100)
    get_soil = carrot_plot_parameterized.soil
    assert get_soil == test_soil

def test_get_seed_01(plot_default):
    get_seed = plot_default.seed
    assert get_seed is None

def test_get_seed_02(carrot_plot_parameterized):
    test_seed = Seed("carrot", 10, 20, 60, 40, 80)
    get_seed = carrot_plot_parameterized.seed
    assert get_seed == test_seed

def test_get_price_01(plot_default):
    get_price = plot_default.price
    assert get_price == 0

def test_get_price_02(carrot_plot_parameterized):
    get_price = carrot_plot_parameterized.price
    assert get_price == 0

def test_set_soil_01(plot_default):
    test_soil = Soil(100, 100)
    plot_default.soil = test_soil
    get_soil = plot_default.soil
    assert get_soil == test_soil

def test_set_soil_02(carrot_plot_parameterized):
    test_soil = Soil(100, 95)
    carrot_plot_parameterized.soil = test_soil
    get_soil = carrot_plot_parameterized.soil
    assert get_soil == test_soil

def test_set_soil_03(plot_default):
    test_soil = "carrot"
    with pytest.raises(ValueError):
        plot_default.soil = test_soil

def test_set_soil_04(carrot_plot_parameterized):
    test_soil = "potato"
    with pytest.raises(ValueError):
        carrot_plot_parameterized.soil = test_soil

def test_set_seed_01(plot_default):
    test_seed = Seed("carrot", 10, 60, 40, 80)
    plot_default.seed = test_seed
    get_seed = plot_default.seed
    assert get_seed == test_seed

def test_set_seed_02(carrot_plot_parameterized):
    test_seed = Seed("potato", 20, 90, 65, 80)
    carrot_plot_parameterized.seed = test_seed
    get_seed = carrot_plot_parameterized.seed
    assert get_seed == test_seed

def test_set_seed_03(plot_default):
    test_seed = "carrot seed"
    with pytest.raises(ValueError):
        plot_default.seed = test_seed

def test_set_seed_04(carrot_plot_parameterized):
    test_seed = "potato seed"
    with pytest.raises(ValueError):
        carrot_plot_parameterized.seed = test_seed

def test_plant_seed_01(plot_default):
    seed_to_plant = Seed("carrot", 10, 60, 40, 80)
    plot_default.plant_seed(seed_to_plant)
    get_seed = plot_default.seed
    assert get_seed == seed_to_plant

def test_plant_seed_02(carrot_plot_parameterized):
    seed_to_plant = Seed("potato", 20, 90, 65, 80)
    with pytest.raises(ValueError, match=r"Plot already has a seed planted"):
        carrot_plot_parameterized.plant_seed(seed_to_plant)

def test_plant_seed_03(carrot_plot_parameterized):
    seed_to_plant = None
    with pytest.raises(ValueError, match=r"The given seed is not a Seed object"):
        carrot_plot_parameterized.plant_seed(seed_to_plant)

def test_plant_seed_04(carrot_plot_parameterized):
    seed_to_plant = "potato"
    with pytest.raises(ValueError, match=r"The given seed is not a Seed object"):
        carrot_plot_parameterized.plant_seed(seed_to_plant)

def test_remove_seed_01(plot_default):
    plot_default.remove_seed()
    get_seed = plot_default.seed
    assert get_seed is None

def test_remove_seed_02(carrot_plot_parameterized):
    carrot_plot_parameterized.remove_seed()
    get_seed = carrot_plot_parameterized.seed
    assert get_seed is None

def test_water_plot_01(plot_default):
    get_soil = plot_default.soil
    with pytest.raises(ValueError, match=r"Plot has no soil"):
        plot_default.water_plot(100)

def test_water_plot_02(plot_default):
    test_soil = Soil(100, 0)
    plot_default.soil = test_soil
    plot_default.water_plot(100)
    get_soil = plot_default.soil
    assert get_soil.water_amount == 100

def test_water_plot_03(carrot_plot_parameterized):
    get_soil = carrot_plot_parameterized.soil
    assert get_soil.water_amount == 100
    carrot_plot_parameterized.water_plot(100)
    get_soil = carrot_plot_parameterized.soil
    assert get_soil.water_amount == 100

def test_water_plot_04(carrot_plot_parameterized):
    get_soil = carrot_plot_parameterized.soil
    get_soil.water_amount = 5
    assert get_soil.water_amount == 5
    carrot_plot_parameterized.water_plot(60)
    assert get_soil.water_amount == 65

def test_water_plot_05(carrot_plot_parameterized):
    with pytest.raises(ValueError, match=r"Water amount cannot be negative"):
        carrot_plot_parameterized.water_plot(-10) 

def test_add_fertilizer_01(plot_default):
    get_soil = plot_default.soil
    with pytest.raises(ValueError, match=r"Plot has no soil"):
        plot_default.add_fertilizer(100)

def test_add_fertilizer_02(plot_default):
    test_soil = Soil(50, 100)
    plot_default.soil = test_soil
    plot_default.add_fertilizer(100)
    get_soil = plot_default.soil
    assert get_soil.fertilizer_amount == 100

def test_add_fertilizer_03(carrot_plot_parameterized):
    get_soil = carrot_plot_parameterized.soil
    get_soil.fertilizer_amount = 5
    assert get_soil.fertilizer_amount == 5
    carrot_plot_parameterized.add_fertilizer(80)
    get_soil = carrot_plot_parameterized.soil
    assert get_soil.fertilizer_amount == 85

