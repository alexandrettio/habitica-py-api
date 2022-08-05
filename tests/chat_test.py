def test_create_message(sleep_a_bit, group_create, group_leave):
    user, _ = group_create
    response = user.group.chat.create("party", "TestMessage")
    assert response.success
    assert response.data.message.text == "TestMessage"
    assert response.data.message.username == "api_test"
