from app.domain.ad_transformers import DO_NOTHING_AD_TRANSFORMER_ID, GOOGLE_AD_TRANSFORMER_ID, FACEBOOK_AD_TRANSFORMER_ID
from app.domain.ad_transformers import GOOGLE_URI, FACEBOOK_URI


def extract_ad_transformer_id(connection_wrapper):
    if connection_wrapper.uri == GOOGLE_URI:
        return GOOGLE_AD_TRANSFORMER_ID

    if connection_wrapper.uri == FACEBOOK_URI:
        return FACEBOOK_AD_TRANSFORMER_ID

    # default
    return DO_NOTHING_AD_TRANSFORMER_ID





