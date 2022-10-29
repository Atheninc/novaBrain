import sys

sys.path.append("../../../lib")

import nova
import os

txt = sys.argv[1]
print(txt)

eval(txt)