from student import Course, Student
import coursefunction

emil_berglund = Student("Emil", "Berglund", 19, 12612)

programmering1 = Course("Programmering 1", "ITF19024", 10)
webuvikling = Course("Webutvikling", "ITF23019", 10)
design = Course("Design", "ITF32789", 10)

emil_berglund.enroll_in_course(programmering1)
emil_berglund.enroll_in_course(webuvikling)

print(emil_berglund.getTotalCredits())