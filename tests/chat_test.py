def test_create_message(sleep_a_bit, group_create, group_leave):
    user, _ = group_create
    response = user.group.chat.create("party", "TestMessage")
    assert response.success
