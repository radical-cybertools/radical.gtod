#!/usr/bin/env python

__author__    = 'Radical Development Team'
__email__     = 'radical@radical-project.org'
__copyright__ = 'Copyright date +%Y, RADICAL@Rutgers'
__license__   = 'MIT'


import os
import time
import radical.utils as ru
import radical.gtod  as rg


# ------------------------------------------------------------------------------
def test_gtod():
    '''
    test
    '''

    out, _, _ = ru.shell_callout('radical.gtod')
    t1 = fload(out)
    t2 = rg.gtod()
    t3 = time.time()

    assert(t3 - 0.1 < t1 < t3 + 0.1)
    assert(t3 - 0.1 < t2 < t3 + 0.1)


# ------------------------------------------------------------------------------
#
if __name__ == '__main__':

    test_gtod()


# ------------------------------------------------------------------------------

