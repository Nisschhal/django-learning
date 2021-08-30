import os
import django
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings', )

django.setup()

from first_app.models import Topic, WebPage, AccessRecord
from faker import Faker

fak_gen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']


def add_topic():
	t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
	t.save()
	return t


def populate(n=5):
	for entry in range(n):
		top = add_topic()

		fake_url = fak_gen.url()
		fake_date = fak_gen.date()
		fake_web_page_name = fak_gen.company()

		web_page = WebPage.objects.get_or_create(topic=top, url=fake_url, web_page_name=fake_web_page_name)[0]

		acc_rec = AccessRecord.objects.get_or_create(web_page_name=web_page, date=fake_date)[0]


if __name__ == '__main__':
	print('populating script!!')
	populate(20)
	print('populate completed!!')
