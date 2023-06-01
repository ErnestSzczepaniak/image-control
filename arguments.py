from datetime import datetime
import binascii, os, uuid

def convert_hex(value: str):
    return int(value, 16)

def convert_bool(value: str):
    return value.lower() in ['true', '1', 'yes']

def convert_size(value: str):
    multiplier = 1
    if value[-1].lower() == 'k':
        multiplier = 1024
    elif value[-1].lower() == 'm':
        multiplier = 1024 * 1024
    return int(value[:-1]) * multiplier

def default_date() -> str:
    return datetime.now().strftime('%d.%m.%Y')

def default_time() -> str:
    return datetime.now().strftime('%H:%M:%S')

def default_random() -> str:
    return binascii.hexlify(os.urandom(64)).decode()

def default_id() -> str:
    return str(uuid.uuid4())

# /* ---------------------------------------------| generic |--------------------------------------------- */

INPUT =                             ['--input',                             {'required': True,      'type': str,            'default': '',                                      'help': 'Input file'}]
OUTPUT =                            ['--output',                            {'required': True,      'type': str,            'default': '',                                      'help': 'Output file'}]

# /* ---------------------------------------------| header |--------------------------------------------- */

HEADER_MAGIC =                      ['--header-magic',                      {'required': False,     'type': str,            'default': 'DKWC',                                  'help': 'Header magic'}]
HEADER_PROTECTION =                 ['--header-protection',                 {'required': False,     'type': str,            'default': '1-0',                                   'help': 'Header protection'}]

HEADER_CRC =                        ['--header-crc',                        {'required': False,     'type': convert_bool,   'default': 'True',                                  'help': 'Header CRC'}]
HEADER_CRC_POLYNOMIAL =             ['--header-crc-polynominal',            {'required': False,     'type': convert_hex,    'default': '0x104C11DB7',                           'help': 'Header CRC polynomial'}]
HEADER_CRC_INITIAL_VALUE =          ['--header-crc-initial-value',          {'required': False,     'type': convert_hex,    'default': '0x0',                                   'help': 'Header CRC initial value'}]
HEADER_CRC_REVERSE =                ['--header-crc-reverse',                {'required': False,     'type': convert_bool,   'default': 'False',                                 'help': 'Header CRC reverse'}]

HEADER_HASH =                       ['--header-hash',                       {'required': False,     'type': convert_bool,   'default': 'True',                                 'help': 'Header hash'}] 
HEADER_HASH_ALGORITHM =             ['--header-hash-algorithm',             {'required': False,     'type': str,            'default': 'sha-256',                                'help': 'Header hash algorithm'}]
HEADER_HASH_LENGTH =                ['--header-hash-length',                {'required': False,     'type': int,            'default': 32,                                      'help': 'Header hash length'}]

# /* ---------------------------------------------| firmware |--------------------------------------------- */

FIRMWARE_ID =                       ['--firmware-id',                       {'required': False,     'type': str,            'default': default_id(),                            'help': 'Firmware ID'}]
FIRMWARE_AUTHOR =                   ['--firmware-author',                   {'required': False,     'type': str,            'default': 'anonymous',                             'help': 'Firmware author'}]
FIRMWARE_FILE =                     ['--firmware-file',                     {'required': False,     'type': str,            'default': '',                                      'help': 'Firmware file'}]
FIRMWARE_VERSION =                  ['--firmware-version',                  {'required': False,     'type': str,            'default': '1.0.0',                                 'help': 'Show version'}]
FIRMWARE_STABILITY =                ['--firmware-stability',                {'required': False,     'type': str,            'default': 'stable',                                'help': 'Firmware stability'}]
FIRMWARE_DATE =                     ['--firmware-date',                     {'required': False,     'type': str,            'default': default_date(),                          'help': 'Firmware date'}]
FIRMWARE_TIME =                     ['--firmware-time',                     {'required': False,     'type': str,            'default': default_time(),                          'help': 'Firmware time'}]
FIRMWARE_VENDOR =                   ['--firmware-vendor',                   {'required': False,     'type': str,            'default': '',                                      'help': 'Firmware vendor'}]
FIRMWARE_PRODUCT =                  ['--firmware-product',                  {'required': False,     'type': str,            'default': '',                                      'help': 'Firmware product'}]
FIRMWARE_MODEL =                    ['--firmware-model',                    {'required': False,     'type': str,            'default': '',                                      'help': 'Firmware model'}]
FIRMWARE_CHIP =                     ['--firmware-chip',                     {'required': False,     'type': str,            'default': '',                                      'help': 'Firmware chip'}]
FIRMWARE_MODE =                     ['--firmware-mode',                     {'required': False,     'type': str,            'default': '',                                      'help': 'Firmware mode'}]
FIRMWARE_PROTECTION =               ['--firmware-protection',               {'required': False,     'type': str,            'default': '1-1-1-0-0',                               'help': 'Payload protection'}]

