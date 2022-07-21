def test_read(init_users):
    user, _ = init_users
    r = user.notification.see_all(
        [
            "71a7c416-624a-45bc-9439-bf692d2f4f17",
        ]
    )
    assert r.success
