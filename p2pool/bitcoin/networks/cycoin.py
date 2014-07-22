import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX='fbc0b6db'.decode('hex'),
P2P_PORT=33833,
ADDRESS_VERSION=28,
RPC_PORT=19333,
RPC_CHECK=defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
	'conspiracycoinaddress' in (yield bitcoind.rpc_help()) and
	not (yield bitcoind.rpc_getinfo())['testnet']
)),
SUBSIDY_FUNC=lambda height: 33*100000000,
BLOCKHASH_FUNC=lambda data: pack.IntType(256).unpack(__import__('xcoin_hash').getPoWHash(data)),
POW_FUNC=lambda data: pack.IntType(256).unpack(__import__('xcoin_hash').getPoWHash(data)),
BLOCK_PERIOD=120, # s
SYMBOL='CYC',
CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'Conspiracycoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Conspiracycoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.conspiracycoin'), 'conspiracycoin.conf'),
BLOCK_EXPLORER_URL_PREFIX='http://block.conspiracycoin.org/block/',
ADDRESS_EXPLORER_URL_PREFIX='http://block.conspiracycoin.org/address/',
TX_EXPLORER_URL_PREFIX='http://block.conspiracycoin.org/tx/',
SANE_TARGET_RANGE=(2**256//2**32//1000 - 1, 2**256//2**20 - 1), 
DUMB_SCRYPT_DIFF=1,
DUST_THRESHOLD=0.001e8,
