import unittest

from code_ca4 import read_file, get_commits, get_changedPaths

class TestCommits(unittest.TestCase):

    def setUp(self):
        self.data = read_file('changes_file.txt')

    def test_number_of_lines(self):
        self.assertEqual(5255, len(self.data))

    def test_number_of_commits(self):
        commits = get_commits(self.data)
        self.assertEqual(422, len(commits))

    def test_first_commit(self):
        commits = get_commits(self.data)
        self.assertEqual('r1551925', commits[0]['r'])
        self.assertEqual('Thomas', commits[0]['name'])
        self.assertEqual('2015-11-27', commits[0]['date'])
        self.assertEqual('16:57:44', commits[0]['time'])
        self.assertEqual('1', commits[0]['num_line'])

    def test_first_changedPath(self):
        changedPaths = get_changedPaths(self.data)
        self.assertEqual('A', changedPaths[0]['changedPathsType'])

if __name__ == '__main__':
    unittest.main()
