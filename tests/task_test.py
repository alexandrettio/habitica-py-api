from consts import PriorityType, TaskType


def test_get_info(sleep_a_bit, init_users):
    user, _ = init_users
    r = user.task.get_info("c7ea765b-5b9f-4660-85a4-010684357373")
    print(r.data.text)


def test_create(sleep_a_bit, init_users):
    user, _ = init_users
    data = {
        "text": "Update Habitica API Documentation - Tasks",
        "type": "todo",
        "notes": "Update the tasks api on GitHub",
        "tags": ["ed427623-9a69-4aac-9852-13deb9c190c3"],
        "checklist": [{"text": "read wiki", "completed": True}, {"text": "write code"}],
        "priority": 2,
    }
    r = user.task.create(data)
    print(r.data.text)


def test_get_all(sleep_a_bit, init_users):
    user, _ = init_users
    r = user.task.get_all(TaskType.HABIT.value)
    print(r.data)


def test_delete(sleep_a_bit, task_create):
    user, task_id = task_create
    r = user.task.delete(task_id)
    assert r.success


def test_update(sleep_a_bit, task_create):
    user, task_id = task_create
    new_data = {
        "text": "Test task was be updated",
        "priority": PriorityType.LEGENDARY.value,
    }
    r = user.task.update(task_id, new_data)
    assert r.success
    assert r.data.text == "Test task was be updated"
    assert r.data.priority == PriorityType.LEGENDARY.value


def test_move_position(sleep_a_bit, init_users):
    user, _ = init_users
    r1 = user.task.move_new_position("35098a12-c013-4098-9f87-80a000d7fda4", 2)
    assert r1.data.index("35098a12-c013-4098-9f87-80a000d7fda4") == 2
    r2 = user.task.move_new_position("35098a12-c013-4098-9f87-80a000d7fda4", 8)
    assert r2.data.index("35098a12-c013-4098-9f87-80a000d7fda4") == 8
