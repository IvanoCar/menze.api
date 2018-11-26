class Auth:
    def __init__(self):
        self.GET_KEY = 'KEY'
        self.POST_KEY = "KEY"
        self.N_POST_KEY = "KEY"
        self.W_POST_KEY = "KEY"

    def get(self, request):
        try:
            key = request.headers['api-key']
            if not key == self.GET_KEY:
                return {'message': 'Invalid API key provided.'}, True
        except KeyError:
            return {'message': 'No API key provided.'}, True

        return None, False

    def post(self, request_json):
        try:
            key = request_json['api-key']
            if not key == self.POST_KEY:
                return {'message': 'Invalid API key provided.'}, True
        except KeyError:
            return {'message': 'No API key provided.'}, True

        return None, False

    def notification_post(self, request_json):
        try:
            key = request_json['api-key']
            if not key == self.N_POST_KEY:
                return {'message': 'Invalid API key provided.'}, True
        except KeyError:
            return {'message': 'No API key provided.'}, True

        return None, False

    def weather_post(self, request_json):
        try:
            key = request_json['api-key']
            if not key == self.W_POST_KEY:
                return {'message': 'Invalid API key provided.'}, True
        except KeyError:
            return {'message': 'No API key provided.'}, True

        return None, False
