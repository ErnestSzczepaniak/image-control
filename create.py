import pathlib, arguments, visualize
from header import Header, FIELDS as HEADER_FIELDS
from firmware import Firmware


ARGUMENTS = [
    arguments.INPUT,
    arguments.OUTPUT,
    arguments.HEADER_MAGIC,
    arguments.HEADER_PROTECTION,
    arguments.HEADER_CRC,
    arguments.HEADER_CRC_POLYNOMIAL,
    arguments.HEADER_CRC_INITIAL_VALUE,
    arguments.HEADER_CRC_REVERSE,
    arguments.HEADER_HASH,
    arguments.HEADER_HASH_ALGORITHM,
    arguments.HEADER_HASH_LENGTH,
    arguments.FIRMWARE_ID,
    arguments.FIRMWARE_AUTHOR,
    arguments.FIRMWARE_FILE,
    arguments.FIRMWARE_VERSION,
    arguments.FIRMWARE_STABILITY,
    arguments.FIRMWARE_DATE,
    arguments.FIRMWARE_TIME,
    arguments.FIRMWARE_VENDOR,
    arguments.FIRMWARE_PRODUCT,
    arguments.FIRMWARE_MODEL,
    arguments.FIRMWARE_CHIP,
    arguments.FIRMWARE_MODE,
    arguments.FIRMWARE_PROTECTION,
    arguments.FIRMWARE_CRC,
    arguments.FIRMWARE_CRC_POLYNOMIAL,
    arguments.FIRMWARE_CRC_INITIAL_VALUE,
    arguments.FIRMWARE_CRC_REVERSE,
    arguments.FIRMWARE_HASH,
    arguments.FIRMWARE_HASH_ALGORITHM,
    arguments.FIRMWARE_HASH_LENGTH,
    arguments.FIRMWARE_SIGNATURE,
    arguments.FIRMWARE_SIGNATURE_ALGORITHM,
    arguments.FIRMWARE_SIGNATURE_KEY,
    arguments.FIRMWARE_RANDOM,
    arguments.FIRMWARE_ENCRYPTION,
    arguments.FIRMWARE_ENCRYPTION_ALGORITHM,
    arguments.FIRMWARE_ENCRYPTION_KEY,
    arguments.FIRMWARE_ENCRYPTION_IV,
    arguments.IMAGE_SIZE,
    arguments.IMAGE_LAYOUT
]

def execute(**kwargs):

    path_input = pathlib.Path(kwargs['input']).absolute()
    path_output = pathlib.Path(kwargs['output']).absolute()

    firmware = Firmware()
    header = Header()

    with open(path_input, 'rb') as input:

        firmware.data = bytearray(input.read())

    # /* ---------------------------------------------| process firmware |--------------------------------------------- */

    if kwargs['firmware_crc'] == True:

        polynomial = kwargs['firmware_crc_polynominal']
        initial_value = kwargs['firmware_crc_initial_value']
        reverse = kwargs['firmware_crc_reverse']

        header.firmware_crc = firmware.crc(polynomial, initial_value, reverse)

    if kwargs['firmware_hash'] == True:

        algorithm = kwargs['firmware_hash_algorithm']
        length = kwargs['firmware_hash_length']

        header.firmware_hash = firmware.hash(algorithm, length)

    if kwargs['firmware_signature'] == True:

        algorithm = kwargs['firmware_signature_algorithm']
        key = kwargs['firmware_signature_key']

        header.firmware_signature = firmware.signature(algorithm, key)

    if kwargs['firmware_encryption'] == True:

        algorithm = kwargs['firmware_encryption_algorithm']
        key = kwargs['firmware_encryption_key']
        iv = kwargs['firmware_encryption_iv']

        firmware.encrypt(algorithm, key, iv)

    # /* ---------------------------------------------| process header |--------------------------------------------- */

    header.firmware_id = kwargs['firmware_id']
    header.firmware_author = kwargs['firmware_author']
    header.firmware_file = kwargs['firmware_file'] if kwargs['firmware_file'] != '' else path_input.name
    header.firmware_version = kwargs['firmware_version']
    header.firmware_stability = kwargs['firmware_stability']
    header.firmware_date = kwargs['firmware_date']
    header.firmware_time = kwargs['firmware_time']
    header.firmware_vendor = kwargs['firmware_vendor']
    header.firmware_product = kwargs['firmware_product']
    header.firmware_model = kwargs['firmware_model']
    header.firmware_chip = kwargs['firmware_chip']
    header.firmware_mode = kwargs['firmware_mode']
    header.firmware_size = firmware.size()
    header.firmware_protection = kwargs['firmware_protection']
    header.firmware_random = kwargs['firmware_random']
    
    header.header_magic = kwargs['header_magic']
    header.header_protection = kwargs['header_protection']

    if kwargs['header_crc'] == True:

        polynomial = kwargs['header_crc_polynominal']
        initial_value = kwargs['header_crc_initial_value']
        reverse = kwargs['header_crc_reverse']

        header.header_crc = header.crc(polynomial, initial_value, reverse)

    if kwargs['header_hash'] == True:

        algorithm = kwargs['header_hash_algorithm']
        length = kwargs['header_hash_length']

        header.header_hash = header.hash(algorithm, length)

    # /* ---------------------------------------------| create layout |--------------------------------------------- */

    padding_size = kwargs['image_size'] - firmware.size() - header.size()

    padding = bytearray(padding_size)
    image = bytearray()

    for element in kwargs['image_layout']:
        if element == 'header':
            image.extend(header.data)
        elif element == 'firmware':
            image.extend(firmware.data)
        elif element == 'padding':
            image.extend(padding)

    with open(path_output, 'wb') as output:
        output.write(image)

    visualize.create_map(kwargs['image_layout'], firmware.size(), padding_size, HEADER_FIELDS)