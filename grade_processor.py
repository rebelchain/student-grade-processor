from typing import TypedDict


class InvalidScoreError(Exception):
  """An exception that is thrown when the score is outside the range of 0–100."""
  pass

class Student(TypedDict):
    name: str
    score: float


def validate_score(score: float) -> None:
    if score < 0 or score > 100:
      raise InvalidScoreError(f"The {score} value is invalid! It must be in the range of 0–100.")


    

def calculate_average(students: list[Student]) -> float:
    if not students:
        return 0.0

    scores: list[float] = []
    for student in students:
        score = student["score"]
        validate_score(score)
        scores.append(score)

    return sum(scores) / len(scores)



def get_highest_lowest(datas: list[Student]) -> tuple[Student, Student]:
   if not datas:
      raise ValueError(f"Student data cannot be empty")

   for student in datas:
      validate_score(student["score"])

   highest_score = max(datas, key=lambda s: s["score"])
   lower_score = min(datas, key=lambda s: s["score"])

   return highest_score, lower_score



def get_pass_fail_status(datas: list[Student], passing_score: float = 60.0) -> list[dict]:
  if not datas:
     raise ValueError(f"Student data cannot be empty")
  for student in datas:
     validate_score(student["score"])
  new_student_data = []

  for student in datas:
     status = "Pass" if student["score"] >= passing_score else "Fail"
     new_student_data.append({**student, "status": status})

  return new_student_data





