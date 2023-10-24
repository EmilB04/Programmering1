
def calculate_total_credits(course_list):
    total_credits = 0
    for course in course_list:
        total_credits += course.credits
    return total_credits