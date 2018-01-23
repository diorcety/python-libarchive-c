# Source: https://github.com/Changaco/version.py

from os.path import dirname, isdir, join
import re
from subprocess import CalledProcessError, check_output


PREFIX = ''

tag_re = re.compile(r'\btag: %s([0-9][^,]*)\b' % PREFIX)
version_re = re.compile('^Version: (.+)$', re.M)


def get_version():
    # Return the version if it has been injected into the file by git-archive
    version = tag_re.search('$Format:%D$')
    if version:
        return version.group(1)

    d = dirname(__file__)

    # Extract the version from the PKG-INFO file.
    with open(join(d, 'PKG-INFO')) as f:
        version = version_re.search(f.read()).group(1)

    return version


if __name__ == '__main__':
    print(get_version())
