import os

import jellyfish
from flask import Flask, request, jsonify

app = Flask(__name__)

admin_skill_list = ['Python', 'relational database', 'Software engineering', 'data science', 'NLP',
                    'natural language processing']


def levenshtein_similarity(a, b):
    return 1 - (jellyfish.levenshtein_distance(a.lower(), b.lower()) / max(len(a), len(b)))

def jaccard_similarity(a, b):
    set_a, set_b = set(a.lower().split()), set(b.lower().split())
    return len(set_a & set_b) / len(set_a | set_b)

def exact_match(a, b):
    return 1.0 if a.lower() == b.lower() else 0.0

def get_best_matches(query):
    matches = []
    for skill in admin_skill_list:
        scores = {
            "skill": skill,
            "exact_match": exact_match(query, skill),
            "levenshtein": levenshtein_similarity(query, skill),
            "jaccard": jaccard_similarity(query, skill)
        }
        scores["final_score"] = max(scores["exact_match"], scores["levenshtein"], scores["jaccard"])
        matches.append(scores)

    matches.sort(key=lambda x: x["final_score"], reverse=True)
    return matches[:3]

@app.route('/match', methods=['POST'])
def match_skill():
    data = request.json
    query = data.get("skill", "").strip()

    if not query:
        return jsonify({"error": "Skill name is required"}), 400

    results = get_best_matches(query)
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
