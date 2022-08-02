import unittest
from unittest import TestCase

from project.student import Student


class StudentTests(TestCase):
    STUDENT_NAME = 'Gosho'

    def setUp(self) -> None:
        self.student = Student(self.STUDENT_NAME)

    def test_init__without_courses_given(self):
        self.assertEqual(self.STUDENT_NAME, self.student.name)
        self.assertEqual({}, self.student.courses)

    def test_init__with_courses_given(self):
        courses = {'Python Advanced': ['note1', 'note2']}
        student = Student(self.STUDENT_NAME, courses)
        self.assertEqual(self.STUDENT_NAME, student.name)
        self.assertEqual(courses, student.courses)

    def test_enroll__student_updates_course_notes_when_course_is_already_enrolled(self):
        course_name = 'Python Advanced'
        course_notes = ['note1', 'note2']
        courses = {course_name: course_notes}
        student = Student(self.STUDENT_NAME, courses)

        result = student.enroll(course_name, ['note3', 'note4'])

        self.assertEqual("Course already added. Notes have been updated.", result)
        self.assertEqual(['note1', 'note2', 'note3', 'note4'], student.courses[course_name])

    def test_enroll__student_extends_courses_with_course_and_notes_when_add_course_notes_is_not_passed(self):
        course_name = 'Python OOP'
        course_notes = ['note 1', 'note 2']
        result = self.student.enroll(course_name, course_notes)

        self.assertEqual("Course and course notes have been added.", result)
        self.assertTrue(course_name in self.student.courses)
        self.assertEqual(course_notes, self.student.courses[course_name])

    def test_enroll__student_extends_courses_with_course_and_notes_when_add_course_notes_is_y(self):
        course_name = 'Python OOP'
        course_notes = ['note 1', 'note 2']
        result = self.student.enroll(course_name, course_notes, "Y")

        self.assertEqual("Course and course notes have been added.", result)
        self.assertTrue(course_name in self.student.courses)
        self.assertEqual(course_notes, self.student.courses[course_name])

    def test_enroll__student_extends_courses_with_course_without_notes_when_invalid_add_course_notes_argument_is_passed(self):
        course_name = 'Python OOP'
        course_notes = ['note 1', 'note 2']
        result = self.student.enroll(course_name, course_notes, "N")

        self.assertEqual("Course has been added.", result)
        self.assertTrue(course_name in self.student.courses)
        self.assertEqual([], self.student.courses[course_name])

    def test_add_notes__adding_non_existing_course__raises_error(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes('Python Advanced', 'Note 3')
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_add_notes__adding_existing_course__updates_course_notes(self):
        course_name = 'Python Advanced'
        course_notes = ['note1', 'note2']
        courses = {course_name: course_notes}
        student = Student(self.STUDENT_NAME, courses)

        result = student.add_notes(course_name, 'note3')
        self.assertEqual("Notes have been updated", result)
        self.assertEqual(['note1', 'note2', 'note3'], student.courses[course_name])

    def test_leave_course__raises_error_when_course_is_not_existing(self):
        self.student.enroll('Python Basics', [])

        with self.assertRaises(Exception) as ex:
            self.student.leave_course('Python Advanced')
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))

    def test_leave_course__when_student_is_enrolled_for_course_is_existing__remove_course(self):
        course_name = 'Python Advanced'
        student = Student(self.STUDENT_NAME, {course_name: []})

        result = student.leave_course(course_name)
        self.assertEqual("Course has been removed", result)
        self.assertTrue(course_name not in student.courses)



if __name__ == '__main__':
    unittest.main()