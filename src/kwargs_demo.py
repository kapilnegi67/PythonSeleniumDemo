def print_student_data(**data):
    print("First Name = %s" % (data.get("first_name", None)))
    print("Middle Name = %s" % (data.get("middle_name", "")))
    print("Course Name = %s" % (data.get("course_name", None)))

print_student_data(first_name="Kapil",
                   middle_name="Kumar",
                   course_name="CSE")
print("\n\n\n\n\n")
print_student_data(first_name="Kapil",
                   course_name="CSE")