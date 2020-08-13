from boofuzz import s_get, s_group, s_initialize, Session, Target, UDPSocketConnection
from seleniumbase import BaseCase

class MyTestClass(BaseCase):
    def test_foo_bar(self):
        session = Session(
            target=Target(
                connection=UDPSocketConnection(
                    recv_timeout=1,
                    host="172.26.87.144", 
                    port=6234, 
                    bind=("0.0.0.0", 12345),),
            ),
            keep_web_open=False
        )

        s_initialize("foo")
        s_group("version", values=["\x06"]) 

        session.connect(s_get("foo"))
        session.fuzz()

        self.open("http://localhost:26000")
        self.assert_text("boofuzz Fuzz Control", "div.main-title")
        self.assert_text("fail", "div.main-title")

    # def test_basic(self):
    #     pass
        # self.open("https://store.xkcd.com/search")
        # self.type('input[name="q"]', "xkcd book\n")
        # self.assert_text("xkcd book", "div.results")
        # self.open("https://xkcd.com/353/")
        # self.click('a[rel="license"]')
        # self.go_back()
        # self.click_link_text("About")
        # self.click_link_text("comic #249")
        # self.assert_element('img[alt*="Chess"]')

