import os
import sys


def construct_path(file_path: str) -> str:
    cd = os.path.dirname(os.path.realpath(__file__))
    result = os.path.join(cd, file_path)

    return result


def init(*, difficulty: str, exercise: str) -> None:
    file_path = f"{difficulty}/ex{exercise}.py"
    target_path = construct_path(file_path)

    with open(target_path, "w+"):
        print(f"Created an exercise file at {target_path}")



def init_test(*, difficulty: str, exercise: str) -> None:
    file_path = f"{difficulty}/test/test_ex{exercise}.py"
    target_path = construct_path(file_path)

    with open(target_path, "w+") as f:
        f.write(f"from leetcode.{difficulty}.ex{exercise} import InitialSolution\n\n\n")
        f.write(f"def test_temp():\n")
        f.write(f"    assert InitialSolution().replace()")
        print(f"Created a test file at {target_path}")



if __name__ == "__main__":
    difficulty = sys.argv[1]
    exercise = sys.argv[2]

    init(difficulty=difficulty, exercise=exercise)
    init_test(difficulty=difficulty, exercise=exercise)
