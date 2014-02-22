# -*- coding: utf-8 -*-

# This file is part of PyBOSSA.
#
# PyBOSSA is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PyBOSSA is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with PyBOSSA.  If not, see <http://www.gnu.org/licenses/>.

import json


def get_iss_photos(start, n_photos, mission, size="small"):
    """
    Gets public photos from ISS missions
    :arg string size: Size of the image from ISS mission
    :returns: A list of photos.
    :rtype: list
    """
    photos = []
    for i in range(start, start + n_photos):
        pattern_s = "http://eol.jsc.nasa.gov/sseop/images/ESC/%s/%s/%s-E-%s.JPG" % (
            size,
            mission,
            mission,
            i)
        pattern_b = "http://eol.jsc.nasa.gov/sseop/images/ESC/%s/%s/%s-E-%s.JPG" % (
            'large',
            mission,
            mission,
            i)

        tmp = dict(link_small=pattern_s,
                   link_big=pattern_b
                   )

        photos.append(tmp)
    return photos
