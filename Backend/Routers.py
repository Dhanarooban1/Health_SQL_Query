import sqlite3
from flask import Blueprint, request, jsonify
from LLMQueryGenerator import LLM_Data_Controller

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/post/query', methods=['POST'])

def get_data_from_llm():
    try:
        data = request.json
        if not data:
            return jsonify({"error": "No input data provided"}), 400
        
        user_question = data.get('question')
        if not user_question:
            return jsonify({"error": "The 'question' field is missing"}), 400
        data_controller = LLM_Data_Controller()
        gemini_query = data_controller.generate_gemini_query(user_question)
        
        from SQLController import execute_query
        connection = sqlite3.connect("test.db")
        cursor = connection.cursor()
        results = execute_query(gemini_query, cursor)
        cursor.close()
        connection.close()
        return jsonify({"query": gemini_query, "results": results}), 200

    except Exception as e:
        print(f"Error occurred: {str(e)}")
        return jsonify({"error": str(e)}), 500