FIRMWARE_CRC =                      ['--firmware-crc',                      {'required': False,     'type': convert_bool,   'default': 'True',                                  'help': 'Header CRC'}]
FIRMWARE_CRC_POLYNOMIAL =           ['--firmware-crc-polynominal',          {'required': False,     'type': convert_hex,    'default': '0x104C11DB7',                           'help': 'Header CRC polynomial'}]
FIRMWARE_CRC_INITIAL_VALUE =        ['--firmware-crc-initial-value',        {'required': False,     'type': convert_hex,    'default': '0x0',                                   'help': 'Header CRC initial value'}]
FIRMWARE_CRC_REVERSE =              ['--firmware-crc-reverse',              {'required': False,     'type': convert_bool,   'default': 'False',                                 'help': 'Header CRC reverse'}]

FIRMWARE_HASH =                     ['--firmware-hash',                     {'required': False,     'type': convert_bool,   'default': 'True',                                  'help': 'Header hash'}] 
FIRMWARE_HASH_ALGORITHM =           ['--firmware-hash-algorithm',           {'required': False,     'type': str,            'default': 'sha-256',                               'help': 'Header hash algorithm'}]
FIRMWARE_HASH_LENGTH =              ['--firmware-hash-length',              {'required': False,     'type': int,            'default': 32,                                      'help': 'Header hash length'}]

FIRMWARE_SIGNATURE =                ['--firmware-signature',                {'required': False,     'type': convert_bool,   'default': 'True',                                  'help': 'Header signature'}]
FIRMWARE_SIGNATURE_ALGORITHM =      ['--firmware-signature-algorithm',      {'required': False,     'type': str,            'default': 'hmac-sha-256',                          'help': 'Header signature algorithm'}]
FIRMWARE_SIGNATURE_KEY =            ['--firmware-signature-key',            {'required': False,     'type': str,            'default': '12345678',                              'help': 'Header signature key'}]

FIRMWARE_ENCRYPTION =               ['--firmware-encryption',               {'required': False,     'type': convert_bool,   'default': 'False',                                  'help': 'Header encryption'}]
FIRMWARE_ENCRYPTION_ALGORITHM =     ['--firmware-encryption-algorithm',     {'required': False,     'type': str,            'default': 'aes-256-ecb',                           'help': 'Header encryption algorithm'}]
FIRMWARE_ENCRYPTION_KEY =           ['--firmware-encryption-key',           {'required': False,     'type': str,            'default': '0123456789abcdef',                      'help': 'Header encryption key'}]
FIRMWARE_ENCRYPTION_IV =            ['--firmware-encryption-iv',            {'required': False,     'type': str,            'default': '0123456789abcdef',                      'help': 'Header encryption iv'}]

FIRMWARE_RANDOM =                   ['--firmware-random',                   {'required': False,     'type': str,            'default': default_random(),                           'help': 'Header random'}]

# /* ---------------------------------------------| structure |--------------------------------------------- */

IMAGE_SIZE =                        ['--image-size',                        {'required': True,     'type': convert_size,    'default': '',                                    'help': 'Image size'}]
IMAGE_LAYOUT =                      ['--image-layout',                      {'required': False,     'type': str,            'default': ['firmware', 'padding', 'header'],        'help': 'Image layout', 'nargs': '+'}]