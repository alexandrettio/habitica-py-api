import pytest


@pytest.mark.parametrize("quest_key, result", [("basilist", "")])
def test_invite_users_to_quest(
    quest_key, result, join_group, group_leave, quest_cancel
):
    """
    Test that user in group can invite group to existing quest.

    :param quest_key: Name of quest we try to use
    :param result: TODO
    :param join_group: fixture user1 joins group owned by user2.
    :param group_leave: user1 leaves group owned by user2.
    :param quest_cancel: user1 cancels his not started quest.
    :return:
    """
    user1, user2 = join_group
    r = user1.group.quest.invite(quest_key)
    assert str(r.data.quest_leader) == user1.user_id


def test_cancel_not_active_quest(join_group, quest_invite, group_leave):
    """
    Test that user can cancel not active quest.

    :param join_group: fixture user1 joins group owned by user2.
    :param quest_invite: user1 invites team to his quest.
    :param group_leave: user1 leaves group owned by user2.
    :return:
    """
    user1, user2 = join_group
    r = user1.group.quest.cancel()
    assert not r.data.active


def test_quest_start_when_all_accepted(join_group, group_leave, quest_abort):
    """
    Test that when all members accepted the quest it'll be started.

    :param join_group: fixture user1 joins group owned by user2.
    :param group_leave: user1 leaves group owned by user2.
    :param quest_abort: user1 cancels his started quest.
    :return:
    """
    user1, user2 = join_group
    user1.group.quest.invite("basilist")
    r = user2.group.quest.accept()
    assert r.data.active
    assert r.data.key == "basilist"
    assert r.data.progress.hp == 100


def test_quest_start_when_all_answered():
    pass


def test_quest_force_start():
    pass


def test_quest_abort_active_quest():
    pass


def test_quest_infi(init_users):
    pass
