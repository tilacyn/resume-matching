junk_subs = {
    '\n',
    '\t',
    '\r',
    '\x91',
    '\x92',
    '\x93',
    '\x94',
    '\x95',
    '\x96',
    '\x97',
    '\x98'
}


def make_prefix_by_special_field(s):
    return s + ':'


def related(data, field):
    return data.startswith(make_prefix_by_special_field(field)) or data.startswith(field)

def try_add_field(data, field_map, field_set):
    for key in field_set:
        if related(data.lower(), key) or related(data, key):
            value_start_index = len(key) + 2
            field_map[key] = data[value_start_index:]
            return True
    return False


def format(data):
    result = data
    for junk in junk_subs:
        result = result.replace(junk, " ")
    return result.strip()