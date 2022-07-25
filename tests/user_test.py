def test_get_info(sleep_a_bit, init_users):
    user, _ = init_users
    user.user.get_user_info()
