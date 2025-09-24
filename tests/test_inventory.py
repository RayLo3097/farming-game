
#imports
import pytest 
from classes.seed import Seed
from classes.item import Items
from classes.inventory import Inventory


#initialization tests
@pytest.fixture
def default_inventory():
    return Inventory()

@pytest.fixture
def water_item():
    return Items("water", 15.0, 7.5, 0, "tool", "assets/itemImages/water.png")

@pytest.fixture
def fertilizer_item():
    fertilizer = Items("fertilizer", 30.0, 15.0, 0, "tool", "assets/itemImages/fertilizer.png")
    return fertilizer

@pytest.fixture
def cornseed_item():
    corn_seed = Seed("corn seeds", "corn", 50.0, 25.0, .1, 50, 112)
    return Items("corn seeds", 50.0, 25.0, 1, corn_seed, "assets/itemImages/corn.png")

@pytest.fixture
def blueberryseed_item():
    blueberry_seed = Seed("blueberry seeds", "blueberry", 200.0, 100.0, 10, 50, 112)
    return Items("blueberry seeds", 200.0, 100.0, 1, blueberry_seed, "assets/itemImages/blueberryseeds.png")

@pytest.fixture
def raspberryseed_item():
    raspberry_seed = Seed("raspberry seeds", "raspberry", 200.0, 100.0, 10, 50, 112)
    return Items("raspberry seeds", 200.0, 100.0, 1, raspberry_seed, "assets/itemImages/raspberryseeds.png")

def test_inventory_init(default_inventory):
    assert default_inventory.capacity == 10
    assert default_inventory.handCapacity == 1
    assert default_inventory.contents == {}
    assert default_inventory.handContents == {}

def test_add_water_item(default_inventory, water_item):
    default_inventory.add_item(water_item)
    retrieved_item = default_inventory.contents.get(water_item.name)
    assert retrieved_item.name == water_item.name

def test_add_fertilizer_item(default_inventory, fertilizer_item):
    default_inventory.add_item(fertilizer_item)
    retrieved_item = default_inventory.contents.get(fertilizer_item.name)
    assert retrieved_item.name == fertilizer_item.name

def test_add_cornseed_item(default_inventory, cornseed_item):
    default_inventory.add_item(cornseed_item)
    retrieved_item = default_inventory.contents.get(cornseed_item.name)
    assert retrieved_item.name == cornseed_item.name

def test_add_multiple_items(default_inventory, cornseed_item, blueberryseed_item, raspberryseed_item):
    default_inventory.add_item(cornseed_item)
    default_inventory.add_item(blueberryseed_item)
    default_inventory.add_item(raspberryseed_item)
    retrieved_item = default_inventory.contents.get(raspberryseed_item.name)
    assert retrieved_item.name == raspberryseed_item.name
    retrieved_item = default_inventory.contents.get(blueberryseed_item.name)
    assert retrieved_item.name == blueberryseed_item.name
    retrieved_item = default_inventory.contents.get(cornseed_item.name)
    assert retrieved_item.name == cornseed_item.name

def test_add_multiple_items_same_item(default_inventory, cornseed_item, blueberryseed_item, raspberryseed_item):
    default_inventory.add_item(cornseed_item)
    default_inventory.add_item(cornseed_item)
    default_inventory.add_item(cornseed_item)
    retrieved_item = default_inventory.contents.get(cornseed_item.name)
    assert retrieved_item.quantity == 3

def test_add_multiple_items_same_and_different(default_inventory, cornseed_item, blueberryseed_item, water_item, fertilizer_item):
    default_inventory.add_item(cornseed_item)
    default_inventory.add_item(cornseed_item)
    default_inventory.add_item(cornseed_item)
    default_inventory.add_item(blueberryseed_item)
    default_inventory.add_item(blueberryseed_item)
    default_inventory.add_item(water_item)
    default_inventory.add_item(water_item)
    default_inventory.add_item(water_item)
    default_inventory.add_item(water_item)
    default_inventory.add_item(water_item)
    default_inventory.add_item(fertilizer_item)
    default_inventory.add_item(fertilizer_item)
    default_inventory.add_item(fertilizer_item)
    default_inventory.add_item(fertilizer_item)
    # Check corn seed    
    retrieved_item = default_inventory.contents.get(cornseed_item.name)
    assert retrieved_item == cornseed_item
    assert retrieved_item.quantity == 3
    # Check blueberry seed
    retrieved_item = default_inventory.contents.get(blueberryseed_item.name)
    assert retrieved_item == blueberryseed_item
    assert retrieved_item.quantity == 2
    # Check water
    retrieved_item = default_inventory.contents.get(water_item.name)
    assert retrieved_item == water_item
    assert retrieved_item.quantity == 5
    # Check fertilizer
    retrieved_item = default_inventory.contents.get(fertilizer_item.name)
    assert retrieved_item == fertilizer_item
    assert retrieved_item.quantity == 4

def test_add_handitem(default_inventory, water_item):
    default_inventory.add_handitem(water_item)
    retrieved_item = default_inventory.handContents.get(water_item.name)
    assert retrieved_item == water_item

def test_add_multiple_handitems(default_inventory, water_item, fertilizer_item):
    default_inventory.add_handitem(water_item)
    default_inventory.add_handitem(fertilizer_item)
    retrieved_item_1 = default_inventory.handContents.get(water_item.name)
    retrieved_item_2 = default_inventory.handContents.get(fertilizer_item.name)
    assert retrieved_item_1 is None
    assert retrieved_item_2 == fertilizer_item
    assert len(default_inventory.handContents) == default_inventory.handCapacity
