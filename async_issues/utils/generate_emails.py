import random
import string
from typing import List


def random_email_generator(email_length: int, number_of_emails: int) -> List[str]:
    return [''.join(random.choice(string.ascii_letters) for _ in range(email_length)) for _ in range(number_of_emails)]

