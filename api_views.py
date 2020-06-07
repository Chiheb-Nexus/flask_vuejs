#
# APIs for the APP
#

from random import randint
from flask import jsonify
from flask.views import MethodView


class APIFirstExample(MethodView):
    def get(self):
        """Return List of dicts"""
        return jsonify([
            dict([
                ('name', f'Person{k}'),
                ('age', randint(10, 100)),
                ('exam1', randint(0, 20)),
                ('exam2', randint(0, 20)),
                ('exam3', randint(0, 20)),
                ('exam4', randint(0, 20))
            ]) for k in range(500)
        ])


class APISecondExample(MethodView):
    def get(self):
        """Return list of dicts"""
        return jsonify([
            dict([
                ('name', f'Sound{randint(0, 100)}'),
                ('track', f'Track{randint(0, 100)}'),
                ('artist', f'Artist{randint(0, 100)}'),
                ('album', f'Album{randint(0, 100)}')
            ]) for _ in range(500)
        ])
