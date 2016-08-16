import os
import yaml

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        for fn in ['schedule.yml', 'open-day-schedule.yml']:
            with open(fn) as f:
                schedule = yaml.load(f.read())

            for date in schedule:
                print(date)
                for room in schedule[date]:
                    print('  {}'.format(room))
                    for time in schedule[date][room]:
                        print('    {}'.format(time))
                        if schedule[date][room][time]:
                            session = schedule[date][room][time]
                            print('      {}'.format(session))

                            fields = {
                                'date': date,
                                'time': time,
                                'room': room,
                            }

                            if session[:6] == 'talks/':
                                fields['session'] = session
                            else:
                                fields['title'] = session

                            dir_path = os.path.join('schedule', date, room)
                            os.makedirs(dir_path, exist_ok=True)
                            with open(os.path.join(dir_path, time), 'w') as f:
                                f.write(yaml.dump(fields, default_flow_style=False))

