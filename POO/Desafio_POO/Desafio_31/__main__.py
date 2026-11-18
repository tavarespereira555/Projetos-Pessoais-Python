from rich import inspect


class Retangulo:
    def __init__(self, base= 1, altura= 1):
        self._base= base
        self._altura= altura
        self._area= self._base * self._altura
        self.area= self._base * self._altura

        @property
        def base(self):
            return self._base

def main():
    r= Retangulo(8, 4)
    inspect(r, private=True, methods=True)

if __name__ == '__main__':
    main()