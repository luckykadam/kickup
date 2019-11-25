import csv


def csv_to_dict(file_name, klass):
    print('loading {} to {} entities'.format(file_name, klass.__name__))
    with open(file_name) as csv_file:
        reader = csv.DictReader(csv_file)
        objects = [klass(**row) for row in reader]
        return {obj.id: obj for obj in objects}


def csv_to_relationship(file_name, a, b):
    print('loading {} to relationships'.format(file_name))
    with open(file_name) as csv_file:
        reader = csv.reader(csv_file)
        next(reader)  # skip the header
        a_to_b = {id: set() for id in a}
        b_to_a = {id: set() for id in b}
        for (a, b) in reader:
            a_to_b[a].add(b)
            b_to_a[b].add(a)
        return a_to_b, b_to_a


def print_entities(entities):
    for id in entities:
        print('{}: {}'.format(id, entities[id]))
