import sys
import csv
from typing import TextIO, List, Optional


def open_file(filename: str) -> Optional[TextIO]:
    """
    Ouvre le fichier en mode lecture et renvoie l'objet de fichier ouvert.
    """
    try:
        file = open(filename, 'r')
        return file
    except FileNotFoundError:
        print("Le fichier spécifié n'a pas été trouvé.")
        return None


def read_csv(file: TextIO) -> List[int]:
    """
    Lit le contenu du fichier CSV et renvoie une liste des nombres.
    """
    try:
        csvreader = csv.reader(file)
        numbers = [int(row[0]) for row in csvreader]
        return numbers
    except csv.Error as e:
        print(f"Erreur lors de la lecture du fichier CSV : {e}")
        sys.exit(1)


def perform_operation(numbers: List[int], operation: str) -> int:
    """
    Effectue l'opération spécifiée sur la liste de nombres.
    """
    if operation == '+':
        result = sum(numbers)
    elif operation == '*':
        result = 1
        for num in numbers:
            result *= num
    else:
        print("Opération non valide. Seules les opérations '+' et '*' sont autorisées.")
        sys.exit(1)
    return result


def display_result(numbers: List[int], operation: str, result: int):
    """
    Affiche les opérations et le résultat formatés.
    """
    print("\n".join([f"{num} {operation}" + (f" (= {sum(numbers[:i + 1])})" if operation == '+' else '') for i, num in
                     enumerate(numbers)]))
    print("-------")
    print(f"total = {result} ({'addition' if operation == '+' else 'multiplication'})")


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python script.py <filename.csv> <+ or *>")
        sys.exit(1)

    filename = "./datas/"+sys.argv[1]
    operation = sys.argv[2]

    file = open_file(filename)
    numbers = read_csv(file)
    result = perform_operation(numbers, operation)
    display_result(numbers, operation, result)
