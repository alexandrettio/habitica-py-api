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


def test_delete(sleep_a_bit, init_users):
    user, _ = init_users
    data = {
        "text": "Test task to be deleted",
        "type": TaskType.TODO.value,
        "priority": PriorityType.MEDIUM.value,
    }
    r = user.task.create(data)
    task_id = r.data.id
    r = user.task.delete(task_id)
    assert r.success
