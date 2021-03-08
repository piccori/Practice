student_data = [
    {'name': 'Bob', 'id': 0, 'scores': [68, 75, 56, 81]},
    {'name': 'Alice', 'id': 1, 'scores': [75, 90, 64, 88]},
    {'name': 'Carol', 'id': 2, 'scores': [59, 74, 71, 68]},
    {'name': 'Dan', 'id': 3, 'scores': [64, 58, 53, 62]},
]


def process_student_data(data, pass_threshold=60,
                         merit_threshold=75):

    for sdata in data:
        av = sum(sdata['scores'])/float(len(sdata['scores']))
        sdata['average'] = av

        if av > merit_threshold:
            sdata['assessment'] = 'passed with merit'
        elif av > pass_threshold:
            sdata['assessment'] = 'passed'
        else:
            sdata['assessment'] = 'failed'

        print("%s's(id:%d) final assessment is: %s" % (
            sdata['name'], sdata['id'], sdata['assessment'].upper()))


if __name__ == '__main__':
    process_student_data(student_data)
