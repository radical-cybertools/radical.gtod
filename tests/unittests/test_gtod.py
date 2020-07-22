#!/usr/bin/env python

__author__	  = 'RADICAL-Cybertools Team'
__email__	  = 'info@radical-cybertools.org'
__copyright__ = 'Copyright 2020, The RADICAL-Cybertools Team'
__license__   = 'MIT'

import time
import radical.utils as ru
import radical.gtod  as rg


# ------------------------------------------------------------------------------
def test_gtod():
    '''
    test
    '''

    out, _, _ = ru.sh_callout('radical-gtod')
    t1 = float(out)
    t2 = rg.gtod()
    t3 = time.time()

    assert(t3 - 0.1 < t1 < t3 + 0.1)
    assert(t3 - 0.1 < t2 < t3 + 0.1)


# ------------------------------------------------------------------------------
#
if __name__ == '__main__':

    test_gtod()


# ------------------------------------------------------------------------------

