def test_create_message(sleep_a_bit, init_users):
    user1, user2 = init_users
    response = user1.members.send_private_message("Test send private message", user2.user_id)
    assert response.success
    assert response.data.message.text == "Test send private message"


def test_get_member_profile(sleep_a_bit, init_users):
    user1, user2 = init_users
    response = user1.members.get_member_profile(user2.user_id)
    assert response.success
    assert response.data.auth.local.username == "second_test_api"


def test_get_member_achievements(init_users):
    user1, user2 = init_users
    response = user1.members.get_member_achievements(user2.user_id)
    assert response.success
    # TODO more asserts
