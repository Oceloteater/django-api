"""
Django command to wait for the db
"""
import time

from psycopg2 import OperationalError as Psycopg2Error

from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
	"""Django command to wait for db"""

	def handle(self, *args, **options):
		self.stdout.write('Waiting for db...')
		db_up = False
		while db_up is False:
			try:
				self.check(databases=['default'])
				db_up = True
			except (Psycopg2Error, OperationalError):
				self.stdout.write('Db unavailable, waiting 1 sec...')
				time.sleep(1)

		self.stdout.write(self.style.SUCCESS('Success! Connection made with db.'))
