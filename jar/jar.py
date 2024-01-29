class Jar:
    def __init__(self, capacity=12, size=0):
        if isinstance(capacity,int) and capacity > 0:
            self._capacity = capacity
        else:
            raise ValueError('This Jar even exists?')

        if isinstance(size,int) and size >= 0:
            self._size = size
        elif size > self._capacity:
            raise ValueError("Lies! This Jar can't hold that many cookies!")
        else:
            raise ValueError("Nah, this doesn't make sense... Try again!")

    def __str__(self):
        return '\U0001F36A' * self._size

    def deposit(self, n=1):
        if self._size + n <= self.capacity:
            self._size += n
        else:
            raise ValueError('Jar is already full my friend')

    def withdraw(self, n=1):
        if self._size >= n:
            self._size -= n
        else:
            raise ValueError('No more cookies :(')

    @staticmethod
    def create():
        jar = Jar()
        jar.capacity = int(input('How many cookies can this jar fit? '))
        jar.size = int(input('How many cookies are in this jar rigth now? '))
        return jar

    @property #getter
    def capacity(self):
        return self._capacity

    @capacity.setter #setter
    def capacity(self, capacity):
        if capacity >= 1:
            self._capacity = capacity
        else:
            raise ValueError('This Jar even exists?')

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size >= 0 and size <= self._capacity:
            self._size = size
        elif size > self._capacity:
            raise ValueError("Lies! This Jar can't hold that many cookies!")
        else:
            raise ValueError("Nah, this doesn't make sense... Try again!")

def main():
    jar = Jar.create()
    print(jar)

if __name__ == "__main__":
    main()
