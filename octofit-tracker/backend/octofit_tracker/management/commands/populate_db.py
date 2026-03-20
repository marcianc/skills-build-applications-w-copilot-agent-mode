from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from octofit_tracker.models import Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        self.stdout.write(self.style.WARNING('Deleting old data...'))
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        self.stdout.write(self.style.SUCCESS('Creating teams...'))
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        self.stdout.write(self.style.SUCCESS('Creating users...'))
        ironman = User.objects.create_user(username='ironman', email='ironman@marvel.com', team=marvel)
        captain = User.objects.create_user(username='captain', email='captain@marvel.com', team=marvel)
        batman = User.objects.create_user(username='batman', email='batman@dc.com', team=dc)
        superman = User.objects.create_user(username='superman', email='superman@dc.com', team=dc)

        self.stdout.write(self.style.SUCCESS('Creating activities...'))
        Activity.objects.create(user=ironman, type='run', duration=30)
        Activity.objects.create(user=batman, type='cycle', duration=45)
        Activity.objects.create(user=superman, type='swim', duration=60)
        Activity.objects.create(user=captain, type='walk', duration=20)

        self.stdout.write(self.style.SUCCESS('Creating workouts...'))
        Workout.objects.create(name='Hero HIIT', description='High intensity for heroes')
        Workout.objects.create(name='Power Yoga', description='Flexibility for super strength')

        self.stdout.write(self.style.SUCCESS('Creating leaderboard...'))
        Leaderboard.objects.create(user=ironman, points=100)
        Leaderboard.objects.create(user=batman, points=90)
        Leaderboard.objects.create(user=superman, points=80)
        Leaderboard.objects.create(user=captain, points=70)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully!'))
