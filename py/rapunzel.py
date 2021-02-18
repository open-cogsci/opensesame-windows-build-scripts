#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""
This file is part of OpenSesame.

OpenSesame is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

OpenSesame is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with OpenSesame.  If not, see <http://www.gnu.org/licenses/>.
"""


def rapunzel():

    # A Hack for Python 3.8 on Windows. However, if asyncio is not available
    # then this is not crucial.
    try:
        import asyncio
        asyncio.set_event_loop_policy(
            asyncio.WindowsSelectorEventLoopPolicy()
        )
    except ImportError:
        pass
    import sys
    sys.argv.append(u'--mode=ide')
    from libqtopensesame import __main__
    __main__.opensesame()


# checking if __name__ is __main__ is required to let multiprocessing correctly
# work on Windows (or any other platform that is not able to use os.fork)
if __name__ == "__main__":

    rapunzel()
