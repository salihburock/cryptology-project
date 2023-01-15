class Constants:
    # CONSTANTS
    def __init__(self, 
        HOST = r'127.0.0.1',
        PORT = 8081,
        PROJECT_NAME = r"Kodların Seyyahı",
        OTEL_NAME = r"PEKMEZ TURİZM",
        STAR_SYMBOL = '✪',
        STAR_COUNT = 5,
    ):
        self.host = HOST
        self.port = PORT
        self.project_name = PROJECT_NAME
        self.otel_name = OTEL_NAME
        self.star_symbol = STAR_SYMBOL
        self.star_count = STAR_COUNT

        STAR_STR = self.star_count * self.star_symbol
        self.start_str = STAR_STR
        TITLE = f'{self.project_name} | {self.otel_name} ({self.start_str})'
        self.title = TITLE