import unittest
from data_structures.browser_history.browser_history import BrowserHistory


class TestBrowserHistory(unittest.TestCase):
    def test_initialization(self):
        """Test browser history initialization with homepage"""
        bh = BrowserHistory("leetcode.com")
        self.assertEqual(bh.page.url, "leetcode.com")
        self.assertIsNone(bh.page.prev)
        self.assertIsNone(bh.page.next)

    def test_single_visit(self):
        """Test visiting a single page"""
        bh = BrowserHistory("leetcode.com")
        bh.visit("google.com")
        self.assertEqual(bh.page.url, "google.com")
        self.assertEqual(bh.page.prev.url, "leetcode.com")
        self.assertIsNone(bh.page.next)

    def test_multiple_visits(self):
        """Test visiting multiple pages in sequence"""
        bh = BrowserHistory("leetcode.com")
        bh.visit("google.com")
        bh.visit("facebook.com")
        bh.visit("youtube.com")

        # Should be on youtube.com
        self.assertEqual(bh.page.url, "youtube.com")
        # Should be able to trace back
        self.assertEqual(bh.page.prev.url, "facebook.com")
        self.assertEqual(bh.page.prev.prev.url, "google.com")
        self.assertEqual(bh.page.prev.prev.prev.url, "leetcode.com")

    def test_back_single_step(self):
        """Test going back one step"""
        bh = BrowserHistory("leetcode.com")
        bh.visit("google.com")
        bh.visit("facebook.com")

        result = bh.back(1)
        self.assertEqual(result, "google.com")
        self.assertEqual(bh.page.url, "google.com")

    def test_back_multiple_steps(self):
        """Test going back multiple steps"""
        bh = BrowserHistory("leetcode.com")
        bh.visit("google.com")
        bh.visit("facebook.com")
        bh.visit("youtube.com")

        result = bh.back(2)
        self.assertEqual(result, "google.com")
        self.assertEqual(bh.page.url, "google.com")

    def test_back_to_homepage(self):
        """Test going back to homepage"""
        bh = BrowserHistory("leetcode.com")
        bh.visit("google.com")
        bh.visit("facebook.com")

        result = bh.back(2)
        self.assertEqual(result, "leetcode.com")
        self.assertEqual(bh.page.url, "leetcode.com")

    def test_back_beyond_homepage(self):
        """Test trying to go back beyond homepage"""
        bh = BrowserHistory("leetcode.com")
        bh.visit("google.com")

        result = bh.back(5)  # More steps than available
        self.assertEqual(result, "leetcode.com")
        self.assertEqual(bh.page.url, "leetcode.com")

    def test_back_from_homepage(self):
        """Test going back from homepage (should stay at homepage)"""
        bh = BrowserHistory("leetcode.com")

        result = bh.back(1)
        self.assertEqual(result, "leetcode.com")
        self.assertEqual(bh.page.url, "leetcode.com")

    def test_forward_single_step(self):
        """Test going forward one step"""
        bh = BrowserHistory("leetcode.com")
        bh.visit("google.com")
        bh.visit("facebook.com")
        bh.back(1)  # Now at google.com

        result = bh.forward(1)
        self.assertEqual(result, "facebook.com")
        self.assertEqual(bh.page.url, "facebook.com")

    def test_forward_multiple_steps(self):
        """Test going forward multiple steps"""
        bh = BrowserHistory("leetcode.com")
        bh.visit("google.com")
        bh.visit("facebook.com")
        bh.visit("youtube.com")
        bh.back(3)  # Now at leetcode.com

        result = bh.forward(2)
        self.assertEqual(result, "facebook.com")
        self.assertEqual(bh.page.url, "facebook.com")

    def test_forward_to_latest(self):
        """Test going forward to latest page"""
        bh = BrowserHistory("leetcode.com")
        bh.visit("google.com")
        bh.visit("facebook.com")
        bh.back(2)  # Now at leetcode.com

        result = bh.forward(2)
        self.assertEqual(result, "facebook.com")
        self.assertEqual(bh.page.url, "facebook.com")

    def test_forward_beyond_latest(self):
        """Test trying to go forward beyond latest page"""
        bh = BrowserHistory("leetcode.com")
        bh.visit("google.com")
        bh.back(1)  # Now at leetcode.com

        result = bh.forward(5)  # More steps than available
        self.assertEqual(result, "google.com")
        self.assertEqual(bh.page.url, "google.com")

    def test_forward_without_history(self):
        """Test going forward when there's no forward history"""
        bh = BrowserHistory("leetcode.com")
        bh.visit("google.com")

        result = bh.forward(1)
        self.assertEqual(result, "google.com")
        self.assertEqual(bh.page.url, "google.com")

    def test_visit_clears_forward_history(self):
        """Test that visiting a new page clears forward history"""
        bh = BrowserHistory("leetcode.com")
        bh.visit("google.com")
        bh.visit("facebook.com")
        bh.back(1)  # Now at google.com

        # Visit new page should clear forward history
        bh.visit("twitter.com")
        self.assertEqual(bh.page.url, "twitter.com")

        # Should not be able to go forward to facebook.com anymore
        result = bh.forward(1)
        self.assertEqual(result, "twitter.com")
        self.assertEqual(bh.page.url, "twitter.com")

    def test_complex_navigation_sequence(self):
        """Test complex sequence of operations"""
        bh = BrowserHistory("leetcode.com")

        # Visit pages: leetcode.com -> google.com -> facebook.com -> youtube.com
        bh.visit("google.com")
        bh.visit("facebook.com")
        bh.visit("youtube.com")

        # Go back 1: youtube.com -> facebook.com
        result = bh.back(1)
        self.assertEqual(result, "facebook.com")

        # Go back 1: facebook.com -> google.com
        result = bh.back(1)
        self.assertEqual(result, "google.com")

        # Go forward 1: google.com -> facebook.com
        result = bh.forward(1)
        self.assertEqual(result, "facebook.com")

        # Visit new page (should clear youtube.com from forward history)
        bh.visit("linkedin.com")
        self.assertEqual(bh.page.url, "linkedin.com")

        # Go back 1: linkedin.com -> facebook.com
        result = bh.back(1)
        self.assertEqual(result, "facebook.com")

        # Forward should only go to linkedin.com, not youtube.com
        result = bh.forward(1)
        self.assertEqual(result, "linkedin.com")

    def test_back_and_forward_zero_steps(self):
        """Test back and forward with zero steps"""
        bh = BrowserHistory("leetcode.com")
        bh.visit("google.com")

        result = bh.back(0)
        self.assertEqual(result, "google.com")

        result = bh.forward(0)
        self.assertEqual(result, "google.com")

    def test_leetcode_example(self):
        """Test the example from LeetCode problem description"""
        bh = BrowserHistory("leetcode.com")
        bh.visit("google.com")
        bh.visit("facebook.com")
        bh.visit("youtube.com")

        result = bh.back(1)
        self.assertEqual(result, "facebook.com")

        result = bh.back(1)
        self.assertEqual(result, "google.com")

        result = bh.forward(1)
        self.assertEqual(result, "facebook.com")

        bh.visit("linkedin.com")

        result = bh.forward(2)
        self.assertEqual(result, "linkedin.com")

        result = bh.back(2)
        self.assertEqual(result, "google.com")

        result = bh.back(7)
        self.assertEqual(result, "leetcode.com")


if __name__ == "__main__":
    unittest.main()