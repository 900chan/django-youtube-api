from django.test import TestCase
from django.contrib.auth import get_user_model

# TDD : Test Driven Development (테스트 주도 개발)

class UserTestCase(TestCase):

    # 일반 유저 생성 테스트 함수
    def test_create_user(self):
        email = 'absbrb@naver.com'
        password = 'password123'

        user = get_user_model().objects.create_user(email=email, password=password)
        # 유저가 정상적으로 만들어졌는지 체크
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
        self.assertFalse(user.is_superuser)


    # 슈퍼 유저 생성 테스트 함수
    def test_create_superuser(self):
        email = 'absbrb_super@naver.com'
        password = 'password123'

        user = get_user_model().objects.create_superuser(
            email=email,
            password=password
        )

        # 슈퍼유저
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)