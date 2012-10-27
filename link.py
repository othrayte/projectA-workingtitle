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

class Link(object):
    """
    A link between attributes
    """
    
    def __init__(self, debtor, onValueChanged, onBreak):
        self._debtor = debtor
        self._debtor._link(self)
        self._onValueChanged = onValueChanged
        self._onBreak = onBreak
        
    def break_(self):
        self._debtor._creditors.remove(self)
        self._onBreak()
        
    def notify(self, value):
        self._onValueChanged(value)
        
    
FLOATING, FIXED = range(2)   

class Linkable(object): 
    state = FLOATING
     
    def __init__(self):
        self._creditLinks = list()
        self._value = 0
        
    def _link(self, link):
        self._creditLinks.append(link)     
    
    def _set(self, v):
        self._value = v
        for creditor in self._creditLinks:
            creditor.notify(v)        
        
    def set(self, v):
        self._value = v
        self.fix()
        for creditor in self._creditLinks:
            creditor.notify(v)
        
    def get(self):
        return self._value
        
    def fix(self):
        self.state = FIXED
        
    def float(self):
        self.state = FLOATING
                
    def __add__(self, o):
        import mutation        
        if isinstance(o, Linkable):
            return mutation.AdditionMutation(self, o)
        else:
            return mutation.AdditionConstMutation(self, o)    
        
class SingleLinkable(Linkable):
    def __init__(self):
        Linkable.__init__(self)
        self._debtLink = None
        
    def linkTo(self, debtor):
        if self._debtLink is not None:
            self._debtLink.break_()
        self._debtLink = Link(debtor, self._incomingChange, self._linkBroken)
        self._value = debtor.get()
        self.float()      
    
    def _incomingChange(self, v):
        self._set(v)
    
    def _linkBroken(self):
        self._debtLink = None
        
    def unlink(self):
        self._debtLink.break_()
        
    def __lshift__(self, o):       
        if isinstance(o, Linkable):
            return self.linkTo(o)
        else:
            return self.set(o)        
        
        
class DoubleLinkable(Linkable):
    def __init__(self):
        Linkable.__init__(self)
        self._leftValue = 0
        self._rightValue = 0
        self._leftDebtLink = None
        self._rightDebtLink = None
        
    def linkLeftTo(self, leftDebtor):
        if self._leftDebtLink is not None:
            self._leftDebtLink.break_()
        self._leftDebtLink = Link(leftDebtor, self._leftIncomingChange, self._leftLinkBroken)
        self._leftValue = leftDebtor.get()
        self.float()   
        
    def linkRightTo(self, rightDebtor):
        if self._rightDebtLink is not None:
            self._rightDebtLink.break_()
        self._rightDebtLink = Link(rightDebtor, self._rightIncomingChange, self._rightLinkBroken)
        self._rightValue = rightDebtor.get()
        self.float()         
    
    def _combine(self, left, right):
        return left + right
    
    def _leftIncomingChange(self, v):
        self._leftValue = v
        self._set(self._combine(v, self._rightValue))
    def _rightIncomingChange(self, v):
        self._rightValue = v
        self._set(self._combine(self._leftValue, v))
    
    def _leftLinkBroken(self):
        self._leftDebtLink = None
    def _rightLinkBroken(self):
        self._rightDebtLink = None
        
    def unlinkLeft(self):
        self._leftDebtLink.break_()
    def unlinkRight(self):
        self._rightDebtLink.break_()
        
class ArrayLinkable(Linkable):    
    pass