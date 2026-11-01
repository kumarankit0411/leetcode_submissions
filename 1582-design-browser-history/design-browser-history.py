class BrowserHistory:

    def __init__(self, homepage: str):
        self.ls = []
        self.rs = []

        self.ls.append(homepage)

    def visit(self, url: str) -> None:
        self.ls.append(url)
        self.rs.clear()

    def back(self, steps: int) -> str:
        back = min(steps, len(self.ls)-1)

        while back > 0:
            url = self.ls.pop()
            self.rs.append(url)
            back-=1
        
        return self.ls[-1]


    def forward(self, steps: int) -> str:
        forward = min(steps, len(self.rs))
        
        while forward > 0:
            url = self.rs.pop()
            self.ls.append(url)
            forward-=1

        return self.ls[-1]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)