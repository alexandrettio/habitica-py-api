import pytest


@pytest.mark.parametrize("quest_key, result", [("basilist", "")])
def test_invite_users_to_quest(
    quest_key, result, join_group, group_leave, quest_cancel
):
    """

    :param quest_key: Name of quest we try to use
    :param result: TODO
    :param join_group: fixture user1 joins group owned by user2.
    :param group_leave: user1 leaves group owned by user2.
    :param quest_cancel: user1 cancels his not started quest.
    :return:
    """
    user1, user2 = join_group
    r = user1.quest.invite(quest_key)
    assert str(r.data.quest_leader) == user1.user_id
