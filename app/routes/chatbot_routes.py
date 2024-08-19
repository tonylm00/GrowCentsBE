import os
from openai import OpenAI
from flask import request, jsonify, Blueprint

bp = Blueprint('chatbot', __name__, url_prefix='/chatbot')


client = OpenAI(
    api_key=os.environ['OPENAI_SECRET_KEY'],
)


@bp.route('/', methods=['POST'])
def chatbot():
    role = "Rispondi alle domande e fornisci consigli sulla finanza personale in modo semplice e chiaro, " \
           "senza utilizzare tecnicismi inutili." \
           "Mantieni sempre un tono rassicurante e parla in italiano, rendendo le informazioni accessibili anche a " \
           "chi ha poca esperienza nel campo finanziario. " \
           "Se qualcuno ti chiede di disinvestire, sottolinea l'importanza di restare investiti nel lungo termine, " \
           "suggerendo alternative come cambiare asset class piuttosto che fare operazioni impulsive. " \
           "Promuovi l'importanza di conoscere se stessi, ricordando l'obbligo legale del questionario MIFID, " \
           "che può aiutare a definire la propria tolleranza al rischio. " \
           "Non dare mai consigli finanziari specifici, ma invita gli utenti a consultare " \
           "consulenti finanziari accreditati per questioni particolari. " \
           "Ogni tanto, cita frasi dal Poor Richard's Almanack per ispirare e motivare gli utenti " \
           "a gestire meglio le loro finanze. Se ti fanno una domanda che va fuori dall'argomenti " \
           "finanza e finanza personale non rispondere e dici che puoi rispondere solo a domande relative " \
           "all'argomento, invitandolo a fare una domanda opportuna."

    try:
        user_message = request.json.get('message')

        response = client.chat.completions.create(
            model="gpt-4o-mini-2024-07-18",
            messages=[
                {"role": "system", "content": role},
                {"role": "user", "content": user_message},
            ],
        )

        assistant_message = response.choices[0].message.content

        return jsonify({'response': assistant_message})

    except Exception as e:
        return jsonify({'error': str(e)}), 500
