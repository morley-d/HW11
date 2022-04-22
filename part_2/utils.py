import json


# - `load_candidates_from_json(path)` – возвращает список всех кандидатов
#
# - `get_candidate(candidate_id)` – возвращает одного кандидата по его id
#
# - `get_candidates_by_name(candidate_name)` – возвращает кандидатов по имени
#
# - `get_candidates_by_skill(skill_name)` – возвращает кандидатов по навыку

def get_candidates(path):
    with open(path, 'r', encoding='utf-8') as file:
        return json.load(file)


def formatted_candidates(candidates_list):
    result = '<pre>'
    for candidate in candidates_list:
        result += (
            f'<h3>Имя кандидата - <mark><em>{candidate["name"]}</em></mark></h3>'
            f'Позиция кандидата - {candidate["position"]}<br>'
            f'Навыки через запятую - {candidate["skills"]}<br>'
            f'Ссыль на профиль - <a  href="/candidates/{candidate["id"]}">Profile</a><br><br>'
        )
    result += '<pre>'
    return result


def candidate_selection_by_id(candidates_list, candidate_id):
    for candidate in candidates_list:
        if candidate['id'] == candidate_id:
            return candidate


def candidate_selection_by_skill(candidates_list, candidate_skill):
    result = []
    for candidate in candidates_list:
        candidate_skills = candidate['skills'].lower().split(', ')
        if candidate_skill in candidate_skills:
            result.append(candidate)
    return result
