import builtins
import pywebio


class Terminal:
    @staticmethod
    def cprint(message):
        builtins.print(message)

    @staticmethod
    def cinput(message):
        return builtins.input(message)


class Web(Terminal):
    @staticmethod
    def cprint(message):
        pywebio.output.put_markdown(message)

    @staticmethod
    def cinput(message):
        return pywebio.input.input(message)


io = Web()
print = io.cprint
input = io.cinput

scores = {
    "Yes": 1,
    "No": 2,
}


def get_risk_profile():
    # weights follow each question
    questions = (
        (
            "In general, would your best friend describe you as a risk taker?",
            9),
        ("You are able to save money regularly?", 1),
        ("If you lose money investing today, your current lifestyle would not "
         "be impacted?", 8),
        ("You do not need to draw down more then 5% of your investment "
         "portfolio for any major financial goal in the next five years?", 1),
        ("You can pay all your monthly bills on time -- including any credit "
         "card or any debt?", 1)

    )

    weighted_scores = []
    for question in questions:
        answer = input(f"{question[0]} (Enter Yes, No): ").title()
        weighted_scores.append(question[1] * scores[answer])
    return weighted_scores


def calculate_risk_score(responses):
    return sum(responses) / len(responses)


def assign_risk_profile(average_score):
    if average_score < 2:
        risk_profile = "Low"
    elif average_score < 3:
        risk_profile = "Moderately Low"
    elif average_score < 4:
        risk_profile = "Moderate"
    elif average_score < 5:
        risk_profile = "Moderately High"
    else:
        risk_profile = "High"
    return risk_profile


def get_personal_data():
    name = input("Your name: ")
    age = input("Your age: ")
    investment_amount = input("Your investment amount: ")
    return {'name': name, 'age': age, 'investment_amount': investment_amount}


personal_data = get_personal_data()
weighted_scores = get_risk_profile()
average_score = calculate_risk_score(weighted_scores)
risk_profile = assign_risk_profile(average_score)

print(f"""
Name: {personal_data['name']}
Age: {personal_data['age']}
Investment Amount: {personal_data['investment_amount']}

Your risk profile is: {risk_profile}
""")
