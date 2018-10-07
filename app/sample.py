class Thing(object):
    def increment(self, x):
        if isinstance(x, int):
            return x + 1
        raise ValueError
