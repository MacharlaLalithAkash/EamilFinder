from permutations import email_permuter


def permute_email(first_name, last_name, domain_name):
    return email_permuter.all_email_permuter(first_name=first_name,
                                             last_name=last_name,
                                             domain_name=domain_name
                                             )
