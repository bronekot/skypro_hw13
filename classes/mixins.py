class mixinRepr(object):
    def __repr__(self):
        values = ', '.join(str(value) for value in self.__dict__.values())
        return f"{self.__class__.__name__}({values})"
