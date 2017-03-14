from __future__ import print_function
from __future__ import unicode_literals

import random


if __name__ == '__main__':
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
    print(''.join(random.choice(chars) for i in range(50)))
