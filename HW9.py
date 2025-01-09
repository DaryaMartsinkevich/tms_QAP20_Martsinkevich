class Cinema:
    def __init__(self, city, name, format):
        self.city: str = city
        self.name: str = name
        self.format: str = format


class TicketOffice(Cinema):
    def __init__(self, name_of_movie, genre, _hall, time, places, tickets):
        super().__init__("Гродно", "Красная звезда", "3D")
        self.name_of_movie: str = name_of_movie
        self.genre: str = genre
        self._hall: int = _hall
        self.time: float = time
        self.places: int = places
        self.tickets: int = tickets

    def addition_info(self):
        print(f"Название кинотеатра: {self.name}\n"
              f"Название фильма: {self.name_of_movie}\n"
              f"Жанр: {self.genre}\n"
              f"Начало фильма: {self.time}\n"
              f"Номер зала: {self._hall}")

    def ticket_info(self, count):
        self.tickets -= count
        self.places -= count
        print(f"Осталось билетов: {self.tickets}\n"
              f"Свободных мест: {self.places}\n")

    def new_info(self, new_movie, genre, time, _hall):
        self.name_of_movie = new_movie
        self.genre = genre
        self.time = time
        self._hall = _hall
        print(f"Добавлен новый фильм: {new_movie}\n"
              f"Жанр: {self.genre}\n"
              f"Начало фильма: {self.time}\n"
              f"Номер зала: {self._hall}")


movie = TicketOffice("Аватар", "fantasy", 1, 10.15, 60, 60)
movie.addition_info()
movie.ticket_info(15)
movie.new_info("Жизнь Пи", "adventure-drama", 15.15, 2)