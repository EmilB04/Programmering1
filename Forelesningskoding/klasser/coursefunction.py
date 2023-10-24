
def calculate_total_credits(course_list):
    '''
    Funksjonen skal regne ut antall studiepoeng fra en liste med Course-objekter
    :param course_list: liste med Course-objekter
    :return: total_credits
    '''
    total_credits = 0
    for course in course_list:
        total_credits += course.credits
    return total_credits
