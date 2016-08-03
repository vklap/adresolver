import uuid

from app.domain.ad_transformers import DO_NOTHING_AD_TRANSFORMER_ID, GOOGLE_AD_TRANSFORMER_ID, FACEBOOK_AD_TRANSFORMER_ID
from app.domain.ad_transformers import DoNothingAdTransformer, GoogleAdTransformer, FacebookAdTransformer

AD_TRANFORMER_BY_TRANSFORMER_ID = {
    DO_NOTHING_AD_TRANSFORMER_ID: DoNothingAdTransformer,
    GOOGLE_AD_TRANSFORMER_ID: GoogleAdTransformer,
    FacebookAdTransformer: FacebookAdTransformer
}


def create_ad_transformer(transformer_id):
    transfomer = AD_TRANFORMER_BY_TRANSFORMER_ID.get(transformer_id)

    if transfomer is None:
        raise ValueError("factories.create_ad_tranformer failed because transformer_id='{tranformer_id}' is not supported")

    transformer_instance = transfomer()
    return transformer_instance


def create_session_id():
    return uuid.uuid1()
