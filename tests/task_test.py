def test_get_info(sleep_a_bit, init_users):
    user, _ = init_users
    r = user.task.get_info("c7ea765b-5b9f-4660-85a4-010684357373")
    print(r.data.text)
