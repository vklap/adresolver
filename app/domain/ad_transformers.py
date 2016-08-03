from abc import abstractmethod, abstractproperty

DO_NOTHING_AD_TRANSFORMER_ID = 0
GOOGLE_AD_TRANSFORMER_ID = 1
FACEBOOK_AD_TRANSFORMER_ID = 2

GOOGLE_URI = 'www.google.com'
FACEBOOK_URI = 'www.facebook.com'


class AdTransformer(object):
    @abstractproperty
    def transformer_id(self):
        pass

    @abstractmethod
    def transform_data(self, html_data):
        pass


class DoNothingAdTransformer(AdTransformer):
    @property
    def transformer_id(self):
        return DO_NOTHING_AD_TRANSFORMER_ID

    def transform_data(self, html_data):
        return html_data


class GoogleAdTransformer(AdTransformer):
    @property
    def transformer_id(self):
        return GOOGLE_AD_TRANSFORMER_ID

    def transform_data(self, html_data):
        #TODO: e.g. find and replace 'www.google.com' with 'blah.blah.com'
        pass


class FacebookAdTransformer(AdTransformer):
    @property
    def transformer_id(self):
        return FACEBOOK_AD_TRANSFORMER_ID

    def transform_data(self, html_data):
        #TODO: e.g. find and replace 'www.facebook.com' with 'blah.blah.com'
        pass
