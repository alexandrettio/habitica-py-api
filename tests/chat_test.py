def test_create_message(sleep_a_bit, group_create, group_leave):
    user, _ = group_create
    response = user.group.chat.create("party", "TestMessage")
    assert response.success
    assert response.data.message.text == "TestMessage"
    assert response.data.message.username == "api_test"


def test_delete_message(sleep_a_bit, group_create, message_create, group_leave):
    user, _, message_id = message_create
    response = user.group.chat.delete_message_from_group("party", message_id)
    assert response.success


def test_get_all(sleep_a_bit, group_join, message_create, group_leave):
    user1, user2 = group_join
    user1.group.chat.create("party", "Message for you, guy.")
    response = user2.group.chat.get_all()
    assert response.success
    assert len(response.data) > 1
    assert response.data[0].text == "Message for you, guy."
