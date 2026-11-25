# ============================================================
# Grade Calculator - Python Week 1 Fundamentals
# Topics: Functions, Loops, Dictionaries
# ============================================================


# --- Dictionary: Grade boundaries ---
GRADE_BOUNDARIES = {
    "A+": 95,
    "A":  85,
    "B+": 75,
    "B":  65,
    "C+": 55,
    "C":  45,
    "D":  35,
    "F":   0,
}


# --- Function: Get letter grade from a numeric score ---
def get_letter_grade(score):
    """Return the letter grade for a given numeric score (0-100)."""
    for grade, minimum in GRADE_BOUNDARIES.items():
        if score >= minimum:
            return grade
    return "F"


# --- Function: Calculate average of a list of scores ---
def calculate_average(scores):
    """Return the average of a list of numeric scores."""
    if len(scores) == 0:
        return 0
    total = 0
    for score in scores:
        total += score
    return total / len(scores)


# --- Function: Collect student scores from user input ---
def get_student_scores():
    """Prompt the user to enter students and their subject scores.
    Returns a dictionary: { student_name: [score1, score2, ...] }
    """
    students = {}

    print("\nEnter student names and scores (type 'done' to finish).")
    print("-" * 50)

    while True:
        name = input("\nStudent name (or 'done'): ").strip()
        if name.lower() == "done":
            break
        if not name:
            print("  Warning: Name cannot be empty. Try again.")
            continue

        scores = []
        print(f"  Enter scores for {name} (press Enter after each, blank line to stop):")

        while True:
            raw = input("    Score: ").strip()
            if raw == "":
                break
            try:
                score = float(raw)
                if 0 <= score <= 100:
                    scores.append(score)
                else:
                    print("    Warning: Score must be between 0 and 100.")
            except ValueError:
                print("    Warning: Please enter a valid number.")

        if scores:
            students[name] = scores
        else:
            print(f"  Warning: No scores entered for {name}. Skipping.")

    return students


# --- Function: Display the final grade report ---
def display_report(students):
    """Print a formatted grade report for all students."""
    if not students:
        print("\nNo student data to display.")
        return

    print("\n" + "=" * 55)
    print(f"{'GRADE REPORT':^55}")
    print("=" * 55)
    print(f"{'Student':<20} {'Average':>8} {'Grade':>6}  {'Scores'}")
    print("-" * 55)

    for name, scores in students.items():
        average = calculate_average(scores)
        grade   = get_letter_grade(average)
        scores_str = ", ".join(str(int(s) if s == int(s) else s) for s in scores)
        print(f"{name:<20} {average:>7.1f}% {grade:>6}  [{scores_str}]")

    print("=" * 55)

    # Overall class average
    all_scores = [calculate_average(s) for s in students.values()]
    class_avg  = calculate_average(all_scores)
    print(f"{'Class Average:':<20} {class_avg:>7.1f}% {get_letter_grade(class_avg):>6}")
    print("=" * 55)


# --- Function: Show grade boundary legend ---
def show_grade_legend():
    """Print the grade boundary table."""
    print("\nGrade Boundaries:")
    print("-" * 25)
    for grade, minimum in GRADE_BOUNDARIES.items():
        print(f"  {grade:<4}  >=  {minimum}%")
    print("-" * 25)


# ============================================================
# Main Program
# ============================================================
def main():
    print("=" * 55)
    print(f"{'GRADE CALCULATOR':^55}")
    print("=" * 55)

    show_grade_legend()

    students = get_student_scores()
    display_report(students)

    print("\nThanks for using Grade Calculator!")


if __name__ == "__main__":
    main()
