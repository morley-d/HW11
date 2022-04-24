import json


# загрузка исходных данных из json файла
def load_candidates_from_json(path):
    with open(path, 'r', encoding='utf-8') as file:
        return json.load(file)


# из списка выбирается кандидат с заданным ID
def candidate_selection_by_id(candidate_id):
    candidates_list = load_candidates_from_json("candidates.json")
    for candidate in candidates_list:
        if candidate['id'] == candidate_id:
            return candidate


# из списка выбирается кандидат с заданным именем
def candidate_selection_by_name(candidate_name):
    candidates_list = load_candidates_from_json("candidates.json")
    result = []
    for candidate in candidates_list:
        candidate_names_list = candidate['name'].lower().split(' ')
        if candidate_name.lower() in candidate_names_list:
            result.append(candidate)
    return result


# из списка выбираются кандидаты с заданным скиллом
def candidate_selection_by_skill(candidate_skill):
    candidates_list = load_candidates_from_json("candidates.json")
    result = []
    for candidate in candidates_list:
        candidate_skills = candidate['skills'].lower().split(', ')
        if candidate_skill.lower() in candidate_skills:
            result.append(candidate)
    return result
