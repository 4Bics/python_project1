import unittest
from models.member import Member

class TestMember(unittest.TestCase):
  def setUp(self):
    self.member = Member("Cameron", 25, "Gold")

#Test member has name
  def test_member_has_name(self):
    self.assertEqual("Cameron", self.member.name)

#Test member has age
  def test_member_has_age(self):
    self.assertEqual(25, self.member.age)

#Test member has membership type
  def test_member_has_membership_type(self):
    self.assertEqual("Gold", self.member.membership_type)

#Test member has class credits
  def test_member_has_class_credits(self):
    self.assertEqual(0, self.member.class_credits)