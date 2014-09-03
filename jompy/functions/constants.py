""" Jompy Constant class"""


class Constant(object):
    def __init__(self, name, value, unit, system):
        self._name = name
        self._value = value
        self._unit = unit
        self._system = system

    def _check_system(self):
        _systems = ['si', 'cgs']
        if not self._system in _systems:
            raise TypeError('specified system is not valid, system: {0}. '
                            'systems: {}'.format(self._system, _systems))


