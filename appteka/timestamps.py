# appteka - helpers collection

# Copyright (C) 2018 Aleksandr Popov

# This program is free software: you can redistribute it and/or modify
# it under the terms of the Lesser GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# Lesser GNU General Public License for more details.

# You should have received a copy of the Lesser GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import time

def get_time(secs, scale="s"):
    """ 
    Return time from timestamp. 

    Parameters
    ----------
    secs : float
        Seconds since the epoch.
    scale : str 
        Scale. Possible values: "ms" (milliseconds), "s" (seconds), "m" (minutes), "h" (hours).

    Returns
    -------
    label : str
        String label representing the time.
        
    """
    t = time.gmtime(secs)
    if   scale == "s":
        return time.strftime("%H:%M:%S", t)
    elif scale == "m":
        return time.strftime("%H:%M", t) 
    elif scale == "h":
        return time.strftime("%H", t)
    elif scale == "ms":
        ms = int(1000*(secs - int(secs)))
        return time.strftime("%H:%M:%S", secs) + ".{}".format(ms)
    
def get_date(secs):
    """ 
    Return date from timestamp. 

    Parameters
    ----------
    secs : float
        Seconds since the epoch.

    Returns
    -------
    Returns
    -------
    label : str
        String label representing the date.
    
    """
    t = time.gmtime(secs)
    return time.strftime("%y-%m-%d", t)
