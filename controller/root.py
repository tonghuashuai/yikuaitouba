#!/usr/bin/env python
# -*- coding: utf-8 -*-


from _base import Base
from misc._route import route


@route('/')
class Index(Base):
    def get(self):
        self.redirect('http://comefunding.com', True)


@route('/tv')
class Investors(Base):
    def get(self):
        self.render()


# @route('/new')
# class NewIndex(Base):
#     def get(self):
#         self.render()
# 
# 
# @route('/mishi')
# class Mishi(Base):
#     def get(self):
#         self.render()
# 
# 
# @route('/danmu')
# class Danmu(Base):
#     def get(self):
#         self.render()
