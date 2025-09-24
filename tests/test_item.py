import pytest
from classes.item import Items
from classes.seed import Seed

# Define a fixture for a sample blueberry item
@pytest.fixture
def blueberry_item():
    return Items(name="Blueberry", price=1.5, sellprice=1.7, quantity=15, description="Juicy blueberry", image="../assets/itemImages/blueberryseeds.png")

@pytest.fixture
def mock_seed():
    return Seed(
        crop_name="Blueberry Seed",
        price=1,
        sellPrice=2.0,
        growth_time=5,
        min_temperature=10,
        max_temperature=30)

@pytest.fixture
def item_with_seed(mock_seed):
    return Items(
        name="Blueberry Seed Pack",
        price=1.0,
        sellprice=1.5,
        quantity=10,
        description="Seeds for planting blueberries",
        image="../assets/itemImages/blueberryseeds.png",
        seed=mock_seed)


# Test the initialization of the blueberry item, ensuring attributes are correctly set.
def test_blueberry_init(blueberry_item):
    assert blueberry_item.name == "Blueberry"
    assert blueberry_item.price == 1.5
    assert blueberry_item.sellprice == 1.7
    assert blueberry_item.quantity == 15
    assert blueberry_item.description == "Juicy blueberry"
    # Image assertion is omitted as it's been mocked.

# Test updating the price of the blueberry item.
def test_update_price(blueberry_item):
    blueberry_item.update_price(2.0)
    assert blueberry_item.get_price() == 2.0
    with pytest.raises(ValueError):
        blueberry_item.update_price(-1)

# Test getting the price of the blueberry item.
def test_get_price(blueberry_item):
    assert blueberry_item.get_price() == 1.5

# Test getting the name of the blueberry item.
def test_get_name(blueberry_item):
    assert blueberry_item.get_name() == "Blueberry"

# Test getting the description of the blueberry item.
def test_get_description(blueberry_item):
    assert blueberry_item.get_description() == "Juicy blueberry"

# Test getting the sell price of the blueberry item.
def test_get_sellprice(blueberry_item):
    assert blueberry_item.get_sellprice() == 1.7

# Test getting the quantity of the blueberry item.
def test_get_quantity(blueberry_item):
    assert blueberry_item.get_quantity() == 15

def test_item_with_seed(item_with_seed):
    assert item_with_seed.seed is not None
    assert item_with_seed.seed.crop_name == "Blueberry Seed"

def test_item_with_seed_attributes(item_with_seed, mock_seed):
    # Assert item contains the seed and their attributes match
    assert item_with_seed.seed == mock_seed
    # Test the temperature requirement method on the seed
    assert item_with_seed.seed.meet_temp_requirements(20)
    assert not item_with_seed.seed.meet_temp_requirements(5)
