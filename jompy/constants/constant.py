class Constant(object):
    def __init__(self, name, value, system, unit, unit_base=None, others=None):
        self._name = name
        self._value = value
        self._system = system
        self._unit = unit
        self._unit_base = unit_base
        self._others = others

        self._check_system()

    def _check_system(self):
        _systems = ['si', 'cgs']
        if not self._system in _systems:
            raise TypeError('specified system is not valid, system: {0}. '
                            'systems: {}'.format(self._system, _systems))

    def __repr__(self):
        pass

    def __str__(self):
        """ table """
        pass

    @property
    def name(self):
        return self._name

    @property
    def value(self):
        return self._value

    @property
    def unit(self):
        return self._unit

    @property
    def unit_base(self):
        """ units as base units """
        return self._unit_base