import os

SOURCE_FOLDER = ("data_ro")
SOURCE_FILES = os.listdir(SOURCE_FOLDER)


def search_for_keys(target_keys):
    matching_doc_count = 0
    for file in SOURCE_FILES:

        if '.txt' in file:
            data = read_data_from_file(file)
            found = find_keys_in_text(data, target_keys)

            if len(found) == len(target_keys):
                write_results(data)
                matching_doc_count += 1
    return matching_doc_count > 0


def read_data_from_file(file):
    f = open(SOURCE_FOLDER + os.path.sep + file, encoding='iso-8859-2')
    data = str(f.read())
    f.close()
    return data


def find_keys_in_text(data, target_keys):
    found = []
    for key in target_keys:
        if key in data:
            found += [key]
    return set(found)


def write_results(data):
    path = os.path.join(SOURCE_FOLDER, 'result.txt')
    f2 = open(path, 'a', encoding='ISO-8859-2')
    f2.write(data)
    f2.write('\r')
    f2.close()


print("Cautare dupa 'fals'")
matches = search_for_keys(["fake news"])
if not matches:
    print("Nu s-a gasit 'fals'")
    print("Cautare dupa 'adevarat'")
    matches = search_for_keys(["fals"])
    if not matches:
        print("Nu s-a gasit 'adevarat'")
        print("Introduceti un cuvant pentru cautare")
        search_for_keys([str(input())])
