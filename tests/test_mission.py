from apollo.mission import secret_message

def test_secret():
    assert secret_message() == "La profe tiene el llavero, pideselo"
