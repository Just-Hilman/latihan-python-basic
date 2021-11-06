def replace_domain(email, old_domain, new_domain):
    if "@" + old_domain in email:
        index = email.index("@" + old_domain)
        new_email = email[:index] + "@" + new_domain
        return new_email
    return email

print(replace_domain("hilman@ciwaru.com", "ciwaru.com", "google.com"));
print(replace_domain("hilman@yahoo.com", "ciwaru.com", "google.com"));
print(replace_domain("hilman@google.com", "ciwaru.com", "google.com"));



print(replace_domain("hilman@ciwaru.com", "ciwaru.com", "google.com"));
print(replace_domain("John@ciwaru.com", "ciwaru.com", "google.com"));
print(replace_domain("Jane@ciwaru.com", "ciwaru.com", "google.com"));
print(replace_domain("Mutia@ciwaru.com", "ciwaru.com", "google.com"));