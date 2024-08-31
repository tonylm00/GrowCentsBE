from flask import Blueprint, request, jsonify

bp = Blueprint('mifid', __name__, url_prefix='/mifid')


def calculate_risk_profile(answers):
    score = sum(answers.values())
    if score <= 10:
        return 'Basso\n', '\n75% Obbligazioni\n25% Azioni\n\nDisclaimer: Questo profilo di rischio e questa allocazione degli asset non sono consigli finanziari. È importante consultare un consulente finanziario per adattare la strategia di investimento alle proprie esigenze e circostanze individuali.'
    elif score <= 15:
        return 'Moderato\n', '\n55% Obbligazioni\n45% Azioni\n\nDisclaimer: Questo profilo di rischio e questa allocazione degli asset non sono consigli finanziari. È importante consultare un consulente finanziario per adattare la strategia di investimento alle proprie esigenze e circostanze individuali.'
    elif score <= 20:
        return 'Medio-Alto\n', '\n35% Obbligazioni\n65% Azioni\n\nDisclaimer: Questo profilo di rischio e questa allocazione degli asset non sono consigli finanziari. È importante consultare un consulente finanziario per adattare la strategia di investimento alle proprie esigenze e circostanze individuali.'
    else:
        return 'Alto\n', '\n10% Obbligazioni\n90% Azioni\n\nDisclaimer: Questo profilo di rischio e questa allocazione degli asset non sono consigli finanziari. È importante consultare un consulente finanziario per adattare la strategia di investimento alle proprie esigenze e circostanze individuali.'


@bp.route('/execute', methods=['POST'])
def execute_mifid():
    data = request.json
    answers = {
        'question_1': data.get('question_1', 0),
        'question_2': data.get('question_2', 0),
        'question_3': data.get('question_3', 0),
        'question_4': data.get('question_4', 0),
        'question_5': data.get('question_5', 0),
        'question_6': data.get('question_6', 0),
        'question_7': data.get('question_7', 0),
        'question_8': data.get('question_8', 0),
        'question_9': data.get('question_9', 0),
        'question_10': data.get('question_10', 0),
        'question_11': data.get('question_11', 0),
        'question_12': data.get('question_12', 0),
    }
    risk_profile, asset_allocation = calculate_risk_profile(answers)

    return jsonify(risk_profile, asset_allocation)
