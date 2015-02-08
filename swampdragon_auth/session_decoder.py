import base64
import ast
from django.utils.encoding import force_unicode

def decode_session(session):
    decoded_session = session.get_decoded()

    if decoded_session:
        return decoded_session

    # If Django returns an empty decoded session, decoding is done manually  
    session_data = force_unicode(session.session_data)
    encoded_data = base64.decodestring(session_data)
    hash, pickled = encoded_data.split(':', 1)

    return ast.literal_eval(pickled)