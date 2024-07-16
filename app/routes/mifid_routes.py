from flask import Blueprint, request, jsonify

bp = Blueprint('mifid', __name__, url_prefix='/mifid')


def calculate_risk_profile(answers):
    score = sum(answers)
    if score <= 10:
        return 'Basso', '70% Obbligazioni, 20% Azioni, 10% Liquidità'
    elif score <= 15:
        return 'Moderato', '50% Obbligazioni, 40% Azioni, 10% Liquidità'
    elif score <= 20:
        return 'Medio-Alto', '30% Obbligazioni, 60% Azioni, 10% Liquidità'
    else:
        return 'Alto', '10% Obbligazioni, 80% Azioni, 10% Liquidità'


@bp.route('/execute', methods=['POST'])
def execute_mifid():
    question_1 = request.json['question_1']
    question_2 = request.json['question_2']
    question_3 = request.json['question_3']
    question_4 = request.json['question_4']
    question_5 = request.json['question_5']
    question_6 = request.json['question_6']

    answers = [question_1, question_2, question_3, question_4, question_5, question_6]
    risk_profile, asset_allocation = calculate_risk_profile(answers)

    return jsonify(risk_profile, asset_allocation)
