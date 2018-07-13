#!/usr/bin/env python
# -*- coding=utf-8 -*-
# author: Dongye Li<dongye@gooalgene.com>
# 2018-07-06 20:07

import sys
from . import db

args = sys.argv


class JournalData(db.Model):

    # 期刊信息表

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(128))
    abbreviated = db.Column(db.String(32))
    ISSN = db.Column(db.String(32))
    total_cites = db.Column(db.Integer)
    IF = db.Column(db.Float)
    IF_without_self_cites = db.Column(db.Float)
    IF_5_year = db.Column(db.Float)
    immediacy_index = db.Column(db.String(32))
    citable_items = db.Column(db.String(32))
    cited_half_life = db.Column(db.String(32))
    citing_half_life = db.Column(db.String(32))
    eigenfactor_score = db.Column(db.String(32))
    influence_score = db.Column(db.String(32))
    articles_in_citable_items = db.Column(db.String(32))
    ajifp = db.Column(db.String(32))
    normalized_eigenfactor = db.Column(db.String(32))

    # def __init__(self, title="", abbreviated="", ISSN="", total_cites=0, IF=0, IF_without_self_cites=0,
    #              IF_5_year="", immediacy_index="", citable_items="", cited_half_life="", citing_half_life="",
    #              eigenfactor_score="", influence_score="", articles_in_citable_items="", ajifp="",
    #              normalized_eigenfactor=""):
    #     self.title = title
    #     self.abbreviated = abbreviated
    #     self.ISSN = ISSN
    #     self.total_cites = total_cites
    #     self.IF = IF
    #     self.IF_without_self_cites = IF_without_self_cites
    #     self.IF_5_year = IF_5_year
    #     self.immediacy_index = immediacy_index
    #     self.citable_items = citable_items
    #     self.cited_half_life = cited_half_life
    #     self.cited_half_life = citing_half_life
    #     self.eigenfactor_score = eigenfactor_score
    #     self.influence_score = influence_score
    #     self.articles_in_citable_items = articles_in_citable_items
    #     self.ajifp = ajifp
    #     self.normalized_eigenfactor = normalized_eigenfactor

    def get_dict(self):
        return {
            'title' : self.title,
            'abbreviated' : self.abbreviated,
            'ISSN' : self.ISSN,
            'total_cites' : self.total_cites,
            'IF' : self.IF,
            'IF_without_self_cites' : self.IF_without_self_cites,
            'IF_5_year' : self.IF_5_year,
            'immediacy_index' : self.immediacy_index,
            'citable_items' : self.citable_items,
            'cited_half_life' : self.cited_half_life,
            'citing_half_life' : self.citing_half_life,
            'eigenfactor_score' : self.eigenfactor_score,
            'influence_score' : self.influence_score,
            'articles_in_citable_items' : self.articles_in_citable_items,
            'ajifp' : self.ajifp,
            'normalized_eigenfactor' : self.normalized_eigenfactor,
        }