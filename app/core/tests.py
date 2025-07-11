
from django.test import SimpleTestCase
from unittest.mock import patch
from django.core.management import call_command
from psycopg2 import OperationalError as Psycopg2OPsycopgError
from django.db.utils import OperationalError

@patch('django.db.utils.ConnectionHandler.__getitem__')
class CommandsTests(SimpleTestCase):
    #wait_for_db 명령어가 DB가 준비되었을 떄 잘 동작하는지 체크하는 함수
    def test_wait_for_db_ready(self, patched_getitem):
        patched_getitem.return_value = True
        call_command('wait_for_db')
        self.assertEqual(patched_getitem.call_count, 1)



    @patch('time.sleep')
    def test_wait_for_db_delay(self, patched_sleep, patched_getitem):
        patched_getitem.side_effect = [Psycopg2OPsycopgError] + \
            [OperationalError] * 5 + [True]
        call_command('wait_for_db')

        self.assertEqual(patched_getitem.call_count, 7)

# test실행 명령어
# docker-compose run --rm app sh -c 'python manage.py test core'
