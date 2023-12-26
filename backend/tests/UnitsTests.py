from typing import Self
import unittest
from controllers import get_all_alumni_ctr

class Funit(unittest.TestCase):
    result = get_all_alumni_ctr()
    result == str