import unittest
from student_crud import Student, StudentRegistrationSystem

class TestStudentRegistrationSystem(unittest.TestCase):
    def setUp(self):
        """Set up a new StudentRegistrationSystem before each test"""
        self.system = StudentRegistrationSystem()
        #prepopulate with 1 student for certain tests
        self.test_student_id = "12345"
        self.test_student = {
            "name": "John Doe",
            "age": 20,
            "major": "Computer Science"
        }
        self.system.create_student(
            self.test_student_id,
            self.test_student["name"],
            self.test_student["age"],
            self.test_student["major"]
        )

    def test_student_creation(self):
        """Test CREATE operations"""
        #test succesful student creation
        self.assertTrue(
            self.system.create_student("67890", "Jane Smith", 22, "Physics")
        )
        
        #test dupe student ID
        self.assertFalse(
            self.system.create_student(self.test_student_id, "Another John", 25, "Math")
        )

    def test_student_reading(self):
        """Test READ operations"""
        #test reading existing student
        result = self.system.read_student(self.test_student_id)
        self.assertEqual(result, self.test_student_id)
        
        #test reading nonexistent student
        result = self.system.read_student("nonexistent")
        self.assertIsNone(result)
        
        #test reading all students
        #case 1: with students
        students = list(self.system.read_all_students())
        self.assertEqual(len(students), 1)
        
        #case 2: empty system
        empty_system = StudentRegistrationSystem()
        self.assertEqual(list(empty_system.read_all_students()), [])

    def test_student_update(self):
        """Test UPDATE operations"""
        #test successful update with all fields
        self.assertTrue(
            self.system.update_student(
                self.test_student_id,
                name="John Updated",
                age=21,
                major="Data Science"
            )
        )
        
        #verify the updates
        updated_student = self.system.students[self.test_student_id]
        self.assertEqual(updated_student.name, "John Updated")
        self.assertEqual(updated_student.age, 21)
        self.assertEqual(updated_student.major, "Data Science")
        
        #test partial update
        self.assertTrue(
            self.system.update_student(
                self.test_student_id,
                name="John Partial"
            )
        )
        
        #verify only name was updated
        partial_updated = self.system.students[self.test_student_id]
        self.assertEqual(partial_updated.name, "John Partial")
        self.assertEqual(partial_updated.age, 21)  #should stay unchanged
        self.assertEqual(partial_updated.major, "Data Science")  #should stay unchanged
        
        #test update of nonexistent student
        self.assertFalse(
            self.system.update_student("nonexistent", name="Nobody")
        )

    def test_student_deletion(self):
        """Test DELETE operations"""
        #test successful deletion
        self.assertTrue(
            self.system.delete_student(self.test_student_id)
        )
        
        #verify student was deletd
        self.assertNotIn(self.test_student_id, self.system.students)
        
        #test deleton of nonexistent student
        self.assertFalse(
            self.system.delete_student("nonexistent")
        )

    def test_student_str_representation(self):
        """Test Student class string representation"""
        student = Student("12345", "John Doe", 20, "Computer Science")
        expected_str = "ID: 12345, Name: John Doe, Age: 20, Major: Computer Science"
        self.assertEqual(str(student), expected_str)

if __name__ == '__main__':
    unittest.main()

#run code by using command: python -m unittest test_student_crud.py