# -*- coding: utf-8 -*-
import pdb
from pprint import pprint
import re
import sys
import os
sys.path.append(os.path.normpath(os.path.join(os.path.dirname(__file__), '../lib')))
import config
from models import Superblock, Proposal, GovernanceObject, Setting, Signal, Vote, Outcome, Watchdog
from models import VoteSignals, VoteOutcomes
from peewee import PeeweeException  # , OperationalError, IntegrityError
from goacoind import GoaCoinDaemon
import goacoinlib
from decimal import Decimal
goacoind = GoaCoinDaemon.from_goacoin_conf(config.goacoin_conf)
import misc
# ==============================================================================
# do stuff here

pr = Proposal(
    name='proposal7',
    url='https://goacoincentral.com/proposal7',
    payment_address='nJUUwdV8JvDXjoMLhmqi9mQCgiA86xPL4h',
    payment_amount=39.23,
    start_epoch=1483250400,
    end_epoch=1491022800,
)

# sb = Superblock(
#     event_block_height = 62500,
#     payment_addresses = "n7mzEvBy6JdP2QQUqJrLjitucQKgTBZAR2|nJUUwdV8JvDXjoMLhmqi9mQCgiA86xPL4h",
#     payment_amounts  = "5|3"
# )


# TODO: make this a test, mock 'goacoind' and tie a test block height to a
# timestamp, ensure only unit testing a within_window method
#
# also, create the `within_window` or similar method & use that.
#
bh = 131112
bh_epoch = goacoind.block_height_to_epoch(bh)

fudge = 72000
window_start = 1483689082 - fudge
window_end = 1483753726 + fudge

print("Window start: %s" % misc.epoch2str(window_start))
print("Window end: %s" % misc.epoch2str(window_end))
print("\nbh_epoch: %s" % misc.epoch2str(bh_epoch))


if (bh_epoch < window_start or bh_epoch > window_end):
    print("outside of window!")
else:
    print("Within window, we're good!")

# pdb.set_trace()
# goacoind.get_object_list()
# ==============================================================================
# pdb.set_trace()
1
