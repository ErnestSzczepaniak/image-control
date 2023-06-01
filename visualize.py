from typing import List

WIDTH = 32

def calculate_scale(size: int):
    if size == 16: return 0
    if size == 32: return 1
    if size == 64: return 2
    if size == 128: return 3
    else: return 5

def create_element(name: str, address: int, offset: int, size: int) -> List[str]:
    
    element = []

    element.append(f'+{"-" * WIDTH}+ 0x{address:08x} (+0x{offset:x})')

    scale = calculate_scale(size)

    for _ in range(0, scale):
        element.append(f'|{" " * WIDTH}|')


    element.append(f'|{name.center(WIDTH)}| {size} (B)')

    for _ in range(0, scale):
        element.append(f'|{" " * WIDTH}|')

    return element

def create_group(name: str, items: List[str]):

    group = []

    for index, line in enumerate(items):
        if index == 0:
            group.append(f'+{"-" * WIDTH}{line}')
        elif index == len(items) / 2:
            group.append(f'|{name.center(WIDTH)}{line}')
        else:
            group.append(f'|{" " * WIDTH}{line}')
    return group

def create_map(layout: List[str], size_firmware: int, size_padding: int, header_layout: dict):

    offset_global = 0
    offset_local = 0
    result = []

    for image in layout:

        if image == 'firmware':
            items = create_element('.firmware', offset_global, 0, size_firmware)
            group = create_group('FIRMWARE', items)
            result.extend(group)
            offset_global += size_firmware
        elif image == 'padding':
            items = create_element('.padding', offset_global, 0, size_padding)
            group = create_group('PADDING', items)
            result.extend(group)
            offset_global += size_padding
        elif image == 'header':
            all_items = []
            for item in header_layout:
                items = create_element(f'.{item}', offset_global, offset_local, header_layout[item])
                all_items.extend(items)
                offset_local += header_layout[item]
                offset_global += header_layout[item]
            group = create_group('HEADER', all_items)
            result.extend(group)

    result.append('+' + '-' * WIDTH + '+' + '-' * WIDTH + '+')

    with open('map.txt', 'w') as output:
        for line in result:
            output.write(line + '\n')