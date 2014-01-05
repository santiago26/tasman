# -*- coding: utf-8 -*-
#
# Copyright (C) 2014 Alexander Shorin
# All rights reserved.
#
# This software is licensed as described in the file LICENSE, which
# you should have received as part of this distribution.
#

from xmppflask import XmppFlask

app = XmppFlask('tasman')


@app.route(u'test')
def test():
    return 'passed'
