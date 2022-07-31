def test_get_info(sleep_a_bit, init_users):
    user, _ = init_users
    user.user.get_user_info()


def test_custom_day_start(sleep_a_bit, init_users):
    user, _ = init_users
    res = user.user.set_custom_day_start(23)
    assert res.success
    assert res.data.message == "Your custom day start has changed."
    res = user.user.set_custom_day_start(2)
    assert res.success
    assert res.data.message == "Your custom day start has changed."
