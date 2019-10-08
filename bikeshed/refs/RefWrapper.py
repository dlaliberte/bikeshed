# -*- coding: utf-8 -*-
from __future__ import division, unicode_literals

import copy

from .utils import stripLineBreaks
from .. import attr

@attr.s(slots=True)
class RefWrapper(object):
    # Refs don't contain their own name, so I don't have to copy as much when there are multiple linkTexts
    # This wraps that, producing an object that looks like it has a text property.
    # It also makes all the ref dict keys look like object attributes.

    text = attr.ib()
    _ref = attr.ib()
    el   = attr.ib(default=None)

    @property
    def type(self):
        return self._ref['type'].strip()
    @property
    def spec(self):
        return self._ref['spec'].strip()
    @property
    def shortname(self):
        return self._ref['shortname'].strip()
    @property
    def level(self):
        return self._ref['level'].strip()
    @property
    def status(self):
        return self._ref['status'].strip()
    @property
    def url(self):
        return self._ref['url'].strip()
    @property
    def export(self):
        return self._ref['export']
    @property
    def normative(self):
        return self._ref['normative']
    @property
    def for_(self):
        return [x.strip() for x in self._ref['for']]
    '''
        "type": linesIter.next(),
        "spec": linesIter.next(),
        "shortname": linesIter.next(),
        "level": linesIter.next(),
        "status": linesIter.next(),
        "url": linesIter.next(),
        "export": linesIter.next() != "\n",
        "normative": linesIter.next() != "\n",
        "for": []
    '''

    def __json__(self):
        refCopy = copy.copy(self._ref)
        refCopy['text'] = self.text
        return stripLineBreaks(refCopy)

def decode(s):
    if isinstance(s, str):
        return unicode(s, encoding="utf-8")
    return s