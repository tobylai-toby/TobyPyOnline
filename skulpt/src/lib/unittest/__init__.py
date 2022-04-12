__author__ = 'bmiller'
'''
This is the start of something that behaves like
the unittest module from cpython.

'''

class TestCase:
    def __init__(self):
        self.numPassed = 0
        self.numFailed = 0
        self.assertPassed = 0
        self.assertFailed = 0
        self.verbosity = 1
        self.tlist = []
        testNames = {}
        for name in dir(self):
            if name[:4] == 'test' and name not in testNames:
                self.tlist.append(getattr(self,name))
                testNames[name]=True

    def setUp(self):
        pass

    def tearDown(self):
        pass
    
    def cleanName(self,funcName):
    # work around skulpts lack of an __name__
        funcName = str(funcName)
        funcName = funcName[13:]
        funcName = funcName[:funcName.find('<')-3]
        return funcName

    def main(self):

        for func in self.tlist:
            if self.verbosity > 1:
                print(f'Running {self.cleanName(func)}')
            try:
                self.setUp()
                self.assertPassed = 0
                self.assertFailed = 0
                func()
                self.tearDown()
                if self.assertFailed == 0:
                    self.numPassed += 1
                else:
                    self.numFailed += 1
                    print(f'Tests failed in {self.cleanName(func)} ')
            except Exception as e:
                self.assertFailed += 1
                self.numFailed += 1
                print(f'Test threw exception in {self.cleanName(func)} ({e})')
        self.showSummary()

    def assertEqual(self, actual, expected, feedback=""):
        res = actual==expected
        if not res and feedback == "":
            feedback = f"Expected {str(actual)} to equal {str(expected)}"
        self.appendResult(res, actual ,expected, feedback)

    def assertNotEqual(self, actual, expected, feedback=""):
        res = actual != expected
        if not res and feedback == "":
            feedback = f"Expected {str(actual)} to not equal {str(expected)}"
        self.appendResult(res, actual, expected, feedback)

    def assertTrue(self,x, feedback=""):
        res = bool(x)
        if not res and feedback == "":
            feedback = f"Expected {str(x)} to be True"
        self.appendResult(res, x, True, feedback)

    def assertFalse(self,x, feedback=""):
        res = not bool(x)
        if not res and feedback == "":
            feedback = f"Expected {str(x)} to be False"
        self.appendResult(res, x, False, feedback)

    def assertIs(self,a,b, feedback=""):
        res = a is b
        if not res and feedback == "":
            feedback = f"Expected {str(a)} to be the same object as {str(b)}"
        self.appendResult(res, a, b, feedback)

    def assertIsNot(self,a,b, feedback=""):
        res = a is not b
        if not res and feedback == "":
            feedback = f"Expected {str(a)} to not be the same object as {str(b)}"
        self.appendResult(res, a, b, feedback)

    def assertIsNone(self,x, feedback=""):
        res = x is None
        if not res and feedback == "":
            feedback = f"Expected {str(x)} to be None"
        self.appendResult(res, x, None, feedback)

    def assertIsNotNone(self,x, feedback=""):
        res = x is not None
        if not res and feedback == "":
            feedback = f"Expected {str(x)} to not be None"
        self.appendResult(res, x, None, feedback)

    def assertIn(self, a, b, feedback=""):
        res = a in b
        if not res and feedback == "":
            feedback = f"Expected {str(a)} to be in {str(b)}"
        self.appendResult(res, a, b, feedback)

    def assertNotIn(self, a, b, feedback=""):
        res = a not in b
        if not res and feedback == "":
            feedback = f"Expected {str(a)} to not be in {str(b)}"
        self.appendResult(res, a, b, feedback)

    def assertIsInstance(self,a,b, feedback=""):
        res = isinstance(a,b)
        if not res and feedback == "":
            feedback = f"Expected {str(a)} to be an instance of {str(b)}"
        self.appendResult(res, a, b, feedback)

    def assertNotIsInstance(self,a,b, feedback=""):
        res = not isinstance(a,b)
        if not res and feedback == "":
            feedback = f"Expected {str(a)} to not be an instance of {str(b)}"
        self.appendResult(res, a, b, feedback)

    def assertAlmostEqual(self, a, b, places=7, feedback="", delta=None):

        if delta is not None:
            res = abs(a-b) <= delta
        else:
            if places is None:
                places = 7
            res = round(a-b, places) == 0

        if not res and feedback == "":
            feedback = f"Expected {str(a)} to equal {str(b)}"
        self.appendResult(res, a, b, feedback)

    def assertNotAlmostEqual(self, a, b, places=7, feedback="", delta=None):

        if delta is not None:
            res = a != b and abs(a - b) > delta
        else:
            if places is None:
                places = 7

            res = round(a-b, places) != 0

        if not res and feedback == "":
            feedback = f"Expected {str(a)} to not equal {str(b)}"
        self.appendResult(res, a, b, feedback)

    def assertGreater(self,a,b, feedback=""):
        res = a > b
        if not res and feedback == "":
            feedback = f"Expected {str(a)} to be greater than {str(b)}"
        self.appendResult(res, a, b, feedback)

    def assertGreaterEqual(self,a,b, feedback=""):
        res = a >= b
        if not res and feedback == "":
            feedback = f"Expected {str(a)} to be >= {str(b)}"
        self.appendResult(res, a, b, feedback)

    def assertLess(self, a, b, feedback=""):
        res = a < b
        if not res and feedback == "":
            feedback = f"Expected {str(a)} to be less than {str(b)}"
        self.appendResult(res, a, b, feedback)

    def assertLessEqual(self,a,b, feedback=""):
        res = a <= b
        if not res and feedback == "":
            feedback = f"Expected {str(a)} to be <= {str(b)}"
        self.appendResult(res, a, b, feedback)

    def appendResult(self,res,actual,expected,feedback):
        if res:
            msg = 'Pass'
            self.assertPassed += 1
        else:
            msg = f'Fail: {feedback}'
            print(msg)
            self.assertFailed += 1

    def assertRaises(self, exception, callable=None, *args, **kwds):
        # with is currently not supported hence we just try and catch
        if callable is None:
            raise NotImplementedError("assertRaises does currently not support assert contexts")
        if kwds:
            raise NotImplementedError("assertRaises does currently not support **kwds")

        res = False
        actualerror = str(exception())
        try:
            callable(*args)
        except exception as ex:
            res = True
        except Exception as inst:
            actualerror = str(inst)
            print("ACT = ", actualerror, exception())
        else:
            actualerror = "No Error"

        self.appendResult(res, str(exception()), actualerror, "")

    def fail(self, msg=None):
        msg = 'Fail' if msg is None else f'Fail: {msg}'
        print(msg)
        self.assertFailed += 1

    def showSummary(self):
        pct = self.numPassed / (self.numPassed+self.numFailed) * 100
        print("Ran %d tests, passed: %d failed: %d\n" % (self.numPassed+self.numFailed,
                                               self.numPassed, self.numFailed))



def main(verbosity=1):
    glob = globals() # globals() still needs work
    for name in glob:
        if type(glob[name]) == type and issubclass(glob[name], TestCase):
            try:
                tc = glob[name]()
                tc.verbosity = verbosity
                tc.main()
            except:
                print("Uncaught Error in: ", name)
