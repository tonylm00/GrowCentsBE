import joblib
import networkx as nx
import pandas as pd
from flask import request, jsonify, Blueprint
from app.esg.data_preparation.cleaning import flatten_dict, clean_decarbonization_target, merge_involvement
from app.esg.data_preparation.encoding import involvement_encoding, encoding_colors, encoding_aligned_no
from app.esg.data_preparation.run import merge_by_esg

bp = Blueprint('esg', __name__, url_prefix='/esg')

model_path = 'C:\\Users\\Tony\\Desktop\\Growcents\\app\\routes\\model.pkl'
dataset_path = 'C:\\Users\\Tony\\Desktop\\Growcents\\app\\esg\\data\\label_with_metrics.csv'


def load_model():
    try:
        print(f"Loading model from: {model_path}")  # Stampa di debug
        return joblib.load(model_path)
    except FileNotFoundError:
        print(f"Model file not found at: {model_path}")  # Stampa di debug
        return None


def get_esg_value(company_name):
    df = pd.read_csv('../esg/data/label_with_metrics.csv')
    esg_value = df.loc[df['name'] == company_name, 'esg'].values
    if len(esg_value) > 0:
        return esg_value[0]
    else:
        return None


def construct_graph(companies, relationships):
    G = nx.Graph()
    G.add_node('TARGET')

    for i, company in enumerate(companies):
        esg_value = get_esg_value(company)
        G.add_node(company, esg=esg_value)
        rel_type = relationships[i] if i < len(relationships) else 'unknown'
        G.add_edge('TARGET', company, relationship=rel_type)

    return G


@bp.route('/predict/data', methods=['POST'])
def predict_data():
    try:
        data = request.get_json()
        flattened_data = flatten_dict(data)

        df = pd.DataFrame({key: [value] for key, value in flattened_data.items()})

        column_mappings = {
            'Decarbonization_Target_target_year': 'Decarbonization Target_Target Year',
            'Decarbonization_Target_comprehensiveness': 'Decarbonization Target_Comprehensiveness',
            'Decarbonization_Target_ambition_per_annum': 'Decarbonization Target_Ambition p.a.',
            'Decarbonization_Target_temperature_goal': 'Temperature Goal',
            'No Poverty': 'sdg_No Poverty',
            'No Hunger': 'sdg_No Hunger',
            'Good Health and Well-Being': 'sdg_Good Health and Well-Being',
            'Quality Education': 'sdg_Quality Education',
            'Gender Equality': 'sdg_Gender Equality',
            'Clean Water and Sanitation': 'sdg_Clean Water and Sanitation',
            'Affordable and Clean Energy': 'sdg_Affordable and Clean Energy',
            'Decent Work and Economic Growth': 'sdg_Decent Work and Economic Growth',
            'Industry, Innovation and Infrastructure': 'sdg_Industry, Innovation and Infrastructure',
            'Reduced Inequalities': 'sdg_Reduced Inequalities',
            'Sustainable Cities and Communities': 'sdg_Sustainable Cities and Communities',
            'Responsible Consumption and Production': 'sdg_Responsible Consumption and Production',
            'Climate Action': 'sdg_Climate Action',
            'Life under Water': 'sdg_Life under Water',
            'Life on Land': 'sdg_Life on Land',
            'Peace, Justice and Strong Institutions': 'sdg_Peace, Justice and Strong Institutions',
            'Partnerships for the Goals': 'sdg_Partnerships for the Goals',
            'Controversies Environment': 'Controversies_Environment',
            'Controversies Social': 'Controversies_Social',
            'Controversies Customers': 'Controversies_Customers',
            'Controversies Human Rights & Community': 'Controversies_Human Rights & Community',
            'Controversies Labor Rights & Supply Chain': 'Controversies_Labor Rights & Supply Chain',
            'Controversies Governance': 'Controversies_Governance'
        }

        df = df.rename(columns=column_mappings)

        # Aggiungi valori predefiniti per le colonne sdg_* e Controversies mancanti
        sdg_columns = [
            'sdg_No Poverty', 'sdg_No Hunger', 'sdg_Good Health and Well-Being', 'sdg_Quality Education',
            'sdg_Gender Equality', 'sdg_Clean Water and Sanitation', 'sdg_Affordable and Clean Energy',
            'sdg_Decent Work and Economic Growth', 'sdg_Industry, Innovation and Infrastructure',
            'sdg_Reduced Inequalities', 'sdg_Sustainable Cities and Communities',
            'sdg_Responsible Consumption and Production', 'sdg_Climate Action', 'sdg_Life under Water',
            'sdg_Life on Land', 'sdg_Peace, Justice and Strong Institutions', 'sdg_Partnerships for the Goals'
        ]

        controversies_columns = [
            'Controversies_Environment', 'Controversies_Social', 'Controversies_Customers',
            'Controversies_Human Rights & Community', 'Controversies_Labor Rights & Supply Chain',
            'Controversies_Governance'
        ]

        for col in sdg_columns + controversies_columns:
            if col not in df.columns:
                df[col] = 'Aligned'  # Valore predefinito per sdg_ colonne
                if col.startswith('Controversies'):
                    df[col] = 'Green'  # Valore predefinito per Controversies colonne

        # Perform necessary cleaning and transformations
        df = clean_decarbonization_target(df)
        df = merge_involvement(df)
        df = involvement_encoding(df)
        df = encoding_colors(df)
        df = encoding_aligned_no(df)
        df = merge_by_esg(df)

        model = load_model()

        if not model:
            return jsonify({'error': 'Model not found'}), 500

        desired_feature_order = ['employees', 'altman_score', 'piotroski_score',
                                 'Decarbonization Target_Target Year',
                                 'Decarbonization Target_Comprehensiveness',
                                 'Decarbonization Target_Ambition p.a.', 'Temperature Goal',
                                 'environmental_metric', 'social_metric', 'governance_metric',
                                 'involvement_metric']

        df = df.reindex(columns=desired_feature_order)
        X = df.values

        prediction = model.predict(X)[0]
        prediction = round(prediction, 2)

        return jsonify({'esg': prediction})

    except KeyError as e:
        print(e)
        return jsonify({'error': f'Missing key: {str(e)}'}), 400
    except Exception as e:
        print(e)
        return jsonify({'error': str(e)}), 500


@bp.route('/scores', methods=['GET'])
def get_esg_scores():
    try:
        # Lista di ticker per le aziende selezionate
        selected_companies = ['IBM', 'Microsoft', 'AMD', 'Accenture', 'Google']

        df = pd.read_csv(dataset_path)
        esg_data = df[df['name'].isin(selected_companies)][['name', 'esg']]
        esg_data = esg_data.rename(columns={'name': 'company'}).to_dict(orient='records')
        print('DATI: ', jsonify(esg_data))

        return jsonify(esg_data)
    except Exception as e:
        print(e)
        return jsonify({'error': str(e)}), 500
