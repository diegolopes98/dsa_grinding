class HistoryNode:
    def __init__(self, url):
        self.url = url
        self.next = None
        self.prev = None


class BrowserHistory:

    def __init__(self, homepage: str):
        self.page = HistoryNode(homepage)

    def visit(self, url: str) -> None:
        new_page = HistoryNode(url)
        new_page.prev = self.page
        self.page.next = new_page
        self.page = self.page.next

    def back(self, steps: int) -> str:
        while steps and self.page.prev:
            self.page = self.page.prev
            steps -= 1
        return self.page.url

    def forward(self, steps: int) -> str:
        while steps and self.page.next:
            self.page = self.page.next
            steps -= 1
        return self.page.url
