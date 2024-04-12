import unittest
from io import StringIO
from unittest.mock import patch
import os
import tempfile

# Importer les fonctions à tester depuis csv_calculator.py
from main import open_file, read_csv, perform_operation, display_result


class TestCSVCalculator(unittest.TestCase):
    def setUp(self):
        # Créer un fichier CSV temporaire pour les tests
        self.file = tempfile.NamedTemporaryFile(mode='w+', delete=False)
        self.filename = self.file.name
        with open(self.filename, 'w') as file:
            file.write("1\n2\n3\n")

    def tearDown(self):
        # Supprimer le fichier CSV temporaire après les tests
        os.remove(self.filename)

    def test_open_file(self):
        # Test d'ouverture de fichier valide
        file = open_file(self.filename)
        self.assertIsNotNone(file)
        file.close()

        # Test d'ouverture de fichier inexistant
        file = open_file('non_existent_file.csv')
        self.assertIsNone(file)

    def test_read_csv(self):
        # Ouvrir et fermer le fichier après l'avoir lu
        with open(self.filename, 'r') as file:
            numbers = read_csv(file)
            self.assertEqual(numbers, [1, 2, 3])

    def test_perform_operation(self):
        # Test d'addition
        result_add = perform_operation([1, 2, 3], '+')
        self.assertEqual(result_add, 6)

        # Test de multiplication
        result_mul = perform_operation([1, 2, 3], '*')
        self.assertEqual(result_mul, 6)

        # Test d'opération invalide
        with self.assertRaises(SystemExit):
            perform_operation([1, 2, 3], '-')

    def test_display_result(self):
        # Rediriger la sortie standard vers un StringIO pour capturer l'affichage
        with patch('sys.stdout', new=StringIO()) as fake_out:
            display_result([1, 2, 3], '+', 6)
            expected_output = "1 + (= 1)\n2 + (= 3)\n3 + (= 6)\n-------\ntotal = 6 (addition)\n"
            self.assertEqual(fake_out.getvalue().strip(), expected_output.strip())


if __name__ == '__main__':
    unittest.main()
