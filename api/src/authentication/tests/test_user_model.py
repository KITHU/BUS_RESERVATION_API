from .base_test import BaseTest
from api.src.authentication.models import User


class authentecationTestCase(BaseTest):

    def test_models_can_create_user(self):
        old_count = User.objects.count()
        User(**self.new_user).save()
        new_count = User.objects.count()
        self.assertEqual(new_count, old_count + 1)
