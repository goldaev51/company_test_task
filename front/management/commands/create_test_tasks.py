import random
from datetime import datetime

from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from faker import Faker

from front.models import Task


class Command(BaseCommand):
    help = 'Create specified number of test tasks'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of tasks to be created')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        fake = Faker()

        if total < 1:
            raise CommandError('Total number of tasks should be greater than 0')

        tasks = []
        for i in range(total):
            due_date = fake.date_between(start_date='today', end_date='+30d')
            title = fake.sentence(nb_words=6, variable_nb_words=True).strip("('")
            description = fake.text(max_nb_chars=200).strip("',)")
            status = random.choice([True, False])
            task = Task(title=title,
                        description=description,
                        due_date=due_date,
                        status=status)
            tasks.append(task)

        Task.objects.bulk_create(tasks)
        self.stdout.write(self.style.SUCCESS(f'Created {total} tasks'))
