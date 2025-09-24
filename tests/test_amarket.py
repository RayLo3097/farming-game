import pytest
from classes.amarket import Market
from classes.inventory import Inventory
from classes.player import Player
from classes.item import Items


# Fixture for creating a test player
@pytest.fixture
def test_player():
    return Player(name="TestPlayer", age=30, money=100.0)

# Fixture for creating an inventory
@pytest.fixture
def test_inventory():
    # Inventory is empty at this point
    return Inventory()

# Fixture for creating a test market with predefined inventory and player
@pytest.fixture
def test_market(test_inventory, test_player):
    products = [
        Items(name="Hemp seeds", price=1.0, sellprice=1.2, quantity=10, description="These are hemp seeds",  image="../assets/itemImages/hempseeds.png"),
        Items(name="Raspberry seeds", price=1.5, sellprice=1.7, quantity=15, description="This is a raspberry seeds",  image="../assets/itemImages/raspberryseeds.png")
    ]
    return Market(products=products, inventory=test_inventory, player=test_player)

# Test to ensure market initializes correctly
def test_market_initialization(test_market):
    assert len(test_market.products) == 2, "Market should initialize with 2 products."
    assert test_market.marketCapacity == 25, "Market capacity should be initialized to 25."

# Test for listing products in the market
def test_list_products(test_market, capsys):
    # List products and capture the output
    Market.listProducts(test_market.getProducts())
    captured = capsys.readouterr()
    assert "Hemp seeds" in captured.out, "Hemp seeds should be listed in the market products."
    assert "Raspberry seeds" in captured.out, "Raspberry seeds should be listed in the market products."

# Test for retrieving products from the market
def test_get_products(test_market):
    products = test_market.getProducts()
    assert len(products) == 2, "getProducts should return 2 products."

# Test for retrieving the market's capacity
def test_get_market_cap(test_market):
    assert test_market.getMarketCap() == 25, "getMarketCap should return the market capacity of 25."

# Test for adding a new product to the market
def test_add_product(test_market):
    test_market.addProduct(
        name="Blueberry seeds", price=0.8, sellprice=0.9, quantity=20, description="These are blueberry seeds", image="../assets/itemImages/blueberryseeds.png", seed=None
    )
    assert any(product.name == "Blueberry seeds" for product in test_market.products), "Blueberry seeds should be added to the market products."

# Test for adding a product to a market that is already at capacity
def test_add_product_to_full_market(test_market):
    # Fill the market to its capacity
    for i in range(test_market.getMarketCap() - len(test_market.getProducts())):
        test_market.addProduct(
            name=f"Product{i}", price=1.0, sellprice=1.1, quantity=5, description=f"Product{i} description", image="../assets/itemImages/water.png", seed=None
        )
    # Verify the market is full and attempting to add another product raises an exception
    assert len(test_market.products) == test_market.getMarketCap(), "Market should be full now."
    with pytest.raises(Exception):
        test_market.addProduct(
            name="OverflowProduct", price=2.0, sellprice=2.5, quantity=5, description="Overflow product", image="../assets/itemImages/water.png", seed=None
        )

# Test for removing a product from the market
def test_remove_product(test_market):
    product_to_remove = test_market.products[0]
    success = test_market.removeProduct(product_to_remove.name)
    assert success, "Should successfully remove a product from the market."
    assert product_to_remove not in test_market.products, "Removed product should not be in the market."

# Test for attempting to remove a product that does not exist in the market
def test_remove_nonexistent_product(test_market):
    success = test_market.removeProduct("Nonexistent")
    assert not success, "Should not successfully remove a product that does not exist."

# Test for selling a product that is in the inventory
def test_sell_product(test_market, test_player):
    product_to_sell = test_market.products[0]
    test_market.inventory.add_item(product_to_sell)
    test_market.sellProduct(product_to_sell)
    assert test_player.getMoney() == 100.0 + product_to_sell.sellprice, "Player's money should increase by the product's sell price."

# Test for attempting to sell a product not present in the inventory
def test_sell_product_not_in_inventory(test_market, test_player):
    product_to_sell = test_market.products[0]
    success = test_market.sellProduct(product_to_sell)
    assert not success, "Should not be able to sell a product that is not in the inventory."

# Test for buying a product from the market
def test_buy_product(test_market, test_player):
    product_to_buy = test_market.products[0]
    initial_money = test_player.getMoney()
    success = test_market.buyProduct(product_to_buy)
    assert success, "Should successfully buy a product from the market."
    assert test_player.getMoney() == initial_money - product_to_buy.price, "Player's money should decrease by the product's price."
