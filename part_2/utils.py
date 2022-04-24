import json


def load_candidates_from_json(path):
    with open(path, 'r', encoding='utf-8') as file:
        return json.load(file)


# (?)преобразует исходный список словарей в словарь, где ключ - ИД, значение - экземпляр класса Person
# def formatted_candidates(candidates_list):
#     basa_candidasa = {}
#     for candidate in candidates_list:
#         person = Person(candidate["id"], candidate["name"], candidate["picture"], candidate["position"],
#                         candidate["gender"], candidate["age"], candidate["skills"])
#         basa_candidasa[candidate["id"]] = person
#     return basa_candidasa


def candidate_selection_by_id(candidate_id):
    candidates_list = load_candidates_from_json("candidates.json")
    for candidate in candidates_list:
        if candidate['id'] == candidate_id:
            return candidate


def candidate_selection_by_name(candidate_name):
    candidates_list = load_candidates_from_json("candidates.json")
    result = []
    for candidate in candidates_list:
        candidate_names_list = candidate['name'].lower().split(' ')
        if candidate_name.lower() in candidate_names_list:
            result.append(candidate)
    return result


def candidate_selection_by_skill(candidate_skill):
    candidates_list = load_candidates_from_json("candidates.json")
    result = []
    for candidate in candidates_list:
        candidate_skills = candidate['skills'].lower().split(', ')
        if candidate_skill.lower() in candidate_skills:
            result.append(candidate)
    return result
