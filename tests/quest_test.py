import pytest


@pytest.mark.parametrize("quest_key, result", [("basilist", "")])
def test_invite_users_to_quest(
    quest_key, result, sleep_a_bit, join_group, group_leave, quest_cancel
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


def test_cancel_not_active_quest(sleep_a_bit, join_group, quest_invite, group_leave):
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


def test_quest_start_when_all_accepted(
    sleep_a_bit, join_group, group_leave, quest_abort
):
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
    members_count = 0
    for member_id in r.data.members:
        if r.data.members[member_id]:
            members_count += 1
    assert members_count == 2


def test_quest_start_when_all_answered(
    sleep_a_bit, join_group, group_leave, quest_abort
):
    """
    Test that when all members answered no matter accept or reject the quest it'll be started.

    :param join_group: fixture user1 joins group owned by user2.
    :param group_leave: user1 leaves group owned by user2.
    :param quest_abort: user1 cancels his started quest.
    :return:
    """
    user1, user2 = join_group
    user1.group.quest.invite("basilist")
    r = user2.group.quest.reject()
    assert r.data.active
    assert r.data.key == "basilist"
    assert r.data.progress.hp == 100
    members_count = 0
    for member_id in r.data.members:
        if r.data.members[member_id]:
            members_count += 1
    assert members_count == 1


def test_quest_force_start(sleep_a_bit, join_group, group_leave, quest_abort):
    """
    Test that when all members answered no matter accept or reject the quest it'll be started.

    :param join_group: fixture user1 joins group owned by user2.
    :param group_leave: user1 leaves group owned by user2.
    :param quest_abort: user1 cancels his started quest.
    :return:
    """
    user1, _ = join_group
    user1.group.quest.invite("basilist")
    r = user1.group.quest.force_start()
    assert r.data.active
    assert r.data.key == "basilist"
    assert r.data.progress.hp == 100
    members_count = 0
    for member_id in r.data.members:
        if r.data.members[member_id]:
            members_count += 1
    assert members_count == 1
