from django import template

register = template.Library()


@register.filter(name='has_group')
def has_group(user, groups_name):
    """ check if groups of the user is in alowed groups """
    groups = user.groups.all()
    current_user_groups = groups_name.split(',')

    for group in groups:
        if str(group) in current_user_groups:
            return True
    return False
