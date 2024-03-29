from justify import justify


class TestJustify:
    lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

    def test_thirty(self):
        assert justify(self.lorem, 30) == ["Lorem  ipsum  dolor  sit amet,", "consectetur  adipiscing  elit,", "sed    do    eiusmod    tempor", "incididunt ut labore et dolore", "magna aliqua. Ut enim ad minim", "veniam,      quis      nostrud", "exercitation  ullamco  laboris", "nisi  ut aliquip ex ea commodo",
                                           "consequat.   Duis  aute  irure", "dolor   in   reprehenderit  in", "voluptate  velit  esse  cillum", "dolore    eu    fugiat   nulla", "pariatur.    Excepteur    sint", "occaecat     cupidatat     non", "proident,  sunt  in  culpa qui", "officia  deserunt  mollit anim", "id est laborum."]

    def test_twenty(self):
        assert justify(self.lorem, 20) == ["Lorem   ipsum  dolor", "sit            amet,", "consectetur         ", "adipiscing elit, sed", "do   eiusmod  tempor", "incididunt ut labore", "et    dolore   magna", "aliqua.  Ut  enim ad", "minim  veniam,  quis", "nostrud exercitation", "ullamco laboris nisi", "ut   aliquip  ex  ea",
                                           "commodo   consequat.", "Duis    aute   irure", "dolor             in", "reprehenderit     in", "voluptate velit esse", "cillum   dolore   eu", "fugiat         nulla", "pariatur.  Excepteur", "sint        occaecat", "cupidatat        non", "proident,   sunt  in", "culpa   qui  officia", "deserunt mollit anim", "id est laborum."]
