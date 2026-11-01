from pyscript import document

def candidate_checker(e):
    club_members = ["Kitana Kahn", "Kung Lao", "Liu Kang", "Sonya Blade", "Johnny Cage"]
    f_name = document.getElementById('first_name').value
    l_name = document.getElementById('last_name').value
    candidate = f_name + ' ' + l_name

    member_checker = candidate in club_members
    if member_checker:
        message = f'Congratulations {candidate}, you are now part of the marching band!'
    else:
        message = f'Sorry {candidate}, your name is not on the list.'

    document.getElementById('result').innherHTML = message[member_checker]