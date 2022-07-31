import pytest

from habitica.error import BadRequestError


def test_get_info(sleep_a_bit, init_users):
    user, _ = init_users
    user.user.get_user_info()


def test_custom_day_start_correct(sleep_a_bit, init_users):
    user, _ = init_users
    res = user.user.set_custom_day_start(23)
    assert res.success
    assert res.data.message == "Your custom day start has changed."
    res = user.user.set_custom_day_start(2)
    assert res.success
    assert res.data.message == "Your custom day start has changed."


def test_custom_day_start_wrong(sleep_a_bit, init_users):
    user, _ = init_users
    try:
        user.user.set_custom_day_start(-3)
    except BadRequestError as e:
        assert e.message == "User validation failed"


@pytest.mark.skip(reason="No idea how to be sure we have an egg and a potion.")
def test_hatch_pet(init_users):
    user, _ = init_users
    res = user.user.hatch_pet("BearCub", "RoyalPurple")
    assert res.success
    assert res.data.message == "Your egg hatched! Visit your stable to equip your pet."
