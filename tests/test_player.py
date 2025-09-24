import pytest
from classes.player import Player

@pytest.fixture()
def player_default():
    return Player()

@pytest.fixture()
def player_param():
    return Player("test", 25, 200)


# Initialization Testing


def test_defaultInit(player_default):
    assert player_default


def test_paramInit(player_param):
    assert player_param


# Getter & Setter Testing


def test_getName_default(player_default):
    assert player_default.getName() == ""


def test_getName_param(player_param):
    assert player_param.getName() == "test"


def test_getAge_default(player_default):
    assert player_default.getAge() == 0


def test_getAge_param(player_param):
    assert player_param.getAge() == 25


def test_getMoney_default(player_default):
    assert player_default.getMoney() == pytest.approx(0.0)


def test_getMoney_param(player_param):
    assert player_param.getMoney() == pytest.approx(200.0)


def test_setName_valid(player_default):
    player_default.setName("steve")
    assert player_default.getName() == "steve"


def test_setName_notString(player_param):
    with pytest.raises(Exception):
        player_param.setName(3)


def test_setName_nameTooLong(player_param):
    with pytest.raises(Exception):
        player_param.setName("aaaaaaaaaaaaaaaaa")


def test_setAge_valid(player_param):
    player_param.setAge(30)
    assert player_param.getAge() == 30


def test_setAge_notInteger(player_param):
    with pytest.raises(Exception):
        player_param.setAge("hello")


def test_setAge_underRange(player_param):
    with pytest.raises(ValueError):
        player_param.setAge(-100)


def test_setAge_overRange(player_param):
    with pytest.raises(ValueError):
        player_param.setAge(1000)


def test_inventory_accessible(player_param):
    assert player_param


# Method Testing


def test_incMoney_valid(player_param):
    player_param.incMoney(25.00)
    assert player_param.getMoney() == pytest.approx(225.0)


def test_incMoney_notFloat(player_param):
    with pytest.raises(Exception):
        player_param.incMoney(False)


def test_incMoney_negative(player_param):
    with pytest.raises(ValueError):
        player_param.incMoney(-100.0)


def test_decMoney_valid(player_param):
    player_param.decMoney(100.0)
    assert player_param.getMoney() == pytest.approx(100.0)


def test_decMoney_notFloat(player_param):
    with pytest.raises(Exception):
        player_param.decMoney("goodbye")


def test_decMoney_negative(player_param):
    with pytest.raises(ValueError):
        player_param.decMoney(-100.0)


def test_decMoney_notEnoughMoney(player_param):
    with pytest.raises(ValueError):
        player_param.decMoney(1000.0)
