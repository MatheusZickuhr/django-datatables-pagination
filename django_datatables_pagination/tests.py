from django.test import TestCase
from django_datatables_pagination.views import split_html_by_tds


class ViewFunctionsTests(TestCase):

    def test_split_html_by_tds1(self):
        html = """
            <td>some data1</td>
            <td>some data2</td>
        """
        expected = ['some data1', 'some data2']
        actual = split_html_by_tds(html)
        self.assertEquals(actual, expected)

    def test_split_html_by_tds2(self):
        html = """
            <td>some data1</td>
            <td></td>
            <td>some data2</td>
        """
        expected = ['some data1', '', 'some data2']
        actual = split_html_by_tds(html)
        self.assertEquals(actual, expected)

    def test_split_html_by_tds3(self):
        html = """
            <td>some data1</td>
            <td><div>some data2</div><img/><span>aaaaaaa</span></td>
        """
        expected = ['some data1', '<div>some data2</div><img/><span>aaaaaaa</span>']
        actual = split_html_by_tds(html)
        self.assertEquals(actual, expected)

    def test_split_html_by_tds4(self):
        html = """
              <td class="aaa">some data1</td>
              <td class="a-class" id="some-id"><div>some data2</div><img/><span>aaaaaaa</span></td>
          """
        expected = ['some data1', '<div>some data2</div><img/><span>aaaaaaa</span>']
        actual = split_html_by_tds(html)
        self.assertEquals(actual, expected)
