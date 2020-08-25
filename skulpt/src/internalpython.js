Sk.internalPy={"files": {"src/staticmethod.py": "class staticmethod(object):\n    \"Emulate PyStaticMethod_Type() in Objects/funcobject.c\"\n\n    def __init__(self, f):\n        self.f = f\n\n    def __get__(self, obj, objtype=None):\n        return self.f\n", "src/property.py": "class property(object):\n    \"Emulate PyProperty_Type() in Objects/descrobject.c\"\n\n    def __init__(self, fget=None, fset=None, fdel=None, doc=None):\n        self.fget = fget\n        self.fset = fset\n        self.fdel = fdel\n        if doc is None and fget is not None:\n            if hasattr(fget, '__doc__'):\n                doc = fget.__doc__\n            else:\n                doc = None\n        self.__doc__ = doc\n\n    def __get__(self, obj, objtype=None):\n        if obj is None:\n            return self\n        if self.fget is None:\n            raise AttributeError(\"unreadable attribute\")\n        return self.fget(obj)\n\n    def __set__(self, obj, value):\n        if self.fset is None:\n            raise AttributeError(\"can't set attribute\")\n        self.fset(obj, value)\n\n    def __delete__(self, obj):\n        if self.fdel is None:\n            raise AttributeError(\"can't delete attribute\")\n        self.fdel(obj)\n\n    def getter(self, fget):\n        return type(self)(fget, self.fset, self.fdel, self.__doc__)\n\n    def setter(self, fset):\n        return type(self)(self.fget, fset, self.fdel, self.__doc__)\n\n    def deleter(self, fdel):\n        return type(self)(self.fget, self.fset, fdel, self.__doc__)\n", "src/classmethod.py": "class classmethod(object):\n    \"Emulate PyClassMethod_Type() in Objects/funcobject.c\"\n\n    def __init__(self, f):\n        self.f = f\n\n    def __get__(self, obj, klass=None):\n        if klass is None:\n            klass = type(obj)\n        def newfunc(*args):\n            return self.f(klass, *args)\n        return newfunc\n"}};