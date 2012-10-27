"""
    Projcet A (Working title)

    Website     : github.com/othrayte/projectA-workingtitle
    Initial idea: Adrian Cowan (othrayte) - othrayte@gmail.com
    Project Contributors:
        Adrian Cowan (othrayte) - othrayte@gmail.com

    Copyright 2012, Adrian Cowan (othrayte) & listed contributors

    This file is part of ProjectA.

    ProjectA is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    ProjectAis distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with ProjectA.  If not, see <http://www.gnu.org/licenses/>.
"""

import link

class DirectMutation(link.SingleLinkable):
    """
    A mutation of attributes
    """

class CombiningMutation(link.DoubleLinkable):
    """
    A mutation of attributes
    """

class ArrayMutation(link.ArrayLinkable):
    """
    A mutation of attributes
    """

class AdditionConstMutation(DirectMutation):
    """
    An addition mutation with a constant value
    """
    
    def __init__(self, attr, const):
        DirectMutation.__init__(self)
        self.attr = attr
        self.const = const
        
        self.linkTo(attr)
        
    def _incomingChange(self, v):
        self._set(v+self.const)
        
class AdditionMutation(CombiningMutation):
    """
    An addition mutation
    """
    
    def __init__(self, left, right):
        CombiningMutation.__init__(self)
        self.left = left
        self.right = left
        
        self.linkLeftTo(left)
        self.linkRightTo(right)    

    def _combine(self, left, right):
        return left + right   