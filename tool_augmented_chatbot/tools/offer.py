# chatbot3/tools/offer.py
from templates.offer_letter_template import OFFER_TEMPLATE

def generate_offer_letter(name, position, company, skills, hr_name):
    return OFFER_TEMPLATE.format(
        name=name,
        position=position,
        company=company,
        skills=skills,
        hr_name=hr_name
    )
