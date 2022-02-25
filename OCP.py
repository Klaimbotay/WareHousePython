class InfoPrinter():
    def __init__(self, object):
        self.object = object

    def show_info(self):
        lines = []
        with open(f'{self.object}', 'r') as db:
            for line in db:
                if line == '\n':
                    continue
                lines.append(line)

        for line in lines:
            print(line, end='')