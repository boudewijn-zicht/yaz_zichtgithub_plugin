import yaz

from yaz_zichtgithub_plugin import ZichtGithub


class TestHelloWorld(yaz.TestCase):
    def test_010_greeting(self):
        caller = self.get_caller([ZichtGithub])
        self.assertEqual("Hello World!", caller())
        self.assertEqual("HELLO WORLD!", caller("--shout"))
        self.assertEqual("Hi there", caller("--greeting", "Hi there"))
        self.assertEqual("HI THERE", caller("--greeting", "Hi there", "--shout"))
