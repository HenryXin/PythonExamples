import weakref
import tempfile, shutil
from pathlib import Path

class TempDir:
    def __init__(self):
        self.name = tempfile.mkdtemp()
        self._finalizer = weakref.finalize(self, shutil.rmtree, self.name)

    def __repr__(self):
        return "TempDir({!r:})".format(self.name)

    def remove(self):
        self._finializer()

    @property
    def removed(self):
        return not self._finalizer.alive

tmp = TempDir()
print(tmp)
print(tmp.removed)
print(Path(tmp.name).is_dir())
