from p2pool.bitcoin import networks

PARENT=networks.nets['cycoin'],
SHARE_PERIOD=15, # seconds
NEW_SHARE_PERIOD=15, # seconds
CHAIN_LENGTH=12*60*60//15, # shares
REAL_CHAIN_LENGTH=12*60*60//15, # shares
TARGET_LOOKBEHIND=10, 
SPREAD=30, # blocks
IDENTIFIER='f0e9a96e6b7e01a8'.decode('hex'),
PREFIX='e0f84ac965e01af8'.decode('hex'),
P2P_PORT=7441,
MIN_TARGET=4,
MAX_TARGET=2**256//2**20 - 1,
PERSIST=False,
WORKER_PORT=9441,
BOOTSTRAP_ADDRS='p2pool-eu.gotgeeks.com p2pool-us.gotgeeks.com rav3n.dtdns.net doge.dtdns.net pool.hostv.pl p2pool.org p2pool.gotgeeks.com p2pool.dtdns.net solidpool.org taken.pl'.split(' ')
ANNOUNCE_CHANNEL='#p2pool-alt',
VERSION_CHECK=lambda v: True,
