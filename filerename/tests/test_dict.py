def test_1():
    # Define a dictionary code
    websters_dict = {'person': 'a human being',
                    'marathon': 'a running race that is about 26 miles',
                    'resist': 'to remain strong against the force',
                    'run': 'to move with haste; act quickly'}

    print(websters_dict['person'])

    for key in websters_dict.keys():
        print(key)

    for val in websters_dict.values():
        print(val)

    for item in websters_dict.items():
        print(item)

    result = list(map(lambda x: x[0] + "-->", websters_dict.items()))
    result.append('new item')
    print(result)


if __name__ == '__main__':
    test_1()
