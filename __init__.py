from os.path import dirname, basename, isfile
import glob
modules = glob.iglob(dirname(__file__)+"/*.py", recursive=True)
__all__ = [ basename(f)[:-3] for f in modules if isfile(f)]
